from scapy.all import *

def fin(ip,port):
    ans=sr1(IP(dst=ip)/TCP(dport=int(port),flags="F"),timeout=10)
    if(ans.getlayer(TCP).flags==0x14):
        print("CLosed:%s"%port)
    else:
        if(int(ans.getlayer(ICMP).type)==3):
            print("Filtered:%s"%port)
        else:
            print("Open:%s"%port)