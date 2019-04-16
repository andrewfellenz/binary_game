import os
import random
import time
import threading
import json


#BINARY
#HEX
# These constants should use list comprehensions to contain all possible combinations of characters

# This file will continue the classes used for the games
# This is the parent class for the games
class BaseGame:
    def __init__(self, time=True, bits=8, high_score=0, char_set=None):
        self.time = time
        self.bits = bits
        self.high_score = high_score
        self.char_set = char_set


    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def char_check(self, char_set, char, input_message):
        while True:
            guess = input(input_message)
            for each in guess:
                if each in self.char_set:
                    continue
                else:
                    # needs work
                    pass

        
    # This property dynamically determines if there is a timer or not
      # This property needs to be modified to actually BE the timer
    # @property
    # def timer(self):
    #     if self.time == True:
    def time_clock(self):
        time_left = 3
        while time_left > 0:
            time.sleep(1)
            time_left -= 1
            print(time_left)
        else:
            self.clear_screen()
            print("GAME OVER")
            raise SystemExit()
        
        thread_timer = threading.Thread(target=time_clock)

   

    # This will be the code to convert numbers to binary or hex
    def get_nums(self):
        while True:
            number_set = set([random.randint(0, (self.bits ** 2)) for _ in range(10)])
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


    @property
    def game_mode(self, bits):
        # This has been tested and is correct
        self.char_set = [convert(num) for num in range(0, (bits ** 2))]
        print(char_set)


    @property
    def high_score(self):
        try:
            with open('high_score.json', 'r') as scores:
                all_scores = scores.read(1)
                high_score = max(scores.values)
           

    def play(self):
        nums = self.get_nums()
        count = 0
        score = 0
        wrong_answers = {}
        #self.time_clock()
        while count < 10:
            self.clear_screen()
            print("Current score:{}\n".format(score))
            current_number = random.choice(nums)
            nums.remove(current_number)
            guess = input("What is {} in binary?\nUse the format \"00000000\" ".format(current_number))
            correct_answer = self.convert(current_number)
            if guess == correct_answer:
                input("That's the correct answer!")
                score += 1
            else:
                input("That is not the right answer!")
                wrong_answers.update({guess: correct_answer})
                input(wrong_answers)
            count += 1
        self.clear_screen()
        input("Your final score was {}!".format(score))
        initials = input("Please enter your name. ")
        high_score = {initials: score}
        with open('high_scores.json', 'w') as write_file:
            json.dump(high_score, write_file, indent=2)
        
           
game = BaseGame()
game.play()


class Hex(BaseGame):
    pass
    #def __init__(self):
        #super().__init__(char_set=BINARY)
