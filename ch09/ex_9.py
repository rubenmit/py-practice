class Fibs(object):
	def __init__(self):
		self.a = 0
		self.b = 1

	def next(self):
		self.a, self.b = self.b, self.a + self.b
		return self.a

	def __iter__(self):
		return self

fibs = Fibs()

for f in fibs: # now, fibs is iterable
	if f > 1000:
		print f
		break
