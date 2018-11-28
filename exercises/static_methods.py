# Design a class with static methods


def main():
    print(Math.square(2))


class Math():

    @staticmethod
    def square(number):
        return number * number


if __name__ == "__main__":
    main()
