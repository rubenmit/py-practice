__metaclass__ = type

class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0

	def setSize(self, size):
		self.width, self.height = size

	def getSize(self):
		return self.width, self.height

	size = property(getSize, setSize)

r = Rectangle()
r.width = 0
r.height = 5
print r.size # 0 5

r.size = 150, 100
print r.size # 150, 100
