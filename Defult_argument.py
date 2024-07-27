def test(a,b,c,d):
    print("A:",a,"B:",b,"C:",c,"D:",d)
test(1,2,3,4)

def test(a=14,b=34,c=32,d=12):
    print("A:",a,"B:",b,"C:",c,"D:",d)
test()

def test(a=14,b=34,c=32,d=12):
    print("A:",a,"B:",b,"C:",c,"D:",d)
test(a=100,d=200)

#Arbitry argument
def test(a,b,c,*d):
    print("A:",a,"B:",b,"C:",c,"D:",d)
test(1,2,3,4)

def test(a,b,c,*d):
    print("A:",a,"B:",b,"C:",c,"D:",d)
test(1,2,3,4,5,2,6,8,6)

def test(a,b,c,*d,**e):
    print("A:",a,"B:",b,"C:",c,"D:",d,"E:",e)
test(1,2,3,4,5,2,6,8,6,x=20,y=30,z=50)





