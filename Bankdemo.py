class Bank:
    def OpenAccount(self,acno,cname,balance):
        print("Hello",cname,"Your Account Number",acno,"Is Open with ",balance,"Rs.")
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
         self.balance-=amount
        else:
         print("Insufficient balance")
    def checkbalance(self):
        print("current balance",self.checkbalance)
       while True:
          print("*"*30)
          print("1.Deposit")
          print("2.Withdraw")
          print("3.check balance")
          print("4.Exit")
          print("*" * 30)

          choice=int(input("Enter your choice:"))
     if choice==1:
         amount=float(input("Enter Deposit amount:"))
         b1.deposit(amount)
    elif choice==2:
        amount=int(input("Enter withdraw amount :")
        b1.withdraw(amount)
        print("*" * 30)
    elif choice==3
        b1.checkbalance()
        print("*" * 30)
    elif chpice==4
        print("Thank you for using our services.")
        print("*" * 30)
        break:
    else:
        print("Invalid choice. please Try Again.")
            
b1=Bank()
b1.OpenAccount("001","Milan",20000)
