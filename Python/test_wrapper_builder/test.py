from test_pkg.test_module import *


try:
    test1()
except:
    print('test1 cannot be called')

try:
    test2()
except:
    print('test2 cannot be called')
