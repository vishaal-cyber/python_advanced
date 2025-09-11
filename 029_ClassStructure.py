

class Car:
    # This space is NOT a 'scope'
    iCount = 0      # Class Attribute/Variable

    def __init__(self, make, model, year, color):
        # Instance Attributes/Variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.bRunning = False


        # global iCount  # <-- Required when the iCount was in the global scope
        Car.iCount += 1
        # print(f"{Car.iCount = }")
        
    def Start(self):
        if self.bRunning is not True:
            print(f"{self.color} {self.make} is starting up")
            self.bRunning = True
        else:
            print(f"{self.color} {self.make} is ALREADY running!")

    def Stop(self):
        if self.bRunning is True:
            print(f"{self.color} {self.make} is winding down")
            self.bRunning = False
        else:
            print(f"{self.color} {self.make} is ALREADY stopped!")

    def __str__(self):
        # return f"[{self.make}, {self.model}, {self.year}, {self.color}  of {Car.iCount} cars]"
        # print(Car.iCount)
        # print(self.iCount)  # --> print(self.__class__.__dict__['iCount'])
        return f"{self.make}, {self.model}, {self.year}, {self.color}  of {self.iCount} cars"

    def GetCarCount(self):
        return Car.iCount

#------------------------------------

class GearedCar(Car):
    def __init__(self, make, model, year, color, gears):
        super().__init__(make, model, year, color)
        self.gears = gears

    def __str__(self):
        print(f"{self.iCount = }")
        return f"{self.gears}-geared, " + super().__str__()


############################################


def Test1():
    car1 = Car("Toyota", "Camry", 2024, "Yellow")
    car2 = Car("Honda", "Accord", 2025, "White")

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
    print(car3)
    print("No. of Cars -->", car2.GetCarCount())

def Test2():
    car1 = GearedCar("Toyota", "Camry", 2024, "Yellow", 5)
    car2 = GearedCar("Honda", "Accord", 2025, "White", 6)
    print(car1)
    print(car2)
    print("No. of Cars -->", car2.GetCarCount())



if __name__ == "__main__":
    Test1()
    Test2()
    