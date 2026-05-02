class Car:
    def __init__(self):
        self.engine_on = False

    def start(self):
        self.engine_on = True
        print("Car started")

    def stop(self):
        self.engine_on = False
        print("Car stopped")

# Using abstraction
my_car = Car()
my_car.start()   # You don't need to know how engine works internally
