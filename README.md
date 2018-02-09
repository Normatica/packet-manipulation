# packet-manipulation
playing with some poc for a future project, don't mind me :)

For playing with packets on port 8000
```bash
sudo iptables -t nat -A PREROUTING -p tcp -i INPUT --dport 8000 -j NFQUEUE --queue-num 1
```
