# Count the numbers from 1 to 30,
# when the current number is divisible by 3, print "Fizz"
# when the current number is divisible by 5, print "Buzz"
# and when the current number is divisible by both 3 and 5, print "FizzBuzz"
# otherwise, print the number as is.

def main():
    for number in range(1, 16):
        if isFizzBuzz(number):
            print("FizzBuzz")
        elif isFizz(number):
            print("Fizz")
        elif isBuzz(number):
            print("Buzz")
        else:
            print(number)


def isFizzBuzz(number):
    return number % 15 == 0


def isFizz(number):
    return number % 3 == 0


def isBuzz(number):
    return number % 5 == 0


if __name__ == "__main__":
    main()
