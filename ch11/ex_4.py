def do_something(fobj):
    print fobj.read()

# auto close the file object
with open('somefile.txt') as somefile:
    do_something(somefile)
