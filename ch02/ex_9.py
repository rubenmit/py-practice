# list
print list('hello')
print ''.join(list('hello')) # hello, different output from above

x = [1, 1, 1]
x[1] = 2
print x

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2] # delete 'Cecil' element
print names

name = list('Perl')
name[1:] = list('ython')
print name

numbers = [1, 5]
numbers[1:1] = [2, 3, 4] # insert a sequence
print numbers

numbers[1:4] = []
print numbers
