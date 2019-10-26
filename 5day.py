import os
import re

route_n_result = os.popen('route -n').read()

for route in route_n_result.strip().split('\n')[2:]:
    re_route = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
                        r'(\w+)\s+\d+\s+\d+\s+\d+ \w',
                        route.strip()).groups()

    if re_route[1] == 'UG':
        print('网关为：', re_route[0])
        break
