import random
import os
import time
import datetime


numbers_to_guess = [random.randint(0, 255) for num in range(10)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(.5)


# Prompts the player to choose whether they want to be timed or not
# Also prompts the player to select the number of bits they want to
# attempt to guess
def bits_time():

    time_message = ("Timed games have 10 questions.\n"
                    "Would you like to play a timed game?"
                    "[Yes/No] ")

    bits_message = ("Enter the number of "
                   "bits you would like to guess.\n"
                   "The number must be a multiple of 2.\n"
                   "If you leave this box blank, "
                   "the game will default to 8 bits.\n"
                   "The minimum and maximum selectable "
                   "numbers are 2 and 64. ")

    while True:
        try:
            time = input(time_message).lower()

            clear_screen()
            if time == "y" or time == "yes":
                time = True
                break
            elif time == "n" or time == "no":
                time = False
                break
            else:
                clear_screen()
                raise ValueError('Please type "Yes" or "No".')
        except ValueError as error:
            print(error)

    while True:
        try:
            bits = int(input(bits_message))

        except ValueError:
            num_message = ("You must select a number between 2 and 64! ")
            clear_screen()
            continue
        else:
            clear_screen()
            if bits % 2 == 0 and bits < 66 and bits > 0:
                return bits, time
            else:
                print("You must select a number between 2 and 64! ")


# This is the game mode for guessing binary numbers: 01010101
def binary_mode(bits, time):
    if time == True:
        pass
    else:
        pass

    

def hex_mode(bits, time):
    pass

# Starts the game and prompts user to select a mode.
def start_game():

    clear_screen()

    welcome_message = "Welcome to the Binary/Hexadecimal Speed Testing Game!"

    print(welcome_message)

    input('Press "Enter" to continue!')

    clear_screen()
    while True:
        try:
            game_mode = input("Would you like to play in [b]inary or [h]ex mode? ").lower()
            
            clear_screen()
            
            if game_mode == "binary" or game_mode == "b":
                binary_mode(*bits_time())
                break
            
            elif game_mode == "hex" or game_mode == "h":
                hex_mode(*bits_time())
                break

            else:
                raise ValueError('Please type in "hex" or "binary".')
        except ValueError as err:
            print(err)
    
    

    

start_game()



# Have a timer increment time

# Have a score board and a high score option available

# Save a record to a .json file of the high score (sorted by hex and binary)

# Have a reverse mode for inputting base 10 numbers to guess binary / hex numbers

# consider incorporating ASCII codes as well
