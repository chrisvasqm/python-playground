def main():
    for number in range(1, 31):
        if isFizzBuzz(number):
            print("FizzBuzz")
        elif isFizz(number):
            print("Fizz")
        elif isBuzz(number):
            print("Buzz")
        else:
            print(number)


def isFizz(number):
    return number % 3 == 0


def isBuzz(number):
    return number % 5 == 0


def isFizzBuzz(number):
    return number % 15 == 0


if __name__ == "__main__":
    main()
