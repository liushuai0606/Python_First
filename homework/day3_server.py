import socket
import struct
import hashlib
import pickle
import sys


address = ("192.168.1.110", 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('UDP服务器就绪！等待客户数据！')
while True:
    try:
        recv_source_data = s.recvfrom(2048)

        rdata, addr = recv_source_data
        header = rdata[:12]
        uppack_header = struct.unpack('>HHLL', header)
        version = uppack_header[0]
        pkt_type = uppack_header[1]
        seq_id = uppack_header[2]
        length = uppack_header[3]

        rdata = rdata[12:]
        data = rdata[:length]
        md5_recv = rdata[length:]

        m = hashlib.md5()
        m.update(header + data)
        md5_value = m.digest()

        if md5_recv == md5_value:
            print('='*80)
            print("{0:<30}:{1:<30}".format("数据来自于", str(addr)))
            print("{0:<30}:{1:<30}".format("数据序列号", seq_id))
            print("{0:<30}:{1:<30}".format("数据长度为", length))
            print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))

    except KeyboardInterrupt:
        sys.exit()