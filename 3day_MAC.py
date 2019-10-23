import re

str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

result = re.match(r'(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(\w\S+\d)',
                  str.strip()).groups()

result_format = '{0:<10}: {1:<30}'

print('-'*80)
print(result_format.format('VLAN ID', result[0]))
print(result_format.format('MAC', result[1]))
print(result_format.format('Type', result[2]))
print(result_format.format('Interface', result[3]))

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result1 = re.match(r'(\w+)\s+server\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})\s+localserver\s+'
                   r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}),\s+idle\s+(\d{1,2}):(\d{1,2}):(\d{1,2}),'
                   r' bytes\s+(\d+),\s+flags\s+(\w+)',str1.strip()).groups()

result_format1 = '{0:<15}: {1:<30}'

print('-'*80)
print(result_format1.format('protoclo', result1[0]))
print(result_format1.format('server', result1[1]))
print(result_format1.format('localserver', result1[2]))
print(result_format1.format('idle', result1[3]))
print(result_format1.format('bytes', result1[4]))
print(result_format1.format('flags', result1[5]))