'''
1. Simple If

    if condition:
        statement
2. If/Else

    if condition:
        statement
    else:
        statement
3. Nested If

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement
4. Ladder If/else

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
'''
# simpal if


a=int(input("Enter Number : "))

if a>0:
    print("A is Positive Number")

# if/else

a=int(input("Enter Number : "))

if a>0:
    print("A is Positive Number")
else:
    print("A is Negative Number")

# odd/even

a=int(input("Enter A : "))

if a%2==00:
    print("A Is Even Number")
else:
    print("A Is Odd Number")

# Greater Number

a=int(input("Enter Number : "))
b=int(input("Enter Number : "))

if a>b:
    print("A is Greater Number")
else:
    print("B is Greater Number")

# Nested if

a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if a>c:
        print("A is Max Number")
    else:
        print("C Is Max Number")
elif b>c:
    print("B Is Max number")
else:
    print("C Is Max number")

# Ladder if/else

rno=int(input("Enter Roll No : "))
sname=input("Enter Student Name : ")
s1=int(input("Enter Marks Of Subject 1 : "))
s2=int(input("Enter Marks Of Subject 2 : "))
s3=int(input("Enter Marks Of Subject 3 : "))

total=s1+s2+s3
per=total/3

print("Student Roll No : ",rno)
print("Student Name : ",sname)
print("Total : ",total)
print("percentage : ",per)

if per>=80:
    print("Distinction")
elif per>=70:
    print("First Class")
elif per>=60:
    print("Second Class")
elif per>=50:
    print("Third Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")


    
