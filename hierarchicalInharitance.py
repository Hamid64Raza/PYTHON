class Father:
    surname="Ansari"
    def show(self):
        print("My name is= ",self.surname)
class Son1(Father):
    def disp(self):
        print("My name is Hamid ",self.surname)
class Son2(Father):
    def dis(self):
        print("My name is Wahid ",self.surname)
ob1=Son1()
ob1.disp()
ob2=Son2()
ob2.dis()
