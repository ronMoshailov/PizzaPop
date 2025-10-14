from scapy.all import IP, UDP, Raw, send
import time

TARGET_IP = "192.168.15.92"   # הטלפון לפי הקוד שלך
TARGET_PORT = 5060

def send_fake_invite(number="0541234567"):
    payload = (
        f"INVITE sip:{number}@{TARGET_IP} SIP/2.0\r\n"
        "From: <sip:TESTER@SIM>\r\n"
        "To: <sip:{number}@SIM>\r\n"
        "Call-ID: 1234@SIM\r\n"
        "CSeq: 1 INVITE\r\n"
        "Contact: <sip:TESTER@SIM>\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    )
    pkt = IP(dst=TARGET_IP) / UDP(dport=TARGET_PORT, sport=5060) / Raw(load=payload.encode())
    send(pkt, verbose=False)
    print(f"Sent INVITE for {number}")


while True:
    send_fake_invite("0548348091")  # תחליף במספר אמיתי שקיים ב-DB שלך
    time.sleep(5)
