# import somemodule
# from somemodule import somefunction
# from somemodule import somefunction, anotherfunction...
# from somemodule import *
import math as foobar
print foobar.sqrt(4)

from math import sqrt as foobar
print foobar(4)

# sequence unpacking
x, y, z = 1, 2, 3
print x, y, z # 1, 2, 3
x, y = y, x
print x, y, z # 2, 1, 3

values = 1, 2, 3
print values
x, y, z = values
print x, y, z # 1, 2, 3

scoundrel = {'name': 'Robin', 'girlfriend':'Marion'}
key, value = scoundrel.popitem()
print key, value

# following both will throw exception
# x, y, z = 1, 2
# x, y, z = 1, 2, 3, 4
