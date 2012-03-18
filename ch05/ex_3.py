name = raw_input('What is your name? ')
if name.endswith('Gumby'):
	print 'Hello, Mr. Gumby'
else:
	print 'Hello, stranger'

num = input('Enter a number: ')
if num > 0:
	print 'The number is positive'
elif num < 0:
	print 'The number is nagative'
else:
	print 'The number is zero'

# int(raw_input()) is same as input()

# x is y # x, y is the same object!!!! same, not equal
# x is not y # X, y is different object
# x in y # x is a member of y
# x not in y # x is not a member of y

age = input()
if 0 < age < 100:
	print `age` + ' is between 0 and 100'
