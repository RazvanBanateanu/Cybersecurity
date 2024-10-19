from scapy.all import ARP, Ether, srp
import ipaddress

def scan_network(network):
    # Create an ARP request packet
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and receive the response
    result = srp(packet, timeout=2, verbose=False)[0]

    # List to hold discovered devices
    devices = []

    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    # Define the network range (modify as needed)
    # Example: "192.168.1.0/24"
    network = input("Enter the network to scan (e.g., 192.168.1.0/24): ")
    
    try:
        # Validate network input
        ipaddress.ip_network(network)
        print(f"Scanning network: {network}...")
        
        # Scan the network
        devices = scan_network(network)

        # Print the discovered devices
        if devices:
            print("Discovered devices:")
            for device in devices:
                print(f"IP: {device['ip']}, MAC: {device['mac']}")
        else:
            print("No devices found.")

    except ValueError:
        print("Invalid network format. Please use CIDR notation (e.g., 192.168.1.0/24).")

if __name__ == "__main__":
    main()

