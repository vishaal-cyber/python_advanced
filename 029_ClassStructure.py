import random


class Car:
    # This space is NOT a 'scope'
    iCount = 0      # Class Attribute/Variable
    # print("Hello")    # <-- Only for demonstration of concept; Bad design

    def __init__(self, make, model, year, color):
        # Instance Attributes/Variables
        self.__make__ = make
        self.model = model
        self.__year__ = year
        self.__color = color
        self.chasis = self.getSerial()
        self.bRunning = False

        # global iCount  # <-- Required when the iCount was in the global scope
        # Car.iCount += 1
        # print(f"{Car.iCount = }")
        self.__class__.iCount += 1

    @property
    def Make(self):
        return self.__make__

    # def SetMake(self, value):
    #     self.__make__ = value

    @property
    def Year(self):
        return self.__year__

    @Year.setter
    def Year(self, value):
        self.__year__ = value

    def Start(self):
        if self.bRunning is not True:
            print(f"{self.__color} {self.__make__} is starting up")
            self.bRunning = True
        else:
            print(f"{self.__color} {self.__make__} is ALREADY running!")

    def Stop(self):
        if self.bRunning is True:
            print(f"{self.__color} {self.__make__} is winding down")
            self.bRunning = False
        else:
            print(f"{self.__color} {self.__make__} is ALREADY stopped!")

    def __str__(self):
        # return f"[{self.make}, {self.model}, {self.year}, {self.color}  of {Car.iCount} cars]"
        # print(Car.iCount)
        # print(self.iCount)  # --> print(self.__class__.__dict__['iCount'])
        return f"{self.__make__}, {self.model}, {self.__year__}, {self.__color}  of {self.iCount} cars"
    
    def __repr__(self):
        return f"[[Chasis: {self.chasis}]] - " + self.__str__()

    # Class  Method
    @classmethod
    def GetCarCount(cls):
        # return Car.iCount
        # return self.iCount
        # return self.__class__.__dict__['iCount']
        # print(f"{type(cls) = }, {cls = }")
        return cls.iCount

    # def GetCarCount(self):
    #     return self.__class__.iCount

    @staticmethod
    def getSerial():
        return random.randint(0, 100000)

    @staticmethod
    def about():
        # Fixed Content
        print("This is a type of a Car object.")


#------------------------------------

class GearedCar(Car):
    iCount = 0      # Class Attribute/Variable

    def __init__(self, make, model, year, color, gears):
        super().__init__(make, model, year, color)
        self.gears = gears
        # GearedCar.iCount += 1

    def __str__(self):
        print(f"{self.iCount = }")
        return f"{self.gears}-geared, " + super().__str__()

    # def GetCarCount(self):
    #     # return GearedCar.iCount
    #     return self.iCount


############################################


def Test1():
    print(Car.GetCarCount())
    car1 = Car("Toyota", "Camry", 2024, "Yellow")
    car2 = Car("Honda", "Accord", 2025, "White")
    car2.__color = "Purple"
    car2._Car__color = "Red"
    print(f"{dir(car2) = }")
    print(car2.__color)

    car1.Start()
    car1.Start()
    car2.Start()

    car2.Stop()

    car1.Stop()
    car1.Stop()

    # global iCount
    # print(iCount)
    # iCount += 10    # iCount = iCount + 10;   L-value & R-value are both required, leading to ambiguity.
    # iCount = 10                 # R-value requirement; Will search the local scope for existing ref; If not found, creates, else replaces
    # print("-->", iCount)        # L-Value requirement; Triggers LEGB search; Resolves to the global iCount
    print(car1)
    print(str(car1))
    print(car1.__str__())       # str(car1)  --> car1.__str__()
    print(car1.__repr__())      # repr(car1)  --> car1.__repr__()

    car3 = Car("Toyota", "Corolla", 2021, "Blue")

    print(car1)
    print(f"{car2 = }")
    print(car3)
    print("No. of Cars -->", car2.GetCarCount())

def Test2():
    car1 = GearedCar("Toyota", "Camry", 2024, "Yellow", 5)
    car2 = GearedCar("Honda", "Accord", 2025, "White", 6)
    # car2.iCount
    car2.__color = "Black"
    print(car1)
    print(car2)
    print("No. of Cars -->", car2.GetCarCount())
    print(repr(car1))
    print(repr(car2))
    car2.about()

def Test3():
    car1 = Car("Toyota", "Camry", 2024, "Yellow")
    car2 = Car("Honda", "Accord", 2025, "White")

    # print(car1.GetMake())
    # print(car1.GetYear())
    # car1.SetYear(2000)
    # print(car1.GetYear())

    print(car1.Make)
    # car1.Make = "Hyundai"
    print(car1.Year)
    car1.Year = 2000
    print(car1.Year)



if __name__ == "__main__":
    # Test1()
    # Test2()
    # print(f"{Car.GetCarCount() = }")
    # print(f"{GearedCar.GetCarCount() = }")
    Test3()

    