# This is the folder for generic functions

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
