# Computer Networks

> 📅 Last Updated: 2026-03-23

---

## 📖 Overview

Computer networks enable communication between devices. Understanding layers (OSI, TCP/IP), protocols (HTTP, DNS, TCP), and how data moves across the internet is fundamental to backend and distributed systems.

> "The internet is a network of networks."

---

## 🏗️ Network Layers (OSI Model)

| Layer | Name | Protocol Example |
|-------|------|------------------|
| 7 | Application | HTTP, DNS, SMTP |
| 6 | Presentation | SSL/TLS, JPEG |
| 5 | Session | NetBIOS |
| 4 | Transport | TCP, UDP |
| 3 | Network | IP, ICMP |
| 2 | Data Link | Ethernet, MAC |
| 1 | Physical | Fiber, WiFi |

> 🧠 Mnemonic: **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

---

## 🔑 Key Protocols

### TCP vs UDP

| Feature | TCP | UDP |
|---------|-----|-----|
| Reliability | ✅ Guaranteed | ❌ Best-effort |
| Connection | ✅ Connection-oriented | ❌ Connectionless |
| Order | ✅ Preserved | ❌ May arrive out of order |
| Speed | Slower | Faster |
| Use Cases | Web, Email, File Transfer | Streaming, Gaming, DNS |

```python
# TCP example (HTTP)
import requests
response = requests.get("https://example.com")  # Reliable, ordered

# UDP example (DNS)
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Fast, unreliable
```

---

### HTTP / HTTPS

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 301 | Moved Permanently |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

**HTTPS** = HTTP over TLS (encrypted)

---

### DNS (Domain Name System)

```
example.com
    ↓
    DNS Resolver
    ↓
    Root Server → TLD Server (.com) → Authoritative Server
    ↓
    Returns: 93.184.216.34 (IP address)
```

---

## 🌐 How the Internet Works

1. **DNS Lookup**: Convert domain → IP address
2. **TCP Handshake**: 3-way handshake (SYN, SYN-ACK, ACK)
3. **TLS Handshake**: Exchange encryption keys (HTTPS)
4. **Data Transfer**: Packets sent via routing
5. **Connection Close**: 4-way handshake (FIN, ACK)

---

## 🔍 Useful Commands

| Command | Purpose |
|---------|---------|
| `ping google.com` | Check connectivity |
| `traceroute google.com` | Trace path to destination |
| `nslookup example.com` | DNS lookup |
| `curl -I https://example.com` | View HTTP headers |
| `netstat -an` | List network connections |
| `telnet example.com 80` | Test port connectivity |

---

## 💻 Code Examples

### Simple HTTP Server (Python)

```python
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
```

### Making HTTP Request

```python
import requests

# GET request
response = requests.get("https://api.github.com/user", params={"since": 135})

# POST request
data = {"key": "value"}
response = requests.post("https://httpbin.org/post", json=data)

# Headers
headers = {"Authorization": "Bearer token"}
response = requests.get("https://api.example.com/data", headers=headers)
```

---

## 🧪 Key Concepts

### Latency vs Throughput

- **Latency**: Time for a packet to travel (e.g., 50ms)
- **Throughput**: Amount of data per second (e.g., 100 Mbps)

### Bandwidth vs Latency

| Low Bandwidth | High Bandwidth |
|---------------|----------------|
| Slow data rate | Fast data rate |

| Low Latency | High Latency |
|-------------|--------------|
| Fast response | Slow response |

### Load Balancer

Distributes traffic across multiple servers:
- Round Robin
- Least Connections
- IP Hash

---

## 🔒 Security

### Common Attacks

| Attack | Description |
|--------|-------------|
| DDoS | Overwhelm server with traffic |
| MITM | Intercept communication |
| XSS | Inject malicious scripts |
| CSRF | Trick user into unwanted action |

### HTTPS & TLS

- Uses SSL/TLS certificates (Let's Encrypt, paid)
- Encrypts data in transit
- Validates server identity

---

## ❓ Questions & Confusions

- [ ] How does TCP guarantee delivery? (ACKs, retransmission)
- [ ] What happens if DNS server goes down? (caching, fallback)

---

## 🔗 Further Reading

- [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/) — Free textbook
- [Mozilla Network Primer](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/How_the_Internet_works)
- [Cloudflare DNS Learning Center](https://www.cloudflare.com/learning/dns/)

---

*[← Systems](../systems/) · [Back to Index](../../README.md)]*
