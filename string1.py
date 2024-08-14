s=input("Enter string :")

al=0
nm=0
sp=0
uc=0
lc=0

for i in s:                                                
    if i.isalpha():
        al=al+1                        
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    if i.isupper():
        up=up+1
    elif i.islower():
        lc=lc+1

print("total alphabats :",al)
print("total numeric :",nm)
print("total space :",sp)
print("total upparcase :",uc)
print("total lowercase :",lc)
        
