class Calculator:

	def calculate(self, expression):
		self.value = expression

class Talker:

	def talk(self):
		print 'Hi, my value is', self.value

# the class inherited earlier will overwrite the method appered in
# the class after
class TalkingCalculator(Calculator, Talker):

	pass

tc = TalkingCalculator()
tc.calculate(`1+2*3`)
tc.talk()

print hasattr(tc, 'talk')
print hasattr(tc, 'fnord')

setattr(tc, 'name', 'Mr. Gumby')
print tc.name
