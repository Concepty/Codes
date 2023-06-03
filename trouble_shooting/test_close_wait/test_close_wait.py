"""
CLOSE_WAIT
"""

from http import client
import os
import time
from run_cmd import run_cmd

NETSTAT_CMD = 'netstat -n -q | findstr :5002'


"""
conn = client.HTTPSConnection('docs.python.org')
conn.request('GET', '/3/library/http.client.html')

"""
"""
conn = client.HTTPSConnection('www.python.org')
conn.request('GET', '/ftp/python/3.12.0/python-3.12.0a7-embed-amd64.zip')
"""
conn = client.HTTPConnection('localhost:5000', source_address=('localhost', 5002))
conn.request('GET', '/download')

print('request sent--------------')
run_cmd(NETSTAT_CMD)

res = conn.getresponse()

print('conn.getresponse()--------------')
run_cmd(NETSTAT_CMD)

time.sleep(10000)

#res.read()

#print('res.read()---------------------')
#run_cmd(NETSTAT_CMD)

conn.close()

print('conn.close()---------------------')
run_cmd(NETSTAT_CMD)

time.sleep(10000)