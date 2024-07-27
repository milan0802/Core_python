def oddeven(n):
    if n%2 == 0:
        print(n,"is an even number.")
    else:
        print(n,"is an odd number.")
oddeven(n=int(input("Enter a number: ")))
print("------------------------------------------------------")
def max(a,b):
    if a>b:
        print(a,"is max number:")
    else:
        print(b,"is max number:")
max(20,30)
print("------------------------------------------------------")
def maxof3(a,b,c):
    if a>c and a>b:
        print(a,"is max number:")
    elif b>a and b>c:
        print(b,"is max number:")
    else:
        print(c,"is max number:")
maxof3(10,20,50)

