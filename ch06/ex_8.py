map(str, range(10)) # equivalent to [str(i) for i in range(10)]

def func(x):
	return x.isalnum()

seq = ["foo", "x41", "?!", "***"]
filter(func, seq) # ["foo", "x41"]

# or
[x for x in seq if x.isalnum()]

# lambda
filter(lambda x: x.isalnum(), seq)
