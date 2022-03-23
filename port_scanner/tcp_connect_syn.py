from scapy.all import *

def syn(ip,port):
    ans=sr1(IP(dst=ip)/TCP(dport=int(port),flags="S"),timeout=10,verbose=False)
    if(ans.getlayer("TCP").flags==0x12):
        print("Open:%s"%port)
    else:
        print("Closed:%s"%port)