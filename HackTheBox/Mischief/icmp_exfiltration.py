#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import sniff, ICMP


def process_packet(packet):
    if packet.haslayer(ICMP) and packet[ICMP].type == 0:
        data = packet[ICMP].load[-8:]
        try:
            print(f"{data.decode('utf-8')}", end="")
        except UnicodeDecodeError:
            pass

        with open("./exfil", "a+b") as f:
            f.write(data)


if __name__ == "__main__":
    sniff(iface="tun0", prn=process_packet)
