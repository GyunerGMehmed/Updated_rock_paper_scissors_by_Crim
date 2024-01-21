import random

print("Welcome to Rock Paper Scissors game!")
choices = ["rock", "paper", "scissors"]


# Making an input for the player move
def get_player_choice():
    player_move = input("Choose: Rock, Paper, Scissors: ").lower()
    if player_move in choices:
        return player_move
    else:
        # If the input is invalid exit the game and print the error message
        raise SystemExit("Invalid input. Try again with the choice available.[\'r', \'p', \'s']")


# Computer random choice generator
def get_computer_choice():
    """Getting a random choice from a PC perspective."""
    computer_move = random.choice(choices)
    # print(computer_move)
    return computer_move


def deciding_the_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return f"You chose: {player_choice.upper()}, Computer chose: {computer_choice.upper()}. \nYou win. It's a draw."
    elif player_choice == "Rock" and computer_choice == "Scissors" or \
            player_choice == "Scissors" and computer_choice == "Paper" or \
            player_choice == "Paper" and computer_choice == "Rock":
        return f"You chose: {player_choice.upper()}, Computer chose: {computer_choice.upper()}. \nYou win."
    else:
        return f"You chose: {player_choice.upper()}, Computer chose: {computer_choice.upper()}. \nYou lose!"


def playing_the_game():
    player = get_player_choice()
    computer = get_computer_choice()

    result = deciding_the_winner(player, computer)
    print(result)


playing_the_game()
