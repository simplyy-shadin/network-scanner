
# Network Scanner

A simple Python script to scan an IP range for active hosts using ARP requests. This tool identifies live devices on a network by returning their IP addresses and corresponding MAC addresses.

## Features
- Scans a specified IP range (e.g., `192.168.1.0/24`) for active devices.
- Displays IP and MAC addresses of responding hosts in real-time.
- Handles invalid input with user-friendly error messages.
- Allows the user to stop the scan with `CTRL+C`.

## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Scapy**: A powerful packet manipulation library for Python.
- **Root/Administrator Privileges**: Required for sending raw packets (e.g., run with `sudo` on Linux).

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/network-scanner.git
   cd network-scanner
   ```
2. Install the required Python package:
   ```bash
   pip install scapy
   ```

## Usage
1. Run the script:
   ```bash
   sudo python3 network_scanner.py
   ```
   *Note*: Use `sudo` on Linux or run as Administrator on Windows, as raw packet operations require elevated privileges.

2. Enter an IP range when prompted (e.g., `192.168.1.0/24`).

3. The script will display the IP and MAC addresses of active devices on the network:
   ```
   [+] Scanning the network... (Press CTRL+C to stop)

   IP: 192.168.1.1, MAC: 00:14:22:01:23:45
   IP: 192.168.1.100, MAC: 00:16:17:2A:3B:4C
   ```

4. Press `CTRL+C` to stop the scan at any time.

## Example
```bash
$ sudo python3 network_scanner.py
Enter an IP range to scan (e.g., 192.168.1.0/24): 192.168.1.0/24
[+] Scanning the network... (Press CTRL+C to stop)

IP: 192.168.1.1, MAC: 00:14:22:01:23:45
IP: 192.168.1.100, MAC: 00:16:17:2A:3B:4C
[-] No more active hosts found in the specified range.
```

## Error Handling
- If an invalid IP range is provided (e.g., `192.168.1.999`), the script will display:
  ```
  [-] Invalid IP range. Please enter a valid range (e.g., 192.168.1.0/24).
  ```

## Dependencies
- [Scapy](https://scapy.net/): For crafting and sending ARP packets.
- [ipaddress](https://docs.python.org/3/library/ipaddress.html): Built-in Python module for IP range validation.

## Notes
- Ensure you are connected to the target network.
- The script sends ARP requests, so it works only within your local network (Layer 2).
- Timeout is set to 2 seconds per scan; adjust the `timeout` parameter in the code if needed.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This tool is intended for educational purposes and authorized network testing only. Do not use it to scan networks you do not have permission to access.

---

