import fileinput

def process(string):
    print 'Process: ', string

# better than f.readlines()
for line in fileinput.input('somefile.txt'):
    process(line)
