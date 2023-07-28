from random import randrange
# from More_Copypasta import all_characters

print("Welcome to Meow Cat's Password Generator. Please fill in the following fields.")

number = int(input("How many passwords would you like to generate? "))
length = int(input("How long would you like each password to be? "))

print("Here are your passwords: ")

for password in range(number):
    generated_password = ""
    for character in range(length):
        # generated_password += random.choice(all_characters)
        generated_password += chr(randrange(33,127,1))
    print(generated_password)