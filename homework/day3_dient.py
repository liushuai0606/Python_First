import socket
import struct
import hashlib
import pickle

def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        # ---header设计---
        # 2字节 版本 1
        # 2字节 类型 1 为请求 2 为响应（由于是UDP单向流量！所以此次实验只有请求）
        # 4字节 ID号
        # 4字节 长度

        # ---变长数据部分---
        #使用pickle转换数据

        # ---HASH校验---
        #16字节 MD5值
        send_data = pickle.dumps(x)
        header = struct.pack('>HHLL', version, pkt_type, seq_id, len(send_data))
        m = hashlib.md5()
        m.update(header + send_data)

        md5_value = m.digest()

        s.sendto(header + send_data + md5_value, address)

        seq_id += 1
    s.close()

if __name__ =="__main__":
    user_data = ['乾颐堂', [1, 'qytang', 3],  {'qytang': 1, 'test': 3}]
    udp_send_data('192.168.1.110', 6666, user_data)