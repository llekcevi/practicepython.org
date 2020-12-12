"""Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock"""
def play_game():  
    #variables hold each players move
    player_1 = input(f"{player_name_1}, do you chose rock, paper or scissors? \n ")
    player_2 = input(f"{player_name_2}, do you chose rock, paper or scissors? \n ")

    #comparing strings the players have entered
    if player_1 == player_2:
        print("It's a draw.")
    else:
        while player_1 == "rock":           
            if player_2 == "paper":
                print(f"{player_name_2} wins!")
                break
            elif player_2 == "scissors":
                print(f"{player_name_1} wins!")
                break

        while player_1 == "paper":
            if player_2 == "scissors":
                print(f"{player_name_2} wins!")
                break
            elif player_2 == "rock":
                print(f"{player_name_1} wins!")
                break

        while player_1 == "scissors":
            if player_2 == "rock":
                print(f"{player_name_2} wins!")
                break
            elif player_2 == "paper":
                print(f"{player_name_1} wins!")
                break
    
print("\n ROCK PAPER SCISSORS \n ")

#asks for players names
player_name_1 = input("What is your name, player one? \n")
player_name_2 = input("What is your name, player two? \n")

#boolean for repeating the game
again = True
#game
play_game()
#while loop for repeating the game
while again:
    repeat = input("Do you want to play again? (Type yes or no.) \n")
    if repeat == "no":
        again = False
        print("Game ended.")
    else:
        play_game()







