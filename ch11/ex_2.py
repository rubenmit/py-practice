f = open('somefile.txt', 'r')
data = f.read(4)
print data # Hell
print f.read() # o, World!
f.close()
