lst = [1, 2, 3]
lst.append(4)
print lst

print ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x.count(1) # 2
print x.count([1, 2]) # 1

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b) # more efficient than a + b, and equal to a[len(a):] = b 
print a

# index
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'in']
print knights.index('who')
# print knights.index('wh') # call a exception

# insert
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four') # [1, 2, 3, 'four', 5, 6, 7] 
# or numbers[3:3] = ['four']
print numbers

# pop
x = [1, 2, 3]
x.pop() # del the last element and return the element
print x # [1, 2]
x.pop(0)
print x # [2]

# remove
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be') # same as `del x[1]`
print x

# reverse
x = [1, 2, 3]
x.reverse()
print x # [3, 2, 1]

# sort
x = [4, 6, 2, 1, 7, 9]
x.sort()
# y = x.sort() # don't do this
print x

x = [4, 6, 2, 1, 7, 9]
y = x
y.sort()
print x # [1, 2, 4, 6, 7, 9]
print y # [1, 2, 4, 6, 7, 9]

# sorted function
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print x # [4, 6, 2, 1, 7, 9]
print y # [1, 2, 4, 6, 7, 9]
# sorted make efficient on any sequence (or any iterable object), 
# but return a list always

# cmp, key, reverse on sorted() function
