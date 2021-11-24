# Make an example of polymorphism


def main():
    vehicles = [Car(), Plane()]

    for vehicle in vehicles:
        vehicle.drive()


class Vehicle(object):
    def drive(self):
        pass

class Car(Vehicle):

    def drive(self):
        print("Driving a car")


class Plane(Vehicle):

    def drive(self):
        print("Driving a plane")


if __name__ == "__main__":
    main()
