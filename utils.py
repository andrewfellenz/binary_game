import os
import random
import time
import datetime


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


    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    
    # This will be the code to convert numbers to binary or hex
    def get_nums(self):
        while True:
            number_set = set([random.randint(0, 15) for _ in range(10)])
            if len(number_set) < 10:
                continue
            else:
                guess_list = [num for num in number_set]
                return guess_list
                

    
    # Converts a random number into a plain binary Str for comparison
    def convert(self, num):
        converted_num = str(bin(num))
        answer_num = [str(num) for num in converted_num[2:]]
        while len(answer_num) < self.bits:
            answer_num.insert(0, "0")
        return ''.join(answer_num)
           

    def play(self):
        nums = self.get_nums()
        count = 0
        score = 0
        while count < 10:
            self.clear_screen()
            print("Current score:{}\n".format(score))
            current_number = random.choice(nums)
            nums.remove(current_number)
            guess = input("What is {} in binary? ".format(current_number))
            correct_answer = self.convert(current_number)
            if guess == correct_answer:
                score += 1
            count += 1
           
game = Game()
game.play()
