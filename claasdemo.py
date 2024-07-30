class student:
    def getdata(self,fname,lname):
        print("getData called")
        self.fname=fname
        self.lname=lname
    def putdata(self):
        print("putData called")
        print("First Name:",self.fname)
        print("Last Name:",self.lname)

s1=student()
s2=student()
s1.getdata("Milan","Hirani")
s1.putdata()



