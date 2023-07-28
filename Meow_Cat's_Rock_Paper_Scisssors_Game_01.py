from random import randrange

switch_dict = {
    "R": 0,
    "P": 1,
    "S": 2
}

def findDictKey(value_to_find, switch):
    for key, value in switch.items():
        if value == value_to_find:
            return key

def compare(user, computer):
    if user == computer :
        return "tie"
    elif (computer == 2 and user ==0) or (user > computer) :
        return "win"
    else:
        return "lose"

computer_score = 0
player_score = 0
while True:
    computer_choice = randrange(0,3,1)
    player_choice = input("Enter your choice, rock(R), paper(P) or scissors(S) and E to exit: ")
    if player_choice == "E":
        break
    result = compare(switch_dict.get(player_choice), computer_choice)
    if result == "win":
        player_score += 1
    elif result == "lose":
        computer_score += 1
    print("computer choice is " + findDictKey(computer_choice, switch_dict) + " and the result is you " + result)

if player_score > computer_score:
    print("You beat the computer.")
elif player_score < computer_score:
    print("You lost to the computer.")
else:
    print("You tied with the computer.")

print("You: " + str(player_score) + "; Computer: " + str(computer_score) + ".")
