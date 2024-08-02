from scapy.all import rdpcap

# Pcap dosyasını oku
packets = rdpcap("captured_packets.pcap")

# Her bir paketi analiz et
for packet in packets:
    print(packet.summary())