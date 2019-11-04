import paramiko
import re

def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode()

def ssh_get_route(ip, username, password):
    route_result = qytang_ssh(ip, username, password, cmd='route -n')
    for route in route_result.split('\n')[2:-1]:
        re_route = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                            r'(\w+)\s+\d+\s+\d+\s+\d+ \w+',
                            route.strip())

        if re_route:
            if re_route.group()[1] == 'UG':
                return re_route.groups()[0]

if __name__ == '__main__':
    # print(qytang_ssh('192.168.1.110', 'root', 'Kd2@@456', cmd='pwd'))
    print('网关为：')
    print(ssh_get_route('192.168.1.110', 'root', 'Kd2@@456'))
