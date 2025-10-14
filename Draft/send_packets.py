from scapy.all import IP, UDP, Raw, send
import time

# כתובות
phone_ip = "192.168.15.12"   # ה"טלפון" – זה היעד (dst)
pc_ip = "192.168.15.10"      # המחשב שלך – זה המקור (src)

# פונקציה לבניית חבילת SIP INVITE
def build_invite_packet(caller="sip:1001@domain.com", called="0548348091"):
    sip_payload = f"""INVITE sip:{called}@{phone_ip}:5060 SIP/2.0
Via: SIP/2.0/UDP {pc_ip}:5060;branch=z9hG4bK776asdhds
Max-Forwards: 70
From: "{caller}" <{caller}>;tag=1928301774
To: <sip:{called}@{phone_ip}>
Call-ID: a84b4c76e66710@{pc_ip}
CSeq: 314159 INVITE
Contact: <{caller}>
Content-Type: application/sdp
Content-Length: 0

"""
    pkt = IP(src=pc_ip, dst=phone_ip) / UDP(sport=5060, dport=5060) / Raw(load=sip_payload)
    return pkt

# שליחה חוזרת כל 3 שניות
print("[+] מתחיל לשדר חבילות INVITE כל 3 שניות...")
counter = 1
try:
    while True:
        pkt = build_invite_packet(
            caller="sip:tester@local",
            called="0548348091"
        )
        send(pkt, verbose=False)
        print(f"send fake packet number {counter}")
        counter+=1
        time.sleep(3)

except KeyboardInterrupt:
    print("\n[!] הופסק על ידי המשתמש.")
