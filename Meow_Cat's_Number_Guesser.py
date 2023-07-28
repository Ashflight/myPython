from random import randrange
answer = randrange(1,100,1)
guess = None
attempts = 0
limit = 7
end = False

print("Welcome to Meow Cat's Guessing Game. \nTry your best to guess the correct number, which can be anywhere between 0 and 100!")
while guess != answer and not(end):
    if attempts < limit:
        guess = float(input("Enter your guess here: "))
        attempts += 1
        if guess < answer and attempts < limit:
            print("Your guess is too small.")
        elif guess > answer and attempts < limit:
            print("Your guess is too big.")
        # else:
        #     None
    else:
        end = True
if end:
    print("GAME OVER")
else:
    print("You've won!")