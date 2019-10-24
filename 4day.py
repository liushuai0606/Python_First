import os
import re

#ifconfig_result = os.popen('ifconfig ' + 'ens160').read()
ifconfig_result = 'ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500' \
                  'inet 192.168.1.166 netmask 255.255.255.0 broadcast 172.16.66.255' \
                  ' inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>' \
                  'ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)' \
                 'RX packets 174598769 bytes 1795658527217 (1.6 TiB)' \
                 'RX errors 1 dropped 24662 overruns 0 frame 0' \
                 'TX packets 51706604 bytes 41788673420 (38.9 GiB)' \
                 'TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0'

#正则表达式查找ip,掩码，广播和Mac地址
ipv4_add = re.findall(r'inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
netmask = re.findall(r'netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
broadcast = re.findall(r'broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
mac_addr = re.findall(r'ether\s+([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})',
                      ifconfig_result)[0]

#格式化字符串
format_string = '{0:<10}: {1:<30}'

#打印结果
print('-'*60)
print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_addr', mac_addr))

#产生网关的IP地址
ipv4_list = ipv4_add.split('.')
ipv4_list[3] = '1'
gateway = '.'.join(ipv4_list)

#ping网关

ping_resul  = os.popen('ping '+ gateway).read()

re_ping = re.findall(r'TTL', ping_resul)

if re_ping:
    print('网关可达！')
else:
    print('网关不可达！')
print('-'*60)