from Python_8day_3 import qytang_ping
from Python_9day import qytang_ssh
import re
import pprint


def qytang_get_if(*ips, username='admin', password='cisco'):
    device_if_dict = {}
    for ip in ips:
        if_dict = {}
        if qytang_ping(ip):
            for line in qytang_ssh(ip, username, password, 'show ip int brie').split('\n'):
                print(line)
        device_if_dict[ip] = if_dict

    return device_if_dict


if __name__ == "__main__":
    pprint.pprint(qytang_get_if('192.168.32.100', '192.168.32.101', username='admin', password='cisco'), indent=4)

