import paramiko
import socket


def qytang_ssh(ip, username, password, cmd='ls', port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    except paramiko.ssh_exception.AuthenticationException as e:
        print("Error !  认证失败", e)
        return
    except socket.timeout as e:
        print("Error !  连接超时", e)
        return
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print("Error !  SSH请求被管理列表过滤", e)
        return
    else:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        i = stdout.read().decode()
        if 'Line has invalid autocommand' in i:
            print("Error ! 命令未执行! 请检查用户权限!")
            return
        else:
            return i
if __name__ == "__main__":
    qytang_ssh('192.168.32.100', 'admin', 'cisco', cmd='show run')
