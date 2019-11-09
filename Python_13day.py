import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *


class QYTPING:
    def __init__(self, ip):
        self.ip = ip
        self.length = 100
        self.srcip = ''

    def make_pkt(self):
        if self.srcip:
            self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)
        else:
            self.pkt = IP(dst=self.ip) / ICMP() / (b'v' * self.length)

    def one(self):
        self.make_pkt()
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result:
            print(self.ip, '可达')
        else:
            print(self.ip, '不可达')

    def ping(self):
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()

    def __str__(self):
        if not self.srcip:
            return '<{0} => dstip:{1}, size:{2}>'.format(self.__class__.__name__,self.ip, self.length)
        else:
            return '<{0} => srcip:{1},dstip:{2}, size{3}>'.format(self.__class__.__name__, self.srcip, self.ip, self.length)


class NewPing(QYTPING):
    def ping(self):
        self.make_pkt()
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)
        print()


if __name__ == '__main__':
    ping = QYTPING('192.168.32.100')
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2), word, s * int((70 - len(word))/2)))
    print_new('print class')
    print(ping)  # 打印类
    print_new('ping on for sure reachable')
    ping.one()  # ping一个包判断可达性
    print_new('ping five')
    ping.ping()  # 模拟正常ping程序ping五个包，‘1‘表示通，’.‘表示不通
    print_new('set payload lenth')
    ping.length = 200  # 设置负载长度
    print(ping)  # 打印类
    ping.ping()  # 使用修改长度的包进行ping测试
    print_new('set ping src ip address')
    ping.srcip = '192.168.32.129'  # 修改原IP地址
    print(ping)  # 打印类
    ping.ping()  # 使用修改长度的包进行ping测试
    print_new('new class NewPing', '=')
    newping = NewPing('192.168.32.101')  # 使用新的类Newping通过继承QYTPING类产生
    newping.length = 300
    print(newping)  # 打印类
    newping.ping()  # NewPing类自定义ping（）这个方法，’+'表示通，‘？’表示不通