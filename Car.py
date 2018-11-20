class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print("This is a %s %s with %s MPG." % self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        super().__init__(model, color, mpg)
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "Like new"


your_car = Car("DeLorean", "silver", 80)
my_car = ElectricCar("Chevy", "Blue", 120, "molten salt")

print(your_car.model, your_car.color, your_car.mpg, your_car.condition)
print(your_car.drive_car())

print(my_car.model, my_car. color, my_car.mpg, my_car.battery_type, my_car.condition)
print(my_car.drive_car())
