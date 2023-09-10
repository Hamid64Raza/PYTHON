class Father:
    name="ansari"
class Son(Father):
    def show(self):
        print("name= Hashim",self.name)
class Gson(Son):
    def disp(self):
        print("name= Hamid",self.name)
ob=Gson()
ob.show()
ob.disp()
