import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

from kamene.all import *
ip = []
def qytang_ping(ip):
    ping = IP(dst=ip) / ICMP()
    ping_result = sr1(ping, timeout=3, verbose=False)
    #ping_result.show()
    if ping_result:
        return ip, True
    else:
        return ip, False


if __name__ == '__main__':
    ping_kong = qytang_ping('192.168.1.1')
    if ping_kong[1]:
        print(f'Ping测试： {ping_kong[0]}      结果：通过！')
    else:
        print(f'Ping测试： {ping_kong[0]}      结果：不通过！')
