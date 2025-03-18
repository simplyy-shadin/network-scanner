from scapy.all import ARP, Ether, srp
import ipaddress

def scan_ip_range(ip_range):
    # Create an ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    print("[+] Scanning the network... (Press CTRL+C to stop)\n")

    try:
        # Send the packet and receive the response
        result = srp(packet, timeout=2, verbose=0)[0]

        # Process results in real-time
        if result:
            for sent, received in result:
                print(f"IP: {received.psrc}, MAC: {received.hwsrc}")
        else:
            print("[-] No active hosts found in the specified range.")

    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user.")

# Get user input and run scan
if __name__ == "__main__":
    ip_range = input("Enter an IP range to scan (e.g., 192.168.1.0/24): ")
    try:
        # Validate the IP range
        ipaddress.ip_network(ip_range, strict=False)
        scan_ip_range(ip_range)
    except ValueError:
        print("[-] Invalid IP range. Please enter a valid range (e.g., 192.168.1.0/24).")


# 172.16.4.102/16
# sudo env "PATH=$PATH" python3 port-finder.py
