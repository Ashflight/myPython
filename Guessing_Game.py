answer = "giraffe"
guess = ""
attempts = 0
limit = 3
end = False

print("Welcome to Meow Cat's Guessing Game. \n Try your best to guess the secret word!")
while guess != answer and not(end):
    if attempts < limit:
        guess = input("Enter your guess here: ")
        attempts += 1
    else:
        end = True
if end:
    print("GAME OVER")
else:
    print("You've won!")