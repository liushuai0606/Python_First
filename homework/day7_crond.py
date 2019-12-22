import paramiko
import sqlite3
from Python_9day import qytang_ssh
import hashlib
import re


def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


def get_config_md5(ip, username='admin', password='cisco'):
    try:
        run_config_raw = qytang_ssh(ip, username, password, cmd='show run')
        split_result = re.split(r'\r\nhostname \S+\r\n', run_config_raw)
        device_config = run_config_raw.replace(split_result[0], '').strip()
        m = hashlib.md5()
        m.update(device_config.encode())
        md5_value = m.hexdigest()

        return device_config, md5_value
    except Exception:
        return


#设备清单
device_list = ['192.168.32.100', '192.168.32.101']
#用户名密码
username = 'admin'
password = 'cisco'


def write_config_md5_to_db():
    conn = sqlite3.connect('qytangconfig.sqlite')
    cursor = conn.cursor()
    #逐个迭代设备，写入数据库！
    for device in device_list:
        config_and_md5 = get_config_md5(device, username, password)
        cursor.execute('select * from config_md5 where ip=?', (device, ))
        md5_result = cursor.fetchall()
        if not md5_result:
            #如果设备的数据库条目不存在，就写入
            cursor.execute("insert into config_md5(ip, config, md5) values (?, ?, ?)",(device,
                                                                                       config_and_md5[0],
                                                                                       config_and_md5[1]))
            conn.commit()

        else:
            if config_and_md5[1] != md5_result[0][2]:
                #如果之前备份的MD5值与当前获取的MD5值不匹配！ 就更新条目
                cursor.execute("update config_md5 set config=?, md5=? where ip=?",(config_and_md5[0],
                                                                                    config_and_md5[1],
                                                                                    device))
            else:   #如果之前备份的MD5与当前获取的MD5值匹配！就略过
                continue
    cursor.execute('select * from config_md5')
    all_result = cursor.fetchall()
    for x in all_result:
        print(x[0], x[2])
    conn.close()

if __name__ == '__main__':
    import os
    if os.path.exists('qytangconfig.sqlite'):
        os.remove('qytangconfig.sqlite')

    conn = sqlite3.connect('qytangconfig.sqlite')
    cursor = conn.cursor()

    #执行创建表的任务
    cursor.execute("create table config_md5 (ip varchar(40), config varchar (99999), md5 varchar (1000))")
    conn.close()

    write_config_md5_to_db()
