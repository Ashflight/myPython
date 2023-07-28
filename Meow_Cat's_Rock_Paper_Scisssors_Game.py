from random import randrange
game_running = True
computer_score = 0
player_score = 0
while game_running == True:
    computer_choice = randrange(0,3,1)
    player_choice = input("Enter your choice, rock, paper or scissors: ")
    if player_choice.lower() == "rock":
        if computer_choice == 0:
            print("You tied with the computer.")
        elif computer_choice == 1:
            print("You lost.")
            computer_score += 1
        else:
            print("You won! (The computer played scissors.)")
            player_score +=1
    elif player_choice.lower() == "paper":
        if computer_choice == 0:
            print("You won! (The computer played rock.)")
            player_score +=1
        elif computer_choice == 1:
            print("You tied with the computer.")
        else:
            print("You lost.")
            computer_score +=1
    elif player_choice.lower() == "scissors":
        if computer_choice == 0:
            print("You lost.")
            computer_score += 1
        elif computer_choice == 1:
            print("You won! (The computer played paper.)")
            player_score += 1
        else:
            print("You tied with the computer.")
    else:
        print("Invalid input.")
    game_continue = input("If you want to play again, enter \"yes\": ")
    if not game_continue.lower() == "yes":
        break

if player_score > computer_score:
    print("You beat the computer.")
elif player_score < computer_score:
    print("You lost to the computer.")
else:
    print("You tied with the computer.")

print("You: " + str(player_score) + "; Computer: " + str(computer_score) + ".")
