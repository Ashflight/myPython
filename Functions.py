def say_hello(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old.")

def say_hello1(age, name="world"):
    print("Hello " + name + ", you are " + str(age) + " years old.")

print(1)
say_hello("Meow Cat", 14)
print(2)
say_hello("Sidera", 17)

print(say_hello1(5))

print(say_hello(age=2, name="test"))

print(say_hello(age=2))