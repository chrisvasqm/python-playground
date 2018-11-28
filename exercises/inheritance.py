# Showcase an example of how
# inheritance works.


def main():
    william = Person("William", "Shakespear")
    print(f"Romeo and Juliet was written by {william.firstname} {william.lastname}")

    carlos = Employee("Carlos", "Sanchez", 10000)
    print(f"My best friend {carlos.firstname} got a really nice job earning {carlos.salary} per month!")

    print(isinstance(william, Person))
    print(isinstance(carlos, Person))
    print(isinstance(william, Employee))
    print(isinstance(carlos, Employee))


class Person():

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Employee(Person):

    def __init__(self, firstname, lastname, salary):
        self.salary = salary
        super().__init__(firstname, lastname)


if __name__ == "__main__":
    main()
