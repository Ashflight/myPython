print(2**3)
#The default python exponent function is two multiplication signs.
#But we can make one with for loops.
def exponent(base, power):
    result = 1
    # for index in range(power):
    index = 0
    while index < power:
        result = result * base
        index += 1
    return result

print(exponent(3, 4))

print("Welcome to Meow Cat's Exponent Calculator. \nEnter your base and exponent. \nNote: Your exponent must be an integer.")
num1 = float(input("Enter your base: "))
num2 = int(input("Enter your exponent: "))
print(exponent(num1, num2))