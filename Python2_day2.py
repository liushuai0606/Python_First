import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  #清楚报错
from kamene.all import *
from Part1_Classic_Protocols.Tools.GET_IP_netifaces import get_ip_address  #获取主机IP地址
from Part1_Classic_Protocols.Tools.GET_MAC_netiface import get_mac_address  #获取主机MAC地址
from Part1_Classic_Protocols.Tools.Scapy_IFACE import scapy_iface  #获取scapy iface的名字
from Part1_Classic_Protocols.Tools.GET_IFNAME import get_ifname  #获取接口唯一ID


def gratuitous_arp(ip_address, ifname = 'ens33'):
    localmac = get_mac_address(ifname)
    gratuitous_arp_pkt = Ether(src=localmac, dst='ff:ff:ff:ff:ff:ff') / ARP(op=2,
                                                                           hwsrc=localmac,
                                                                           hwdst=localmac,
                                                                           psrc=ip_address,
                                                                           pdst=ip_address)

    sendp(gratuitous_arp_pkt, ifaces=scapy_iface(ifname), verbose=false)

if __name__ == "__main__":
    gratuitous_arp("192.168.32.100")
