import turtle
from time import sleep
class Board():

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.setup()
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.display()

    def setup(self):
        """Setup a screen setting"""
        self.screen.bgcolor("#011627")
        self.screen.title("Tic tac toe game")

    def display(self):
        """Display a 3 x 3 grid by using a turtle to draw"""
        self.screen.reset()
        self.turtle.speed(100)
        self.turtle.penup()
        self.draw_board()
        self.draw_value()

    def draw_board(self):
        """Draw a Tic tac toe board with a turtle"""

        self.turtle.pensize(10)
        self.turtle.color("#39FF14")

        for i in range(2):
            self.turtle.goto(-300, 100 - 200 * i)
            self.turtle.pendown()
            self.turtle.forward(600)
            self.turtle.penup()
            self.turtle.pencolor('white')
            self.turtle.pencolor("#39FF14")
        self.turtle.right(90)

        for j in range(2):
            self.turtle.goto(-100 + 200 * j, 300)
            self.turtle.pendown()
            self.turtle.forward(600)
            self.turtle.penup()
            self.turtle.pencolor('white')
            self.turtle.pencolor("#39FF14")

    def draw_value(self):
        """Draw an O or a X mark"""
        self.turtle.pencolor('white')
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                if val in ('o', 'x'):
                    val = '❌' if val == 'x' else '🟢'
                    self.turtle.goto(200*(j+1)-400 - 15, -200*(i+1)+400 - 15)
                    self.turtle.write(val, False, font=('Menlo', 15, 'normal'))
    
    def mark_value(self, loc, val):
        '''Put an O or X mark in location'''
        j, i = loc % 3, loc // 3
        if loc not in range(9) or self.board[i][j] != ' ':
            print('Invalid value')
            return False
        self.board[i][j] = val
        self.display()
        return True
    
    def if_win(self, val):
        """Check if a player marks match win conditions"""
        win_vertical = any(all(self.board[i][j] == val for j in range(3)) for i in range(3))
        win_horizontal = any(all(self.board[i][j] == val for i in range(3)) for j in range(3))

        diag_1 = all(self.board[i][j] == val for i in range(3) for j in range(3) if i == j)
        diag_2 = all(self.board[i][j] == val for i in range(3) for j in range(3) if (2-i)==j)

        win_diagonal = diag_1 or diag_2

        return win_horizontal or win_vertical or win_diagonal
