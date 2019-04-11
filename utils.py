# This file will continue the classes used for the games

# This class is for determining if an answer is right or wrong
class CheckGuess:
    def __init__(self, user_guess, game_num):
        self.user_guess 

# This is the parent class for the games
class Game:
    def __init__(self, time=False, bits=8, high_score=0):
        self.time = time
        self.bits = bits
        self.high_score = high_score
