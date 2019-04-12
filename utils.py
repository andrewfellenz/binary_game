import datetime
import random

# This file will continue the classes used for the games
# This is the parent class for the games
class Game:
    def __init__(self, time=False, bits=8, high_score=0):
        self.time = time
        self.bits = bits
        self.high_score = high_score


    # This property dynamically determines if there is a timer or not
      # This property needs to be modified to actually BE the timer
    @property
    def timer(self):
        if self.time == True:
            print("@property time is true")
            # Get current date time as starting point
            # Routinely check datetime to make sure
              # that the game isn't out of time
            
        else:
            print("No time limit")
    
    # This will be the code to convert numbers to binary or hex
    def get_nums(self):
        while True:
            guess_numbers = set([random.randint(0, 255) for _ in range(10)])
            if len(guess_numbers) < 10:
                continue
            else:
                return guess_numbers

    
    # Converts a random number into a plain binary Str for comparison
    def convert(self, num):
        converted_num = str(bin(num))
        answer_num = [num for num in converted_num[2:]]
        while len(answer_num) < self.bits:
            answer_num.insert(0, "0")
        return ''.join(answer_num)
           

    def play(self):
        nums = get_nums()
        count = 0
        while True count < 10:

            
e = Game()
