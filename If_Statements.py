is_male = eval(input("Enter True if the user is male, and False if not: "))
is_fem= eval(input("Enter True if the user is female, and False if not: "))

if is_male or is_fem:
    print("Your are male or female.")
else:
    print("You are nonbinary.")

if is_male and is_fem:
    print("You are bigender.")
elif is_male and not(is_fem):
    print("You are male.")
elif is_fem and not(is_male):
    print("You are female.")
else:
     print("You are agender.")


a = 5
aBoolean = a > 5
if aBoolean:
    print("a>5")
else:
    print("a<=5")

# b="xyz"
# b=""
b = None
if b:
    print("b is not empty")
else:
    print("b is empty")

aList = ["a'"]
# aList = []
aList = None
if aList :
    print("a is not empty")
else:
    print("a is empty")