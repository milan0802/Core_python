Rollno=int(input("Enter Rollno:"))
sname=input("Enter Student name:")
s1=int(input("Enter Marks Subject 1:"))
s2=int(input("Enter Marks Subject 2:"))
s3=int(input("Enter Marks Subject 3:"))        

total=s1+s2+s3
per=total/3

print("Rollno:",Rollno)
print("Student Name:",sname)
print("total:",total)
print("parsentege:",per)
       
if per>=70:
   print("destiction")
elif per>=60:
  print("First class")
elif per>=50:
  print("Second class")
elif per>=40:
   print("Pass class")
else:
   print("Fail")
