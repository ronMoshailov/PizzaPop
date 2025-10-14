from scapy.all import IP, UDP, Raw, send
import time

LOOP = "127.0.0.1"
PORT = 5060

def build(called="0548348091", caller="sip:tester@local"):
    return (f"INVITE sip:{called}@{LOOP}:{PORT} SIP/2.0\r\n"
            f"Via: SIP/2.0/UDP {LOOP}:{PORT};branch=z9hG4bK776asdhds\r\n"
            f"Max-Forwards: 70\r\n"
            f"From: \"{caller}\" <{caller}>;tag=1928301774\r\n"
            f"To: <sip:{called}@{LOOP}>\r\n"
            f"Call-ID: a84b4c76e66710@{LOOP}\r\n"
            f"CSeq: 1 INVITE\r\n"
            f"Contact: <{caller}>\r\n"
            f"Content-Type: application/sdp\r\n"
            f"Content-Length: 0\r\n\r\n")

print("Starting to send simulated INVITE to 127.0.0.1:5060 every 3s (Ctrl+C to stop)")
i = 1
try:
    while True:
        payload = build(called=f"0548348{100 + (i % 900)}")
        pkt = IP(src=LOOP, dst=LOOP) / UDP(sport=PORT, dport=PORT) / Raw(load=payload)
        send(pkt, verbose=False)
        print(f"sent simulated INVITE #{i}")
        i += 1
        time.sleep(3)
except KeyboardInterrupt:
    print("\nStopped by user.")
