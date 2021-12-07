import turtle
from Board import Board
from Player import Human_Player, Computer_Player


class Game:

    def __init__(self, player1_name, player2_name=None) -> None:
        """Give a player to choose a value O or X"""
        self.board = Board()

        if not player2_name:
            human_val = turtle.textinput('Game has started', 'Choose your value(o/x)')
            computer_val = 'o' if human_val == 'x' else 'x'

            self.player1 = Human_Player(player1_name, human_val)
            self.player2 = Computer_Player(computer_val)
            self.player2.name = 'Bot'

        else:
            self.player1 = Human_Player(player1_name, 'o')
            self.player2 = Human_Player(player2_name, 'x')

    def if_break(self):
        """Check if a player have already win a game"""
        if self.board.if_win('o'):
            return 'o'
        if self.board.if_win('x'):
            return 'x'

    def main(self):
        """Play a game turn by turn and stop the game if a player has won a game"""

        now_player = self.player1

        for _ in range(9):

            now_player.mark_value(self.board)

            is_break = self.if_break()

            if is_break:
                winner = self.player1 if is_break == self.player1.val else self.player2
                print(f'{winner.name} won')
                break

            now_player = self.player2 if now_player == self.player1 else self.player1
        else:
            print('Draw!')
