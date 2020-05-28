#This script is the game "guess the number"

player_1 = input("First player, enter your name: ")
player_2 = input("Second player, enter your name: ")
orig_number_2 = int(input(f"{player_1}, enter a number for {player_2}: "))
orig_number_1 = int(input(f"{player_2}, enter a number for {player_1}: "))

player_1_winner = False
player_2_winner = False
number_1 = 0
number_2 = 0

while not(player_1_winner or player_2_winner):
    #player_1 turn
    number_1 = input(f"{player_1}, your turn! Try to quess the number! (enter 'q' for exit): ")
    if number_1 == 'q':
        break
    number_1 = int(number_1)
    if number_1 == orig_number_1:
        player_1_winner = True
        print(f"{player_1}, you guessed!")
    elif orig_number_1 < number_1:
        print(f"{player_1}, original number is less then {number_1}!")
    else:
        print(f"{player_1}, original number is greater then {number_1}!")

    # player_2 turn
    number_2 = input(f"{player_2}, your turn! Try to quess the number! (enter 'q' for exit): ")
    if number_2 == 'q':
        break
    number_2 = int(number_2)
    if number_2 == orig_number_2:
        player_2_winner = True
        print(f"{player_2}, you guessed!")
    elif orig_number_2 < number_2:
        print(f"{player_2}, original number is less then {number_2}!")
    else:
        print(f"{player_2}, original number is greater then {number_2}!")

if player_1_winner and player_2_winner:
    print("Congratulations! Both players guessed!")
elif player_1_winner:
    print(f"Congratulations, {player_1}! You are the winner!")
elif player_2_winner:
    print(f"Congratulations, {player_2}! You are the winner!")
else:
    print("Goodbye!")