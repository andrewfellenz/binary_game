import os
import random
import time
import threading
import json


# This is the parent class for the games
class BaseGame:
    def __init__(self, time=True, bits=8, mode='binary', score=0):
        self.time = time
        self.bits = bits
        self.mode = mode
        self.score = score

    # Used to clear the screen between messages / guesses
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
            number_set = set([random.randint(0, ((2 ** self.bits) - 1))
                              for _ in range(2 + self.bits)])
            if len(number_set) < (2 + self.bits):
                continue
            else:
                guess_list = [num for num in number_set]
                return guess_list

    # Converts a random number into a plain binary Str for comparison
    def convert(self, num):
        if self.mode == 'binary':
            converted_num = str(bin(num)[2:])
            answer_num = [num for num in converted_num]
            while len(answer_num) < self.bits:
                answer_num.insert(0, "0")
            return ''.join(answer_num)

        elif self.mode == 'hex':
            converted_num = str(hex(num)[2:])
            answer_num = [num for num in converted_num]
            while len(answer_num) < self.bit_representation:
                answer_num.insert(0, "0")
            return ''.join(answer_num)

    @property
    def game_mode(self):
        # This has been tested and is correct
        self.char_set = [self.convert(num) for num in range(0, (bits ** 2))]

    @property
    def bit_representation(self):
        if self.mode == 'binary':
            bit_representation = self.bits
        elif self.mode == 'hex':
            bit_representation = int(self.bits / 4)
        return bit_representation

    # This property dynamically grabs the high score from a separate file
    # at the beginning of each game.
    @property
    def high_score(self):
        try:
            with open('high_scores.json', 'r') as scores:
                scores.seek(0)
                all_scores = json.load(scores)
                high_score = max(all_scores.values())
                # Leaving a spot to put name recall
                return high_score
        except Exception:
            input('There is no high score file to read from.')

    # This is the command to end the game and set a new high score
    def end_game(self):
        print("Game over")
        if self.score > self.high_score:
            print("Congratulations! {} is the new high score!"
                  .format(self.score))
            while True:
                try:
                    # still needs alpha check
                    initials = input("Please enter your initials! ").lower()
                    high_score = {initials: self.score}
                    # This code is here for now, but may be moved
                    with open('high_scores.json', 'w') as write_file:
                        json.dump(high_score, write_file, indent=2)
                    break
                # This still needs tooling
                except ValueError:
                    # still need proper exception handling
                    pass
        input("Your final score is: {}".format(self.score))

    # prompts player to decide if they want to play another round
    def play_again(self):
        pass

    def play(self):
        nums = self.get_nums()
        count = 0
        wrong_answers = {}
        # self.time_clock()
        while count < (2 + self.bits):
            self.clear_screen()
            print("Current score: {}  |  Current high score: {}\n"
                  .format(self.score, self.high_score))
            current_number = random.choice(nums)
            nums.remove(current_number)
            guess = input("What is {} in {}?\nUse the format \"{}\" "
                          .format(current_number, self.mode,
                                  ("0" * self.bit_representation)))
            correct_answer = self.convert(current_number)
            if guess == correct_answer:
                input("\nThat's the correct answer!")
                self.score += 1
            else:
                input("\nThat is not the right answer!")
                wrong_answers.update({guess: correct_answer})
                input(wrong_answers)
            count += 1
        self.clear_screen()
        self.end_game()
        # self.play_again()


game = BaseGame(bits=2)
game.play()


class Hex(BaseGame):
    def __init__(self):
        super().__init__(bits=8, mode='hex')


game_2 = Hex()
# game_2.play()
