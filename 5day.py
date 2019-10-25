import os
route_n_result = os.popen('ipconfig/all').read()

print(route_n_result)