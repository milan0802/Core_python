import ramdom

print(random.randint(1000,9999))
print(random.choice([1,2,10,20,"tops","python",True,100]))

l=[]
lucku=[]

for i in range(1,100):
    l.append(i)

for i in range(10):
    num=rendom.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)
