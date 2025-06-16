from scapy.all import sniff

def packet_sniffer(packet):
    print(packet.summary())

    

def main():
    sniff(prn=packet_sniffer, store=0)

if __name__ == "__main__":
    main()