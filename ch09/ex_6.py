class CounterList(list):
	def __init__(self, *args):
		super(CounterList, self).__init__(*args)
		self.counter = 0

	def __getitem__(self, index):
		self.counter += 1
		return super(CounterList, self).__getitem__(index)

cl = CounterList(range(10))
print cl

cl.reverse()
print cl

print cl.counter # 0

print cl[4] + cl[2] # 12

print cl.counter # 2
