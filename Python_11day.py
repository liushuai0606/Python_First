from Python_9day import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='cisco'):
    try:
        device_config_raw = qytang_ssh(ip, username, password, 'show run')
        split_result = re.split(r'\r\nhostname \S+\r\n', device_config_raw)
        device_config = device_config_raw.replace(split_result[0],  '').strip()
        return device_config
    except Exception:
        return


def qytang_check_diff(ip, username='admin', password='cisco'):
    before_md5 = ''
    while True:
        device_config = qytang_get_config(ip, username, password)
        m = hashlib.md5()
        m.update(device_config.encode())
        md5_value = m.hexdigest()
        print(md5_value)
        if not before_md5:
            before_md5 = md5_value
        elif before_md5 != md5_value:
            print('MD5 value changed')
            break
        time.sleep(5)
    pass


if __name__ == "__main__":
    #print(qytang_get_config('192.168.32.100' username='admin', password='cisco'))
    qytang_check_diff('192.168.32.100', username='admin', password='cisco')