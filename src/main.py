from sysconfig import get_scheme_names
from players import UserPlayer, EasyComputerPlayer, GeniusComputerPlayer 
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]  #we will use a singe list to rep 3x3 board
        self.current_winner = None # Keep track of the winner
    
    @staticmethod
    def number_chart():
        #0 | 1 | 2 | (this tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print("-------------")
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print("-------------\n")
    
    def print_board(self):
        # The calaculates the rows
        print("-------------")
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]: # If time try and change this to match the num pad on the key board.
            print('| ' + ' | '.join(row) + ' |')
        print("-------------")
            
    def free_spots(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] #List comprehension outlining all the free spots available on the board.    

    def make_move(self, player, letter):
        position = player.get_move(self)
        self.board[position] = letter
        print(f"{player.name} makes a move to position {position}")
        self.print_board()

def play(game, x_player, y_player):
    print('Commencing game....')
    # Add in option here to play scissor, paper rock to decide who goes first. 
    while game.free_spots():
        game.make_move(x_player, "X")
        if game.free_spots():
            game.make_move(y_player, "O")           


            


def select_opponent():
    print("Lots of players are around around today who would love to play Tic-Tac-Toe with you.\n")
    time.sleep(2)

    while True:
        selection = input("Select from the following opponents:\n a) Peter the Panda\n b) Katie the Koala\n c) Ollie the Octopus\n d) Danni the Dolphin\n\nEnter a single letter from (a-d) ")
        selection = selection.lower().strip()
        if selection not in ("a", "b", "c", "d"):
            time.sleep(0.8)
            print("\nSorry that is not a valid option. You must enter a single letter from (a-d).")
            continue
        else:
            break
    if selection == "a":        
        return pete_panda
    elif selection == "b":
        return katie_koala
    elif selection == "c":
        return ollie_octopus
    else:
        return danni_dolphin
    




if __name__ == '__main__':
    print("Welcome to TicTacToe!\n")
    player_name = (input("What is your name?: "))
    print("Hello " + player_name.title() + "! So lovely to meet you. That's a great name.\n")
    time.sleep(0.8)
    user_player_1 = UserPlayer('X', player_name)
    pete_panda = EasyComputerPlayer('O', "Pete the Panda")
    katie_koala = EasyComputerPlayer('O', "Katie the Koala")
    ollie_octopus = GeniusComputerPlayer('O', "Ollie the Octopus")
    danni_dolphin = GeniusComputerPlayer('O', "Danni the Dolphin")
    standard_board = TicTacToe()
    opponent = select_opponent()
    print(f"You have selected {opponent.name} as your opponent today.  Good choice.")
    print("Our game will be played on a 3 by 3 board using the following positions.\n")
    standard_board.number_chart()   
    play(standard_board, user_player_1, opponent)
    





   
    # returns the winner of the game if there is one. 
    # o_player = GeniusComputerPlayer('O')
    # t = TicTacToe()
    # play(t, x_player, o_player, print_game=True) 