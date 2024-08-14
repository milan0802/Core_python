from _collections import deque

a=deque([])
a.append(10)
print(list(a))
a.append(20)
print(list(a))
a.append(30)
print(list(a))
a.append(40)
print(list(a))
a.append(50)
print(list(a))


a.popleft()
print(list(a))
a.popleft()
print(list(a))
a.popleft()
print(list(a))
a.popleft()
print(list(a))
a.popleft()
print(list(a))
    
