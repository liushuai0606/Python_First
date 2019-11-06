import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=3, verbose=False)
    #ping_result.show()
    if ping_result:
        return ip, True
    # else:
    #     return ip, False


if __name__ == '__main__':
    print(qytang_ping('192.168.32.100'))
    # ping_kong = qytang_ping('192.168.1.105')
    # if ping_kong[1]:
    #     print(f'Ping测试： {ping_kong[0]}      结果：通过！')
    # else:
    #     print(f'Ping测试： {ping_kong[0]}      结果：不通过！')
