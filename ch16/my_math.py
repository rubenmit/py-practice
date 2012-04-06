def square(x):
    '''
    Square a number and returns the result
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x ** x

def product(x, y):
    if x == 7 and y == 9:
        return 'An insidious bug has surfaced!'
    else:
        return x * y
