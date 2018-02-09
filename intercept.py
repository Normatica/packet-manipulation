#!/usr/bin/python
from scapy.all import *
from netfilterqueue import NetfilterQueue
def modify(packet):
  pkt = IP(packet.get_payload())
  print pkt
  packet.accept()
nfqueue = NetfilterQueue()
nfqueue.bind(1, modify) 
try:
  nfqueue.run()
except KeyboardInterrupt:
  pass
