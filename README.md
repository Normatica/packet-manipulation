# packet-manipulation
playing with some poc for a future project, don't mind me :)

For playing with packets outgoing on port 8000
```bash
sudo iptables -A OUTPUT -p tcp --dport 8000 -j NFQUEUE --queue-num 1
```
