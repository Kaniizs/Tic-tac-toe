import turtle
from time import sleep
import random

from database import Db


class Board():

    def __init__(self):
        self.__turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.setup()
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.display()

    def setup(self):
        self.screen.bgcolor("#011627")
        self.screen.title("Tic tac toe game")

    def display(self):
        """Display a 3 x 3 grid by using a __turtle to draw"""
        self.screen.reset()
        self.__turtle.speed(100)
        self.__turtle.penup()
        self.draw_board()
        self.draw_value()

    def draw_board(self):

        self.__turtle.pensize(10)
        self.__turtle.color("#39FF14")

        for i in range(2):
            self.__turtle.goto(-300, 100 - 200 * i)
            self.__turtle.pendown()
            self.__turtle.forward(600)
            self.__turtle.penup()
        self.__turtle.right(90)

        for j in range(2):
            self.__turtle.goto(-100 + 200 * j, 300)
            self.__turtle.pendown()
            self.__turtle.forward(600)
            self.__turtle.penup()

    def draw_value(self):

        self.__turtle.pencolor('white')
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                if val in ('o', 'x'):
                    val = '❌' if val == 'x' else '🟢'
                    self.__turtle.goto(200*(j+1)-400 - 15, -200*(i+1)+400 - 15)
                    self.__turtle.write(val, False, font=('Menlo', 15, 'normal'))

    def yord(self, loc, val):
        j, i = loc % 3, loc // 3
        if loc not in range(9) or self.board[i][j] != ' ':
            print('Invalid value')
            return False
        self.board[i][j] = val
        self.display()
        return True

    def if_win(self, val):

        win_vertical = any(
            all(self.board[i][j] == val for j in range(3)) for i in range(3))
        win_horizontal = any(
            all(self.board[i][j] == val for i in range(3)) for j in range(3))

        diag_1 = all(self.board[i][j] == val for i in range(3)
                     for j in range(3) if i == j)
        diag_2 = all(self.board[i][j] == val for i in range(3)
                     for j in range(3) if (2-i) == j)

        win_diagonal = diag_1 or diag_2

        return win_horizontal or win_vertical or win_diagonal


class Player:

    def __init__(self, val) -> None:
        self.val = val


class Humen_Player(Player):

    def __init__(self, name, val) -> None:
        super().__init__(val)
        self.name = name

    def yord(self, board):

        loc = int(turtle.textinput(f"{self.name}'s Turn",
                  'PLease choose location from here:\n\n 0 | 1 | 2\n 3 | 4 | 5\n 6 | 7 | 8'))
        if not board.yord(loc, self.val):
            self.yord(board)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('name must be a string')
        self._name = new_name


class Computer_Player(Player):
    
    def __init__(self, val) -> None:
        super().__init__(val)
        self.name = 'Bot'

    def yord(self, board):
        loc = random.randrange(9)
        if not board.yord(loc, self.val):
            self.yord(board)


class Game:

    def __init__(self, player1_name, player2_name=None) -> None:
        self.board = Board()
        self.database = Db()

        if not player2_name:
            human_val = turtle.textinput('BANANA!', 'Choose your value(o/x)')
            computer_val = 'o' if human_val == 'x' else 'x'

            self.player1 = Humen_Player(player1_name, human_val)
            self.player2 = Computer_Player(computer_val)
            self.player2.name = 'Bot'
            self.mode = 'bot'

        else:
            self.player1 = Humen_Player(player1_name, 'o')
            self.player2 = Humen_Player(player2_name, 'x')
            self.mode = 'player'

    def if_break(self):
        if self.board.if_win('o'):
            return 'o'
        if self.board.if_win('x'):
            return 'x'

    def main(self):

        now_player = self.player1

        for _ in range(9):
            print(self.board.board)

            now_player.yord(self.board)

            is_break = self.if_break()

            if is_break:
                winner = self.player1 if is_break == self.player1.val else self.player2
                print(f'{winner.name} won')
                self.database.update_data(self.mode, self.player1.name, self.player2.name, winner.name)
                break

            now_player = self.player2 if now_player == self.player1 else self.player1
        else:
            print('Draw!')


if __name__ == '__main__':
    G = Game('God', 'kong')
    G.main()
