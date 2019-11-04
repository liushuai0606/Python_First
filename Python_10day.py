from Python_8day_3 import qytang_ping
from Python_9day import qytang_ssh
import re
import pprint

def qytang_get_if(*ips, username='root', password='Kd2@@456'):
    device_if_dict = {}
    for ip in ips:
        print(ip)
        if_dict = {}
        if qytang_ping(ip):
            for line in qytang_ssh(ip, username, password, 'show ip int brie').split('\n'):
                print(line)
        device_if_dict[ip] = if_dict

    return device_if_dict

if __name__ == "__main__":
    pprint.pprint(qytang_get_if('192.168.1.110', '192.168.1.2', username='root', password='Kd2@@456'), indent=4)

