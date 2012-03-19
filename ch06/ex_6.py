x = 1
def change_global():
	global x
	x += 1

change_global()
print x # 2
