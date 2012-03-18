# pass

# del
x = 1
del x
# print x # throw exception

# exec: execute a series of statement
exec "print 'hello, world!'"

from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope.keys() # 

# eval: calc the python expression
