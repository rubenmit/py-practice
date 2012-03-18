def add(x, y):
	return x + y

def hello_3(greeting = 'hello', name = 'world'):
	print '%s, %s!' % (greeting, name)

params = (1, 2)
print add(*params)

params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)
