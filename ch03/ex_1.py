# str in python is a type can not be changed
format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print format % values

format = "Pi with three decimals: %.3f"
from math import pi
print format % pi

# find
'With a moo-moo here, and moo-moo there'.find('moo')
title = "Monty Python's Flying Circus"
print title.find('Monty') # 0
print title.find('Flying') # 15
print title.find('Zirquss') # -1

subject = '$$$ Get rich now!!! $$$'
print subject.find('$$$')
print subject.find('$$$', 1) # st, ed
print subject.find('$$$', 1, 16) # st, ed

# rfind, index, rindex, count, startwith, endswith

# join
seq = ['1', '2', '3', '4', '5']
sep = '+'
print sep.join(seq)

# lower
print 'Trondheim Hammer Dance'.lower()

# replace
print 'This is a test'.replace('is', 'eez')

# split (to sequence)
print '1+2+3+4+5'.split('+')

# strip (delete the whitespace in two end)
print '    internal whitespace is kept     '.strip()

# translate (handle single character)
from string import maketrans
table = maketrans('cs', 'kz') # len(table) = 256
print 'this is an incredible test'.translate(table)
