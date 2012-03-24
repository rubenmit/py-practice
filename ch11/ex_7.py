import fileinput

def process(string):
    print 'Process: ', string

# better way, and needn't to close the file by yourself
# iteration
for line in open('somefile.txt'):
    process(line)
