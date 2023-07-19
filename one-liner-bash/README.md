## Network Scanning on local network

```bash
nmap -sn -n $(ip -o -f inet addr show | grep -E "\b(10\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|172\.(1[6-9]|2[0-9]|3[0-1])|192\.168)\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2}\b" -o) | awk '/Nmap scan report for/{print $NF }'
```

- nmap: The command initiates Nmap, a versatile and widely used network scanning utility.
- -sn: This option triggers a "ping scan," during which Nmap only checks if target hosts are online by sending ICMP echo requests (pings), rather than conducting a full port scan.
- -n: To expedite the scan, the option disables DNS resolution, avoiding unnecessary DNS lookups for IP addresses.
- $(ip -o -f inet addr show | grep -E "..." -o): This part of the command employs shell command substitution. It retrieves the IPv4 address information of the network interfaces, filters out private IP addresses within the ranges 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 using grep, and then returns the matching IP addresses.
- awk '/Nmap scan report for/{print $NF }': The awk command processes the output text line by line. It searches for lines containing "Nmap scan report for" and prints the last field (target IP address) of each matching line.
