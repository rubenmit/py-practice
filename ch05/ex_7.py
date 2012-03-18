a = [x * x for x in xrange(10)]
print a

a = [x * x for x in xrange(10) if x % 3 == 0]
print a

a = [(x, y) for x in xrange(3) for y in xrange(3)]
print a

result = []
for x in xrange(3):
	for y in xrange(3):
		result.append((x, y))
