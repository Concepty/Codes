from test_pkg.test_mod import *
from test_pkg2.test_mod import *

test()
test2()

"""
there is warning in visual studio code because the test function is dynamically added to test_pkg.test_mod.__all__
"""