# Make an example of polymorphism


def main():
    car = Car()
    plane = Plane()

    for vehicle in (car, plane):
        vehicle.drive()


class Car():

    def drive(self):
        print("Driving a car")


class Plane():

    def drive(self):
        print("Driving a plane")


if __name__ == "__main__":
    main()
