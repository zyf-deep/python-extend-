from scapy.all import *

def udp(ip,port):
    ans=sr1(IP(dst=ip)/UDP(dport=int(port)),timeout=10,verbose=False)
    #print(type(ans))
    if(ans.haslayer(UDP)):
        print("Open%s"%port)
    else:
        print("closed")