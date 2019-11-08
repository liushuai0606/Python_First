import paramiko
import time


def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    chan = ssh.invoke_shell()
    time.sleep(1)
    x = chan.recv(2048).decode()
    if enable and '>' in x:
        chan.send('enable'.encode())
        chan.send(b'\n')
        chan.send(enable.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
    elif not enable and '>' in x:
        print('需要配置enable密码！')
        return
    for cmd in cmd_list:
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        x = chan.recv(4096).decode()
        if verbose:
            print(x)
    chan.close()
    ssh.close()


if __name__ == '__main__':
    qytang_multicmd('192.168.32.100', 'admin', 'cisco',
                    ['terminal length 0',
                    #'show ver',
                     'config ter', 'router ospf 1',
                    'network 192.168.32.0 0.0.0.255 area 0'],
                    enable='cisco',
                    wait_time=1, verbose=True)