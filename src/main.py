from players import UserPlayer, EasyComputerPlayer, GeniusComputerPlayer 
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]  #we will use a singe list to rep 3x3 board
        self.current_winner = None # Keep track of the winner
    
    def print_board(self):
        # The calaculates the rows
        print("-------------")
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]: # If time try and change this to match the num pad on the key board.
            print('| ' + ' | '.join(row) + ' |')
        print("-------------")
            
def play(game, x_player, o_player):
    pass

def select_opponent():
    print("Lots of players are around around today who would love to play TicTacToe with you.")
    time.sleep(2)

    while True:
        selection = input("Select from the following opponents:\n a) Peter the Panda\n b) Katie the Koala\n c) Ollie the Octopus\n d) Danni the Dolphin\n\n Enter a single letter from (a-d) ")
        selection = selection.lower().strip()
        if selection not in ("a", "b", "c", "d"):
            time.sleep(0.8)
            print("You must enter a single letter from (a-d)")
            continue
        else:
            break
    if selection == "a":        
        o_player = pete_panda
    elif selection == "b":
        o_player = katie_koala
    elif selection == "c":
        o_player = ollie_octopus
    else:
        o_player = danni_dolphin
    print(f"You have selected {o_player.name} as your opponent today.  Good choice")
    return o_player



    




if __name__ == '__main__':
    print("Welcome to TicTacToe!")
    player_name = (input("What is your name?: "))
    print("Hello " + player_name.title() + "! So lovely to meet you. That's a great name.\n")
    time.sleep(0.8)
    user_player_1 = UserPlayer('X', player_name)
    pete_panda = EasyComputerPlayer('O', "Pete the Panda")
    katie_koala = EasyComputerPlayer('O', "Katie the Koala")
    ollie_octopus = GeniusComputerPlayer('O', "Ollie the Octopus")
    danni_dolphin = GeniusComputerPlayer('O', "Danni the Dolphin")
    select_opponent()
    
    





    user_player_1.get_move()
    # returns the winner of the game if there is one. 
    # o_player = GeniusComputerPlayer('O')
    # t = TicTacToe()
    # play(t, x_player, o_player, print_game=True) 