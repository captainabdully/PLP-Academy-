#Assignment 2
#Polymophism with the vehicles!!!

#Parent Class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The vehicle is moving.....")


#Child class 1
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road!")


#Child class 2
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky")

#Child class 3
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the indian ocean!")

#Child class 4
class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} is riding at kilimanjaro park")


#List of vehicle objects
vehicles = [
    Car("Mercedez benz"),
    Plane("Boeing 777"),
    Boat("Sea horse"),
    Bicycle("Mountain Bike!"),
]

#Looping the same method(move)
for v in vehicles:
    v.move()