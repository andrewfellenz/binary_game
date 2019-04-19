# The game still needs some updates. The issues are the following:
# Game mode is still not selectable by user
# Tutorial still needs to be built
# Still needs to be ported to Android / IOS
# Still needs GUI to be made
# Needs more comments explaining functions

# Still need a way to display the HUD and Time
# Without disrupting everything else
# The main issue is with how the HUD and check_input
# functions are coupled together.

# Binary and Hex modes still need to check input

import random
import json
import utils



mode = ['hex', 'bin']
mode_question = "\nDo you want to play in [Hex] or [Bin] Mode? "
mode_error_text= '\nYou must enter either Hex or Bin!\nPress Enter to continue.'

bits = [1, 2, 4, 8, 16, 32, 64]
bits_question = "\nHow many bits would you like to play with? "
bits_error_text = '\nYou must enter a number that is a power of 2!\nPress Enter to continue.'

again = ['yes', 'no', 'y', 'n']
again_question = "\nWould you like to play again? [Yes/No] "
again_error_text = '\nYou must enter yes or no.\n'

BINARY = [0, 1]
binary_error_text = 'Please enter only 0s and 1s in the correct format.\n'

HEX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
hex_error_text = 'Please Enter only numbers 0-9 and letters A-F in the correct format.\n'

welcome = "Welcome to the Machine Language Game!"


def check_input(terms, question, error_text, integer=False):
    while True:
        utils.clear_screen()
        try:
            if integer == False:
                ask_user = input(question).lower()
            else:
                ask_user = input(question)
                try:
                    ask_user = int(ask_user)
                except:
                    raise ValueError(error_text)
            if ask_user in terms:
                utils.clear_screen()
                return ask_user
            else:
                raise ValueError(error_text)
        except ValueError as error:
            utils.clear_screen()
            input(error)


