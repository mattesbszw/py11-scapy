import argparse
from scapy.all import rdpcap

def do_analyse(i_packet_list):

    # ...

    return

def main(): 
    
    argParser = argparse.ArgumentParser()
    argParser.add_argument("filename", help="pcap file name")
    args = argParser.parse_args()

    if args.filename == None:
        print("pcap file name is mandatory!")
        exit()

    packet_list = rdpcap(args.filename)
    do_analyse(packet_list)

if __name__ == "__main__":
    main()

