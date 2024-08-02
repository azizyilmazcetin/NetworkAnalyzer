from scapy.all import rdpcap

# Pcap dosyasını oku
packets = rdpcap("captured_packets.pcap")

# Port numaralarını saymak için bir sözlük
port_counts = {}

# Her bir paketi analiz et
for packet in packets:
    if packet.haslayer('TCP'):
        port = packet['TCP'].dport
        if port in port_counts:
            port_counts[port] += 1
        else:
            port_counts[port] = 1

# Belirli bir port numarasına çok fazla bağlantı varsa bildir
threshold = 100
for port, count in port_counts.items():
    if count > threshold:
        print(f"Port {port} has high traffic: {count} packets")