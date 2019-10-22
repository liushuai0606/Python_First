import re

str1 = 'Port-channel1.189     192.168.189.254  YES     CONFIG   UP'

result = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)',str1).groups()

print('-'*80)
print('%-7s : %s' % ('接口',  result[0]))
print('%-7s : %s' % ('IP地址', result[1]))
print('%-7s : %s' % ('状态', result[5]))