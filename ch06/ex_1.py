def hello(name):
    return 'Hello, ' + name

# we can get detail using square.__doc__
def square(x):
    'Calculate the square of the number x'
    return x * x

def list_change_value(prices):
    prices.append(10)

print hello('world')

x = [2, 3]
# x = (2, 3) # throw exception, because tuple is unable to changed.
list_change_value(x)
print x # [2, 3, 100]
