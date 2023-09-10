class A:
    num1=int(input("Enter 1st Number"))
    num2=int(input("Enter 2nd number"))
    def add(self):
        print("Addition=",self.num1+self.num2)
    def sub(self):
        print("Subtraction=",self.num1-self.num2)
class B(A):
    def mul(self):
        print("Multiplication=",self.num1*self.num2)
    def div(self):
        print("Dev=",self.num1/self.num2)
obj=B()
obj.add()
obj.sub()
obj.mul()
obj.div()
