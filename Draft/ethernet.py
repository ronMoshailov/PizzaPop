"""
sip_sniffer.py
לכידה פרומיסקואסית של חבילות ברשת; מדפיס מספרים מתוך SIP INVITE
הרץ כמנהל / root. צריך scapy והתקנת Npcap (Windows) או libpcap (Linux).
"""

from scapy.all import sniff, IP, Raw
import re
import time

# כתובת ה‑Yealink שלך (שנה אם צריך)
PHONE_IP = "192.168.15.92"

# פורטים/מזהים שנבדוק (SIP בדרך כלל 5060, לעתים 5061/5062)
SIP_PORTS = {5060, 5061, 5062}

# regexes לחילוץ מספרים מתוך INVITE/From headers
INVITE_NUM_RE = re.compile(r'INVITE\s+sip:(\+?\d+)@', re.IGNORECASE)
FROM_SIP_RE   = re.compile(r'From:.*?<sip:(\+?\d+)@', re.IGNORECASE)
GENERIC_DIGITS_RE = re.compile(r'(\+?\d{6,15})')  # גיבוי: תופס רצף ספרות ארוך

# debounce: לא להדפיס באותו מספר יותר מפעם אחת בפרק זמן קצר
seen = {}
DEBOUNCE_SECONDS = 4.0

def extract_number_from_payload(payload):
    """מנסה לשלוף מספר בדרכים שונות מהטקסט הגולמי של ה-SIP"""
    if not payload:
        return None
    # 1) INVITE sip:NUMBER@
    m = INVITE_NUM_RE.search(payload)
    if m:
        return m.group(1)
    # 2) From: <sip:NUMBER@
    m = FROM_SIP_RE.search(payload)
    if m:
        return m.group(1)
    # 3) חיפוש גנרי של רצף ספרות (גיבוי)
    m = GENERIC_DIGITS_RE.search(payload)
    if m:
        return m.group(1)
    return None

def should_print_number(num):
    now = time.time()
    last = seen.get(num)
    if last and (now - last) < DEBOUNCE_SECONDS:
        return False
    seen[num] = now
    return True

def packet_handler(pkt):
    # רק IPv4 וחבילות עם payload
    if not pkt.haslayer(IP):
        return
    ip = pkt[IP]
    src = ip.src
    dst = ip.dst

    # בדוק אם אחד הכתובות תואמת את הטלפון
    if src != PHONE_IP and dst != PHONE_IP:
        return  # לא קשור אלינו

    # אם ה‑IP layer קיים, נבדוק פורטים (אם יש UDP/TCP) - לא חובה אך מייעל
    sport = None
    dport = None
    if pkt.haslayer("UDP"):
        sport = pkt["UDP"].sport
        dport = pkt["UDP"].dport
    elif pkt.haslayer("TCP"):
        sport = pkt["TCP"].sport
        dport = pkt["TCP"].dport

    # אם יש פורטים ונראה שאינם SIP/קרובים, אפשר להמשיך
    if sport and dport:
        if sport not in SIP_PORTS and dport not in SIP_PORTS:
            # עדיין ייתכן שתכיל SIP בדרכים מיוחדות; אבל לרוב זורקים
            pass

    # חפש payload טקסטואלי
    payload = None
    if pkt.haslayer(Raw):
        try:
            payload = pkt[Raw].load.decode('utf-8', errors='ignore')
        except Exception:
            payload = str(pkt[Raw].load)

    if not payload:
        return

    # נבדוק אם זו הודעת SIP INVITE או שכוללת מילות מפתח של SIP
    if ("INVITE" in payload) or ("SIP" in payload) or ("From:" in payload) or ("To:" in payload):
        num = extract_number_from_payload(payload)
        if num and should_print_number(num):
            direction = "->" if src == PHONE_IP else "<-"
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {direction} {num}   (src={src} dst={dst})")
            # אופציונלי: הדפס את השורה המלאה לצורכי דיבוג
            # print("PAYLOAD:", payload.splitlines()[:20])

if __name__ == "__main__":
    # רשימת ממשקי ברירת מחדל: None יבחר את הראשון; אפשר להעביר iface="Ethernet" אם צריך
    print("Starting SIP sniffer (promiscuous). Run as admin/root. Phone IP:", PHONE_IP)
    # sniff יכול להיות מסונן גם ע"י BPF filter: כאן נשתמש ב‑udp or tcp to reduce noise
    # אפשר לשנות filter ל־"udp port 5060 or tcp port 5060" אם רוצים
    sniff(prn=packet_handler, store=False, filter="udp or tcp", promisc=True)
