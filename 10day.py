from 8day_3 import 8day_3
from 9day import 9day
import re
import pprint

def qytang_get_if(*ips, username='admin', password='Cisc0123'):
    device_if_dict = {}
    for ip in ips:
        if dict = {}
        if 8day_3(ip):
            for line in 9day(ip,username,password,'show ip int brie').split('\n')
            pint(line)
        device_if_dict[ip]

    return device_if_dict

if __name__ == '__main__':
    pprint.pprint(qytang_get_if('192.168.1.1','192.168.1.2',username='admin',password='Cisc0123'),indent=4)

