import os
import re
import time

while True:
    try:
        netstat_result = os.popen('netstat -tulnp').read()
        finded_tcp80 = False
        for netstat in netstat_result.split('\n')[2:-1]:
            re_result = re.match(r'tcp\s+\d+\s+\d+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:80\s+'
                                 r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\*\s+LISTEN\s+\d+/.*', netstat)
            if re_result:
                print('HTTP（TCP/80）服务已被打开')
                finded_tcp80 = True
                break
        if finded_tcp80:
            break
        print('等待一秒后重新开始监控！')
        time.sleep(1)
    except KeyboardInterrupt:
        print('接受到管理员的ctrl+cl')
        print('退出程序')
        break
