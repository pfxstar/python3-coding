
import math

def convert_input_to_int(msg):
    a = ""
    while not a.isdigit():
        a = input(msg)
      
    return int(a)
    

def move(player_name, current_step):
    a = convert_input_to_int(player_name + ", how many steps do you want to jump? ")

    while a > 2 or a < 1:
        print("Sorry, your number must be either 1 or 2. Please input another.")
        a = convert_input_to_int(player_name + ", how many steps do you want to jump? ")
    current_step += a
    print(player_name + " is on " + str(current_step) + ".")
    return current_step

def game():
    current_step = 0
    current_player = "Player A"
    n = convert_input_to_int("Please input the total steps you want to go. (Must be under or equal to 100) ") # int(input("Please input the total steps you want to go. (Must be under or equal to 100) "))
    while n > 100:
        print("Sorry, you number is too big. Please input another.")
        n = convert_input_to_int("Please input the total steps you want to go. (Must be under or equal to 100) ")
    print("""
    The rules are simple.
    - You can move 1 or 2 steps each turn. 
    - After your turn, it passes to the other player. 
    - Whoever reaches the last step is the winner. 
    - The steps you went are continued by your opponent.
    """)

    while current_step < n:
        # Moving the Player
        current_step = move(current_player, current_step)
        # Switching Players
        if current_step < n:
            if current_player == "Player A":
                current_player = "Player B"
            else:
                current_player = "Player A"

        
    print("The winner is " + current_player + ". Congrats! :)")

while True:
    game()
  