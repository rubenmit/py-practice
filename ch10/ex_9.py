# Double-ended queue
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)

print q 
print list(q)

q.pop()
q.popleft()

print q
q.rotate(1)
q.rotate(-1)
print q
