from scapy.sendrecv import sr
from scapy.layers.inet import IP, TCP
from tcp_connect import three
from tcp_connect_syn import syn
from tcp_connect_ack import ack
from tcp_connect_FIN import fin
from tcp_connect_null import null
from tcp_connect_Xmas import xmas
from tcp_connect_windows import win
from udp_connect import udp
import optparse

t_method=["connect_three","connect_syn","connect_ack","connect_fin","connect_null","connect_xmas","connect_win","connect_udp"]

def PortScan(host,ports,method):
    global t_method
    if(method==t_method[0]):
        for port in ports:
            three(host,port)
    elif(method==t_method[1]):
        for port in ports:
            syn(host,port)
    elif(method==t_method[2]):
        for port in ports:
            ack(host,port)
    elif(method==t_method[3]):
        for port in ports:
            fin(host,port)
    elif(method==t_method[4]):
        for port in ports:
            null(host,port)
    elif(method==t_method[5]):
        for port in ports:
            xmas(host,port)
    elif(method==t_method[6]):
        for port in ports:
            win(host,port)
    elif(method==t_method[7]):
        for port in ports:
            udp(host,port)
    else:
        for port in ports:
            three(host,port)
    #print(t_method[k])
    #verbose,buhuixianshijiazaitiao

def main():
    parser=optparse.OptionParser("[*] Usage: python3 test.py -t <target_host> -p <target_port> -m <scan_methd>")
    parser.add_option('-t',dest="target_host",type="string",help="specify target host")
    parser.add_option("-p",dest="target_ports",type="string",help="specify target port[s]")
    parser.add_option("-m",dest="target_method",type="string",help="specify target method")
    (options,args)=parser.parse_args()
    host=options.target_host
    ports=str(options.target_ports).split(",")
    method=options.target_method
    #print(host,ports,type(ports),ports[0],type(ports[0]),method)
    PortScan(host,ports,method)
    
if __name__=="__main__":
    main()