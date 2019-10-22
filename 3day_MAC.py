import re

str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

result = re.match(r'(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(\w\S+\d)',str.strip()).groups()

result_format = '{0:<10}:{1:<30}'

print('-'*80)
print(result_format.format('VLAN ID', result[0]))
print(result_format.format('MAC', result[1]))
print(result_format.format('Type', result[2]))
print(result_format.format('Interface', result[3]))