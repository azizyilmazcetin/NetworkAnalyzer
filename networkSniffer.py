from scapy.all import sniff, PcapWriter

# Paketleri yakalayan fonksiyon
def packet_callback(packet):
    print(packet.summary())
    # PcapWriter ile yakalanan paketleri pcap dosyasına yaz
    writer.write(packet)

# PcapWriter objesi
writer = PcapWriter("captured_packets.pcap", append=True, sync=True)

# Ağ trafiğini yakala
sniff(prn=packet_callback, store=0)