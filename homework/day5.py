import logging
import re

from homework.day4 import mat_bing
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
import paramiko
from kamene.all import *


def ssh_singlecmd(ip, username, password, cmd):
    try:
        ssh = paramiko.SSHClient()  # 创建SSH Client
        ssh.load_system_host_keys()  # 加载系统SSH密钥
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
        ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # SSH连接
        stdin, stdout, stderr = ssh.exec_command(cmd)  # 执行命令
        x = stdout.read().decode()  # 读取回显
        ssh.close()
        return x

    except Exception as e:
        print('%stErrorn %s' % (ip, e))

    def get_netflow_app():
        show_result = ssh_singlecmd('192.168.32.100', 'admin', 'cisco', 'show flow monitor name qytang-monitor cache format table')
        print(show_result)
        app_name_list = []
        app_bytes_list = []
        for line in show_result.strip().split('\n'):
            print(line)
            app_bytes = re.match(r'^((port|layer7) [a-z]+)\s+(\d+)', line)
            if app_bytes:
                app_name_list.append(app_bytes.groups()[0])
                app_bytes_list.append(app_bytes.groups()[2])

        mat_bing(app_bytes_list, app_name_list)

    if __name__ == "__main__":
        get_netflow_app()