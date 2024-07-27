a=[1,2.3,3.5,"Milan",True,"python",False]

print(a)

a.append(100)
print(a)

a.clear()
print(a)

a1=a.copy()
print(a)

a1.append(200)
print(a)
print(a1)

a2=a
print(a2)

a2.append(300)
print(a2)
print(a)

a3=[100,200,300]
a.extend(a3)
print(a)

a.pop()
print(a)


