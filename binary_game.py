def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bits_time():
    try:
        time = input("""
Timed games have 10 questions.
Would you like to play a timed game? [Yes/No] )
""").lower()

        if time in "yes":
            time = True
        elif time in "no":
            time = False
        else:
            raise ValueError('Please type "yes" or "no".')
    except ValueError as error:
        print(error)

    try:
        bits = input("""
Enter the number of bits you would like to guess.
The number must be a multiple of 2.
If you leave this box blank, the game will default to 8 bits.
The minimum and maximum selectable numbers are 2 and 64.
""")
        if bits % 2 == 0 and bits < 66 and bits > 0:
            return bits, time
        else:
            raise ValueError('Please type a number between 2 and 64.')
    

def binary_mode(bits, time):

def hex_mode(bits, time):


# Starts the game and prompts user to select a mode.
def start_game():
    welcome_message = "Welcome to the Binary/Hexadecimal Speed Testing Game!\n"
    
    print(welcome_message)

    try:
        game_mode = input("Would you like to play in [b]inary or [h]ex mode? ").lower()
        if game_mode in "binary":
            binary_mode()
        elif game_mode in "hex":
            hex_mode()
        else:
            raise ValueError('Please type in "hex" or "binary".')
    except ValueError as err:
        print(err)
    
    

    

start_game()



# Ask user if they want to guess in hex or binary

# Ask user for number of bits they would like to guess, range 2-16 (for now)

# Have a timer increment time

# Have a score board and a high score option available

# Save a record to a .json file of the high score (sorted by hex and binary)

# Have a reverse mode for inputting base 10 numbers to guess binary / hex numbers

# consider incorporating ASCII codes as well
