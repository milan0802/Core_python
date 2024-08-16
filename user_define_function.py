# function with no argument and no return value.

def printline():
    print("*"*50)
printline()
print("user define function in python.")
printline()

# function with argument but no return value.
def add(a,b):
    print("Addition : ",a+b)
    printline()
add(10,20)

# function with argument & with return value.
def sub(a,b):
    return (a-b)
printline()
#ans=sub(10,20)
print("subtraction ; ",sub(10,20))
printline()
