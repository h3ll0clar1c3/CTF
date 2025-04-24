# File: generate_pcap.py
from scapy.all import *

packet = IP(dst="10.0.0.1") / TCP(dport=80) / "CTF{network_flag}"
wrpcap("challenge.pcap", [packet])