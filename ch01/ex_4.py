# str
temp = 42
print "The temperature is " + `temp` # bad formation
print "The temperature is " + repr(temp) # repr is a function
print "The temperature is " + str(temp) # str is a type, 
										#same  as int..

print '-' * 50
# long string
print '''This is a very long string.
It continues here.
And not yet over.
"Hello, world!"
Still here.'''

# raw string
print r'C:\nowhere'
print r'Let\'s go' # !!
print r'C:\nowhere\\' # wrong output
print r'C:\nowhere' '\\'

# unicode str
print u'Hello, world!' # in python3.0, all str is unicode str
