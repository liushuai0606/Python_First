import re

str1 = 'Port-channel1.189     192.168.189.254  YES     CONFIG   UP'

result = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)',str1).groups()

print('-'*80)
print('%-7s : %s' % ('接口',  result[0]))
print('%-7s : %s' % ('IP地址', result[1]))
print('%-7s : %s' % ('状态', result[5]))

#方法2
import re

str2 = 'Port-channel1.189     192.168.189.254  YES     CONFIG   UP  DOWN'

result2 = re.match(r'(\w\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+(UP|DOWN)\s+\w+',
                   str2.strip()).groups()

result_format = '{0:<10}:{1:<30}'

print('-'*80)
print(result_format.format('接口2', result2[0]))
print(result_format.format('IP地址2', result2[1]))
print(result_format.format('状态2', result2[2]))