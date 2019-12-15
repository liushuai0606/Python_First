import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清楚报错
from kamene.all import *
from GET_IP_netifaces import get_ip_address  # 获取主机IP地址
from GET_MAC_netifaces import get_mac_address  # 获取主机MAC地址
# from Scapy_IFACE import scapy_iface  # 获取scapy iface的名字
# from GET_IFNAME import get_ifname  # 获取接口唯一ID


def gratuitous_arp(ip_address, ifname='ens37'):
    localmac = get_mac_address(ifname)
    gratuitous_arp_pkt = Ether(src=localmac, dst='ff:ff:ff:ff:ff:ff') / ARP(op=2,
                                                                            hwsrc=localmac,
                                                                            hwdst=localmac,
                                                                            psrc=ip_address,
                                                                            pdst=ip_address)

    sendp(gratuitous_arp_pkt, iface=scapy_iface(ifname), verbose=False)



if __name__ == "__main__":
    gratuitous_arp("192.168.32.100")
