from scapy.all import *

def ack(ip,port):
    ans=sr1(IP(dst=ip)/TCP(dport=int(port),flags="A"),timeout=10)
    print(type(ans))
    if(ans.getlayer(TCP).flags==0x4):
        print("no guolv")
    else:
        print("safe")