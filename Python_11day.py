from Python_9day import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='cisco'):
    try:
        device_config_raw = qytang_ssh(ip, username, password,'show run')
        print(device_config_raw)
    except Exception:
        return


def qytang_check_diff(ip, username='admin', password='cisco'):
    pass

if __name__ == "__main__":
    print(qytang_get_config('192.168.32.100' username='admin', password='cisco'))