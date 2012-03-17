tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30] # [)
print tag[32:-4]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[3:6]
print numbers[0:1]
print numbers[7:10]
print numbers[-3:-1]
print numbers[-3:0] # [], got empty
print numbers[-3:]
print numbers[:3]
print numbers[:] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print '-' * 60

# step length
print numbers[0:10:1]
print numbers[0:10:2]
print numbers[::4] # [1, 5, 9]
print numbers[8:3:-1] # !!!! [9, 8, 7, 6, 5]
print numbers[10:0:-2]

print '-' * 60

print [1, 2, 3] + [4, 5, 6]
print 'hello ' + 'world'

print '-' * 60

print 'python' * 5
print [42] * 10
