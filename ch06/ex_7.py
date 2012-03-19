def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

def search(sequence, number, lower = 0, upper = None):
	if upper is None:
		upper = len(sequence) - 1

	if lower == upper:
		assert number == sequence[upper]
		return upper
	else:
		middle = (lower + upper) // 2
		if number > sequence[middle]:
			return search(sequence, number, middle + 1, upper)
		else:
			return search(sequence, number, lower, middle)

print factorial(3)

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print seq
print search(seq, 34) # bisect module...
