class Car:
    def __init__(self, make, model, year, color):
        # Instance Variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.bRunning = False

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
        return f"[{self.make}, {self.model}, {self.year}, {self.color}]"




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

    print(car1)
    print(str(car1))
    print(car1.__str__())       # str(car1)  --> car1.__str__()
    print(car1.__repr__())      # repr(car1)  --> car1.__repr__()



if __name__ == "__main__":
    Test1()