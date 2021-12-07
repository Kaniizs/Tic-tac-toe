import turtle
import random


class Player:

    def __init__(self, val) -> None:
        self.val = val


class Human_Player(Player):

    def __init__(self, name, val) -> None:
        """Input a name"""
        super().__init__(val)
        self.name = name

    def mark_value(self, board):
        """Put a mark in an input location for a player"""

        loc = int(turtle.textinput('Please choose loc form here:', ' 0 | 1 | 2\n 3 | 4 | 5\n 6 | 7 | 8'))
        if not board.mark_value(loc, self.val):
            self.mark_value(board)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('name must be a string')
        self._name = new_name



class Computer_Player(Player):

    def mark_value(self, board):
        """Put a mark in a random valid location for computer player"""
        loc = random.randrange(9)
        if not board.mark_value(loc, self.val):
            self.mark_value(board)