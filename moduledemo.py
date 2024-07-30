import UDF
while True:
    print("*"*30)
    print("1.EvenOdd")
    print("2.Max of two")
    print("3.Max of three")
    print("4.Fibonacci")
    print("5.prime")
    print("6.Exit")
    print("*"*30)

    choice=int(input("Enter your choice: "))
    print("*" * 30)

    if choice==1:
        a=int(input("Enter first number: "))
        UDF.oddeven(a)
        print("*" * 30)
    elif choice==2:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        UDF.max(a,b)
        print("*" * 30)
    elif choice==3:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        c=int(input("Enter third number:"))
        UDF.maxof3(a, b, c)
        print("*" * 30)
    elif choice==4:
        a=int(input("Enter first number:"))
        UDF.Fibonacci(a)
        print("*" * 30)
    elif choice==5:
        a=int(input("Enter first number:"))
        UDF.prime(a)
    elif choice==6:
        break
    else:
        print("Invalid choice. Please try again.")


