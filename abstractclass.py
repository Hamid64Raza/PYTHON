from abc import ABC, abstractmethod
class Car(ABC):
    def show(self):
        print("Every car has 4 wheels")
    @abstractmethod
    def speed(self):
            pass
class Maruti(Car):
    def speed(self):
        print("Speed is 100 km/h")
class Suzuki(Car):
    def speed(self):
        print("speed is 70km/h")
ob=Maruti()
ob.show()
ob.speed()

ob1=Suzuki()
ob1.show()
ob1.speed()
