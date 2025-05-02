def generate_snort_rule(network, threshold):
    rule = f"alert arp {network} any -> 255.255.255.255 any (msg:\"Suspicious ARP Broadcast\"; arp_opcode:REPLY; threshold: type both, track by_src, count {threshold}, seconds 60; sid:1000001;)"
    return rule

# User input
network = input("Enter network to monitor (e.g., 192.168.1.0/24): ").strip()
threshold = input("Enter threshold for ARP packets (e.g., 10): ").strip()

# Generate and display rule
rule = generate_snort_rule(network, threshold)
print(f"Snort Rule: {rule}")