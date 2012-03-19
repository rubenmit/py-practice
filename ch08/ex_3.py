try:
	x = input('Enter the first number: ')
	y = input('Enter the second number: ')
	print x / y
except (ZeroDivisionError, TypeError, NameError):
	print 'Your numbers were bogus...'

try:
	x = input('Enter the first number: ')
	y = input('Enter the second number: ')
	print x / y
except: # catch all the exception
	print 'Your numbers were bogus...'
