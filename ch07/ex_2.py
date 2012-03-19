# equivalent for following two statements
def foo(x): return x * x
foo = lambda x: x * x

class MemberCount:
	members = 0
	def init(self):
		MemberCount.members += 1

m1 = MemberCount()
m1.init()

m2 = MemberCount()
m2.init()

print MemberCount.members # 2

m1.members = 'Two'
print m1.members # 'Two'
print m2.members # 2
