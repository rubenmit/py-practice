# for
words = ['this', 'is', 'an', 'parrot']
for word in words:
	print word

for number in xrange(1, 10):
	print number

# key..
# dict is un-ordered...
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
	print key, 'corresponds to', d[key]

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in xrange(len(names)):
	print names[i], 'is', ages[i], 'year old'

print '-' * 60

# built-in function: zip() 
for name, age in zip(names, ages):
	print name, 'is', age, 'year old'

print zip(xrange(5), xrange(100))

# built-in function: enumerate()
x = [1, 2, 3, 4, 5]
for index, number in enumerate(x):
	if 2 == number:
		x[index] = 100
print x

print '-' * 60

for number in xrange(10, 0, -3):
	print number
