# dictionary

# clear
x = {}
y = x
x['key'] = 'value'
print y
x = {}
print y # {'key': 'value'}

x = {}
y = x
x['key'] = 'value'
print y
x.clear()
print y # {}

print '-' * 60

# copy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mhl'
y['machines'].remove('bar')
print y
print x

# deepcopy
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c
print dc

print '-' * 60

# fromkeys
print {}.fromkeys(['name', 'age'])
print dict.fromkeys(['name', 'age'])
print {}.fromkeys(['name', 'age'], 'None')

# get
d = {}
# print d['name'] # throw exception!!!
print d.get('name') # return None
print d.get('name', 'N/A') # return N/A

# has_key
d = {}
d.has_key('name') # False

# items / iteritems
# iteritems() will more efficient in some condition

# keys / iterkeys

print '-' * 60

# pop
d = {'x': 1, 'y': 2}
d.pop('x') # list also has pop()
print d

# popitem
# {}.popitem() will pop random element

# setdefault
d = {}
d.setdefault('name', 'N/A')
print d # {'name": 'N/A'}
d['name'] = 'Gumby'
d.setdefault('name', 'N/A')
print d # {'name': 'Gumby'}

# update

# values / itervalues
