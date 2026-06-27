from collections import deque

dq = deque()

dq.append(10)
dq.appendleft(5)

print(dq.pop())
print(dq.popleft())
