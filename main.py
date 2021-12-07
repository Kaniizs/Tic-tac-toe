from Game import Game
import turtle


if __name__ == '__main__':
    mode = int(turtle.textinput("Welcome to tic tac toe game", '1.Human vs Human\n2.Computer vs Human\nChoose a gamemode to play:'))
    if mode == 2:
        player1_name = turtle.textinput('Player', 'Put a player name: ')
        g = Game(player1_name)
        g.main()
    else:
        player1_name = turtle.textinput('P1', 'Please enter player1 name: ')
        player2_name = turtle.textinput('P2', 'Please enter player2 name: ')
        g = Game(player1_name, player2_name)
        g.main()

       
       