# This is the parent class for the games
class Game:
    def __init__(self, mode, bits, score=0, time=None):
        self.time = time
        self.bits = bits
        self.mode = mode
        self.score = score

    def __str__(self):
        message = "\nScore: {}  |  High Score: {}  |  Mode: {}  |  Bits: {}  |  Time limit: {}\n".format(
            self.score, self.high_score, self.mode, self.bits, self.time)
        return message
    
    # This function is not in use at this time: 4/16/19
    def time_clock(self):
        time_left = 3
        while time_left > 0:
            time.sleep(1)
            time_left -= 1
            print(time_left)
        else:
            utils.clear_screen()
            print("GAME OVER")
            raise SystemExit()
        thread_timer = threading.Thread(target=time_clock)

    # This will be the code to convert numbers to binary or hex
    def get_nums(self):
        while True:
            number_set = set([random.randint(0, ((2 ** self.bits) - 1))
                              for _ in range(2 * self.bits)])
            if len(number_set) < (2 * self.bits):
                continue
            else:
                guess_list = [num for num in number_set]
                return guess_list

    # Converts a random number into a plain binary Str for comparison
    def convert(self, num):
        if self.mode == 'bin':
            converted_num = str(bin(num)[2:])
            answer_num = [num for num in converted_num]
            while len(answer_num) < self.bits:
                answer_num.insert(0, "0")
            return ''.join(answer_num)

        elif self.mode == 'hex':
            converted_num = str(hex(num)[2:])
            answer_num = [num.upper() for num in converted_num]
            while len(answer_num) < self.bit_representation:
                answer_num.insert(0, "0")
            return ''.join(answer_num)

    @property
    def total_bits(self):
        total_bits = [str(num) for num in range(1, (self.bit_representation + 1))]
        total_bits.reverse()
        return ''.join(total_bits)        


    # This has still not been implemented
    @property
    def char_set(self):
        # This has been tested and is correct
        char_set = [self.convert(num) for num in range(0, (2 ** self.bits))]
        return char_set

    @property
    def bit_representation(self):
        if self.mode == 'bin':
            bit_representation = self.bits
        elif self.mode == 'hex':
            bit_representation = int(self.bits / 4)
        return bit_representation

    # @property
    # def format_question(self):
    #     message =
    #     "What is {} in {}?\nUse the format \"{}\"\n\n
    #     Bit numbers by position:\n
    #     {}\n".format(
    #         current_number, self.mode,
    #         ("0" * self.bit_representation), self.total_bits))
    #     return message


    # This property dynamically grabs the high score from a separate file
    # at the beginning of each game.
    @property
    def high_score(self):
        try:
            with open('high_score.json', 'r') as scores:
                scores.seek(0)
                all_scores = json.load(scores)
                high_score = max(all_scores.values())
                # Leaving a spot to put name recall
                return high_score
        except Exception:
            with open('high_score.json', 'w') as high_score:
                json.dump({"New player": 0}, high_score, indent=2)
            input('Welcome to the Machine Language Challenge!')
            utils.clear_screen()
            return 0

    # This is the command to end the game and set a new high score
    def end_game(self):
        utils.clear_screen()
        print("\nGame over")
        if self.score > self.high_score:
            while True:
                try:
                    # still needs alpha check
                    initials = input("Please enter your initials! ").lower()
                    high_score = {initials: self.score}
                    # This code is here for now, but may be moved
                    with open('high_score.json', 'w') as write_file:
                        json.dump(high_score, write_file, indent=2)
                    break
                # This still needs tooling
                except ValueError:
                    # still need proper exception handling
                    pass
        else:
            input('\nYour final score was: {}!'.format(self.score))

    # prompts player to decide if they want to play another round
    def play_again(self):
        self.hud()
        play = check_input(again, again_question, again_error_text)
        if play == 'yes' or play == 'y':
            self.score = 0
            count = 0
            Game.menu()
        else:
            utils.clear_screen()
            raise SystemExit

    def play(self):
        nums = self.get_nums()
        count = 0
        wrong_answers = {}
        while count < (2 * self.bits):
            self.hud()
            current_number = random.choice(nums)
            guess = input("What is {} in {}?\nUse the format \"{}\"\n\n"
                          "Bit numbers by position:\n"
                          "{}\n".format(current_number, self.mode,
                                      ("0" * self.bit_representation),
                                       self.total_bits))
            correct_answer = self.convert(current_number)
            if self.mode == 'hex':
                try:
                    guess = guess.upper()
                    if guess in self.char_set:
                        if guess == correct_answer:
                            input("\nThat's the correct answer!")
                            self.score += 1
                        else:
                            input("\nThat is not the right answer!")
                            self.hud()
                            print("That is not the right answer!")
                            print("You answered: {}".format(guess))
                            input("{} in hex is {}".format(current_number, correct_answer))
                            wrong_answers.update({guess: correct_answer})
                        nums.remove(current_number)
                        count += 1
                    else:
                        raise ValueError(hex_error_text)
                except ValueError as error:
                    self.hud(error, pause=True)
                    
            elif self.mode == 'bin':
                try:
                    if guess in self.char_set:
                        if guess == correct_answer:
                            print("\nThat's the correct answer!")
                            self.score += 1
                        else:
                            self.hud()
                            print("That is not the right answer!")
                            print("You answered: {}".format(guess))
                            input("{} in binary is {}".format(current_number, correct_answer))
                            wrong_answers.update({guess: correct_answer})
                        nums.remove(current_number)
                        count += 1
                    else:
                        raise ValueError(binary_error_text)
                except ValueError as error:
                    self.hud(error, pause=True)
        self.hud()
        self.end_game()
        self.play_again()
    
    # This is the first method called in the game
    @classmethod
    def menu(cls):
        utils.clear_screen()
        game = cls(check_input(mode, mode_question, mode_error_text),
        check_input(bits, bits_question, bits_error_text, integer=True))
        game.play()

    def hud(self, *args, pause=False):
        utils.clear_screen()
        print(self)
        if args:
            for arg in args:
                print(arg)
        if pause == True:
            input("Press Enter to continue.")

    def check_input(self, terms, question, error_text, integer=False):
        while True:
            try:
                if integer == False:
                    ask_user = input(question).lower()
                else:
                    ask_user = input(question)
                    try:
                        ask_user = int(ask_user)
                    except ValueError:
                        self.hud(error_text)
                if ask_user in terms:
                    self.hud()
                    return ask_user
                else:
                    raise ValueError(error_text)
            except ValueError as error:
                self.hud(error)

        

if __name__ == '__main__':

    Game.menu()


