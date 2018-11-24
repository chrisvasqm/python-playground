# Make a Higher Order Function that takes two parameters
# and a callback function to output a single value based
# on the callback operation.

def calculate(first, second, callback):
    return callback(first, second)

add = calculate(2, 2, lambda first, second: first + second)
print("2 + 2 = " + str(add))

substract = calculate(5, 2, lambda first, second: first - second)
print("5 - 2 = " + str(substract))

multiply = calculate(5, 3, lambda first, second: first * second)
print("5 * 3 = " + str(multiply))