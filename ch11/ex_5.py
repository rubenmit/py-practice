def process(string):
    print 'Processing: ', string

f = open('somefile.txt')
print type(f) # <type 'file'>

# readlines() need large memory
for line in f.readlines():
    process(line)
f.close()
