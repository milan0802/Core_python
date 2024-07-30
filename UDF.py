def oddeven(n):
    if n%2 == 0:
        print(n,"is an even number.")
    else:
        print(n,"is an odd number.")

print("------------------------------------------------------")
def max(a,b):
    if a>b:
        print(a,"is max number:")
    else:
        print(b,"is max number:")

print("------------------------------------------------------")
def maxof3(a,b,c):
    if a>c and a>b:
        print(a,"is max number:")
    elif b>a and b>c:
        print(b,"is max number:")
    else:
        print(c,"is max number:")
print("------------------------------------------------------")
def Fibonacci(n):
  a,b=0,1
  print(a,end="")
  while b<n:
    print(b,end=" ")
    a,b=b,a+b
print("------------------------------------------------------")
def prime(n):
    if n%2!==0:
        for i in range(3,(int(n/2)+1),2):
            if n%i==0:
                print(n,"Is not prime number.")
        else:
          print(n,"Is prime number.")




