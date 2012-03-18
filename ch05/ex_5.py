# while
x = 1
while x <= 100:
	print x
	x += 1

name = ''
while not name:
	name = raw_input('Please enter your name: ')
print 'Hello, %s' % name
