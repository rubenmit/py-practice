# tuple: sequence that can not changed.
x = (1, 2, 3)
x = (1,) # tuple that only has one element, not (1) !!!

# tuple(), is not function
x = tuple([1, 2, 3])
print x # (1, 2, 3)
x = tuple("abc")
print x # ('a', 'b', 'c')
x = tuple((1, 2, 3))
print x # (1, 2, 3)

# squence: list, str, tuple
