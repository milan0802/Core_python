def prime(n):

    if n%2!=0:
        for i in range(3,(int(n/2)+1),2):
            if n%i==0:
                print(n,"Is not prime number.")
        else:
          print(n,"Is prime number.")

prime(n = int(input("Enter first number:")))