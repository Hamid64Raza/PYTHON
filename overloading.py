class A:
    def show(self):
        print("No argument")
    def show(self,Firstname=''):
        print("welcome",Firstname)
    def show(self,Firstname='',Lastname=''):
        print("Welcome",Firstname,Lastname)
ob=A()
ob.show()
ob.show("Hamid")
ob.show("Hamid","Raza")
