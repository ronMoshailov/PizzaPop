from scapy.all import sniff

# data
phone_ip = "192.168.15.12"
pc_ip = "192.168.15.10"

# פונקציה שתטפל בכל חבילה
def handle_packet(pkt):
    if pkt.haslayer('UDP') and pkt.haslayer('Raw'):
        print("[+] Received UDP packet")
        data = pkt['Raw'].load.decode(errors='ignore')
        if "INVITE sip:" in data:
            # חילוץ המספר שמתקשרים אליו (Called Number)
            start = data.find("INVITE sip:") + len("INVITE sip:")
            end = data.find("@", start)
            number = data[start:end]

            # חילוץ ה-Caller ID מתוך From:
            caller = ""
            if "From:" in data:
                f_start = data.find("From:") + len("From:")
                f_end = data.find("\r\n", f_start)
                caller = data[f_start:f_end].strip()

            print(f"נכנסת שיחה! Caller: {caller}, Called: {number}")

# מתחיל לקלוט חבילות בזמן אמת
# -sniff- is a function that allows you to “capture” network packets in real time,
#         meaning it listens to all the packets passing through your network interface and lets you process them as needed.
# SIP works in port 5060
# one of them is phone_ip (destination or target)
sniff(filter=f"host {phone_ip} and udp port 5060", prn=handle_packet)

# ((ip.src == 192.168.15.12 && ip.dst == 192.168.15.10) || (ip.src == 192.168.15.10 && ip.dst == 192.168.15.12))
# Installing Npcap

