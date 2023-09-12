class A:
    def show(self):
        print("I am in parent")
class B(A):
                                   #Same typesignature
    def show(self):
        super().show()
        print("I am in child")
ob=B()
ob.show()
        
