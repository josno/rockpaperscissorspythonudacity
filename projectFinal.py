import random

# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    """Randomplayer that picks rock, scissor,
    paper at using random choice module"""
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        """Changes all capital letters to lowercase."""
        move = input("Pick one weapon - rock, scissors, paper: ").lower()
        while move not in moves:
            """Prints out a message to try again
            when something is mistyped or a weapon that is not
            in the moves variable is typed. Will keep repeating
            until a validated move is played."""
            move = input("You can only use rock, scissors, paper: ").lower()
        return move


class ReflectPlayer(Player):
    """ ReflectPlayer takes the opponent's
        move and makes it its next move.
        Initializes a storedmove variable that
        can change when learn function is run."""
    def __init__(self):
        self.storedmove = 'rock'

    def move(self):
        """ When self.learn doesn't have a storedmove
        variable, ReflectPlayers picks a random move (Round 1 only).
        When self.learn has a storedmove (Round 2 and on) it returns
        the storedmove as the next move."""
        if self.learn is None:
            return random.choice(moves)
        else:
            return self.storedmove

    def learn(self, my_move, their_move):
            """Remembers other player's move to use
            it as the next ReflectPlayer's move."""
            self.storedmove = their_move
            return self.storedmove


class CyclePlayer(Player):
    """CyclePlayer remembers its last move in
    order to play the next move on the list."""
    def __init__(self):
        self.storedmove = 'rock'

    def move(self):
        if self.learn is None:
            return random.choice(moves)
        elif self.storedmove != 'scissors':
            """ If the item pick is not scissors (end of list),
            cycle through the list and find the current move,
            then return the move one after the current move.
            move = ['rock', 'paper', 'scissors']
            If storedmove is 'rock', it will return 'paper' and so on."""
            for item in moves:
                played = self.storedmove
                nextmove = moves[moves.index(played) + 1]
                return nextmove
        else:
            """Scissors is at the end of list so it will always
            return the beginning of the list ('rock')."""
            return 'rock'

    def learn(self, my_move, their_move):
        """Remembers the CyclePlayer's last move
        and puts it in storedmove variable."""
        self.storedmove = my_move
        return self.storedmove


class Game:
    """Class Game initializes all scoring and
    what type of players will play in the game.
    It has the points system pone_score and
    ptwo_score that adds up total points. Game
    will print result after all three rounds are played."""
    def __init__(self, p1, p2):
        self.p1 = HumanPlayer()
        self.p2 = HumanPlayer()
        self.pone_score = 0
        self.ptwo_score = 0

    def beats(self, one, two):
        """Returns True or False on winning weapons."""
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        """Instances include round-level moves, points and winners."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"P1: {move1}  P2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        """Proneround_score and ptworound_score resets
        to 0 at beginning of every round."""
        poneround_score = 0
        ptworound_score = 0
        if self.beats(move1, move2):
            print("Player 1 Wins This Round")
            poneround_score = 1
            self.pone_score += 1
        elif self.beats(move2, move1):
            print("Player 2 Wins This Round")
            ptworound_score = 1
            self.ptwo_score += 1
        else:
            print("Tie! No Points.")
        print(f"Round Points - P1: {poneround_score} | P2: {ptworound_score}")

    def score(self):
        """Prints final scoreboard at the end of
        three rounds and declares a winner."""
        score_message = {
                            'Onewins': "\nThe Winner is Player 1!",
                            'Twowins': "\nThe Winner is Player 2!",
                            'Tie': "\nTie! Looks like everyone's a winner!",
                            'Nowinner': "\nYikes, neither of you win!"
                        }
        if self.pone_score > self.ptwo_score:
            print(score_message['Onewins'])
        elif self.pone_score < self.ptwo_score:
            print(score_message['Twowins'])
        elif self.pone_score == 0 and self.ptwo_score == 0:
            print(score_message['Nowinner'])
        else:
            print(score_message['Tie'])

    def play_game(self):
        print("Welcome, to the Rock, Scissor, Paper Game.")
        print("Can you win in three rounds?")
        print("Ready? Let's begin!")
        for round in range(1, 4):
            print(f"\nRound {round}:")
            self.play_round()
        self.score()
        print(f"\nFinal Scores")
        print(f"P1: {self.pone_score} ||  P2: {self.ptwo_score}")
        print(f"Great Game!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
