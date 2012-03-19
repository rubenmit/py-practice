class Filter:

	def init(self):
		self.blocked = []

	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): # SPAMFilter is the subclass of Filter

	def init(self): # overwrite the init() method
		self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1, 2, 3]) # [1, 2, 3]

s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])

print issubclass(SPAMFilter, Filter) # True
print issubclass(Filter, SPAMFilter) # False

print SPAMFilter.__bases__ # get the base class of cur class
print Filter.__bases__

print isinstance(s, SPAMFilter) # True
print isinstance(s, Filter) # True
print isinstance(s, str) # False

print s.__class__ # get the class of s
