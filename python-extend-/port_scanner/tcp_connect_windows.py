from scapy.all import *

def win(ip,port):
    ans=sr1(IP(dst=ip)/TCP(dport=int(port),flags="A"),timeout=10,verbose=False)
    #print(type(ans))
    if((ans.getlayer(TCP).window)!=0):
        print("Open%s"%port)
    else:
        print("cloesd")