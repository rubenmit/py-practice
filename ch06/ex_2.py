def hello(greeting, name = 'ct.Liu'):
	print '%s, %s' % (greeting, name)

def print_params(x, y, z = 3, *pospar, **keypar):
	print x, y, z
	print pospar
	print keypar

hello(greeting = 'hello', name = 'world')
hello(greeting = 'hello')
print_params(1, 2, 3, 5, 6, 7, foo = 1, bar = 2)
