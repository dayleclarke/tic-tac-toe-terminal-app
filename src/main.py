from players import UserPlayer, EasyComputerPlayer, ExpertComputerPlayer 
from random import choice
import time
import pyfiglet
from simple_term_menu import TerminalMenu
import clearing


class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]  #we will use a singe list to rep 3x3 board
        self.current_winner = None # Keep track of the winner
    
    @staticmethod
    def board_number_indices():
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
            
    def free_positions(self):
        return [i for i, position in enumerate(self.board) if position == ' '] #List comprehension outlining all the free spots available on the board.   
    
    def empty_squares(self): # This will return true if there are empty squares on the board. False means all the positions are taken. 
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ') 

    def make_move(self, position, letter):
        if self.board[position] == " ":
            self.board[position] = letter
            if self.winner(position, letter):
                self.current_winner = letter

    def test_move(self, possible_move, player_letter):
        if self.board[possible_move] == ' ':
            self.board[possible_move] = player_letter
        if self.winner(possible_move, player_letter):
            return True
        else: 
            return False
           
    def winner(self, position, letter):
        # winner if 3 in a row anywhere. Must check row, column and both diagonals
        #row check       
        row_index = position // 3 # how many times is the position index divisable by 3?  This will indicate its row (either 0, 1 or 2). 
        row = self.board[row_index * 3 : (row_index + 1) * 3] # This selects the entire row that the position is in. 
        if all([square == letter for square in row]):
            return True
        
        #column check
        col_index = position % 3 # When you divide the position by 3 what is left over? (Position modu 3 will indicate its column index (either 0, 1 or 2))
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([square == letter for square in column]):
            return True
        
        #diagonal check
        #diagonals left to right are on (0, 4, 8)
        #diagonals right to left are on (2, 4, 6)
        if position % 2 == 0: # Only even numbers run along the diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([square == letter for square in diagonal1]):
                return True           
            diagonal2= [self.board[i] for i in [2, 4, 6]]
            if all([square == letter for square in diagonal2]):
                return True
        
        # If all checks fail there is no winner return False
        return False

    def reset_board(self):
        self.board = [' ' for i in range(9)]  #we will use a singe list to rep 3x3 board
        self.current_winner = None

def select_starting_player(user_player, computer_player):
    hand_gestures = {
      "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
"scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
  }
    print("To begin we will play a quick game of scissors, paper, rock to determine which player will start.\nMenu entries can be selected with the arrow or j/k keys ") 
    while True:
        user_options = list(hand_gestures.keys())
        terminal_menu = TerminalMenu(user_options, title="Hand Gesture Options:")
        menu_entry_index = terminal_menu.show()  
        user_choice = user_options[menu_entry_index] 
        print(hand_gestures[user_choice])
        print(f"{user_player} has chosen to play {user_choice}.")
        time.sleep(0.8)
        opponent_choice = choice(list(hand_gestures.keys()))
        time.sleep(0.8)
        print(hand_gestures[opponent_choice])
        print(f"{computer_player} has chosen to play {opponent_choice}.")
        time.sleep(0.8)
        if user_choice == opponent_choice: 
            print(f"Great minds think alike! You both selected {user_choice}. Please select again.")
            continue
        else:
            break

    if user_choice == "paper":
        if opponent_choice == "scissors":
            print(f"{computer_player}'s scissors cuts {user_player}'s paper. {computer_player} wins and will go first!")
            return computer_player
        elif opponent_choice == "rock":
            print(f"{user_player}'s paper covers {computer_player}'s scissors. {user_player} wins and will go first!")
            return user_player
    
    if user_choice == "scissors":
        if opponent_choice == "paper":
            print(f"{user_player}'s scissors cuts {computer_player}'s paper. {user_player} wins and will go first!")
            return user_player
        elif opponent_choice == "rock":
            print(f"{computer_player}'s rock crushes {user_player}'s scissors. {computer_player} wins and will go first!")
            return computer_player


    if user_choice == "rock":
        if opponent_choice == "paper":
            print(f"{computer_player}'s paper covers {user_player}'s rock. {computer_player} wins and will go first!")
            return computer_player
        elif opponent_choice == "scissors":
             print(f"{user_player}'s rock crushes {computer_player}'s scissors. {user_player} wins and will go first!")
             return user_player

def play(game, x_player, o_player):
    turn = select_starting_player(user_player_1.name, opponent.name)
    print("Turn variable:", turn)
    print("X_player- value", x_player.name)
    print("Our game will be played on a 3 by 3 board using the following positions.\n")
    standard_board.board_number_indices()  
    print('Commencing game....')
    # Add in option here to play scissor, paper rock to decide who goes first. 
    while game.free_positions():
        if turn == x_player.name:
            position = x_player.get_move(game)
            game.make_move(position, "X")
            print(f"{x_player.name} makes a move to position {position}")
            game.print_board()
            if game.current_winner:
                print("Congratulations!! You won the game!")   
                break
            turn = o_player.name
            continue
        elif turn == o_player.name:
            time.sleep(1)
            position = o_player.get_move(game)
            game.make_move(position, "O") 
            print(f"{o_player.name} makes a move to position {position}")
            game.print_board()
            if game.current_winner:
                print(f"Better luck next time! {o_player.name} won the game this time.")
                break
            turn = x_player.name
            continue 
    else:
        print("It's a tie!") 
    # def make_move(self, player, letter):
    #     position = player.get_move(self)
    #     self.board[position] = letter
    #     print(f"{player.name} makes a move to position {position}")
    #     
    #     if self.winner(position, letter):
    #         self.current_winner = player
         
def select_opponent():
    print("Lots of players are around around today who would love to play Tic-Tac-Toe with you.\n")
    time.sleep(0.8)

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
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣦⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⠟⠋⠉⠀⠀⠀⠀⠉⠑⠢⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣦⡀
⠀⣀⠀⠀⢀⡏⠀⢀⣴⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠇
⣾⣿⣿⣦⣼⡀⠀⢺⣿⣿⡿⠃⠀⠀⠀⠀⣠⣤⣄⠀⠀⠈⡿⠋⠀
⢿⣿⣿⣿⣿⣇⠀⠤⠌⠁⠀⡀⢲⡶⠄⢸⣏⣿⣿⠀⠀⠀⡇⠀⠀
⠈⢿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠈⠉⠓⠂⠀⠙⠛⠛⠠⠀⡸⠁⠀⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⠑⠀⣠⠞⠁⠀⠀⠀
⠀⠀⠀⢸⡏⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⢸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠻⠿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣶⠶⠤⠤⢤⣶⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣿⣿⣿⠏⠀⠀⠀⠈⢿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        print(pyfiglet.figlet_format("Pete the Panda", font = "digital"))        
        return pete_panda
    elif selection == "b":
        print("""
⢀⠔⠊⠉⠑⢄⠀⠀⣀⣀⠤⠤⠤⢀⣀⠀⠀⣀⠔⠋⠉⠒⡄⠀
⡎⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠘⡄
⣧⢢⠀⠀⠀⠀⠀⠀⠀⠀⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣆⡗
⠘⡇⠀⢀⠆⠀⠀⣀⠀⢰⣿⣿⣧⠀⢀⡀⠀⠀⠘⡆⠀⠈⡏⠀
⠀⠑⠤⡜⠀⠀⠈⠋⠀⢸⣿⣿⣿⠀⠈⠃⠀⠀⠀⠸⡤⠜⠀⠀
⠀⠀⠀⣇⠀⠀⠀⠀⠀⠢⣉⢏⣡⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀
⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢨⠃⠀⢀⠀⢀⠔⡆⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡎⠀⠀⠧⠬⢾⠊⠀⠀⢀⡇⠀⠀⠟⢆⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡇⠀⠀⡞⠀⠀⢣⣀⡠⠊⠀⠀⠀⢸⠈⣆⡀⠀⠀
⠀⠀⡠⠒⢸⠀⠀⠀⡇⡠⢤⣯⠅⠀⠀⠀⢀⡴⠃⠀⢸⠘⢤⠀
⠀⢰⠁⠀⢸⠀⠀⠀⣿⠁⠀⠙⡟⠒⠒⠉⠀⠀⠀⠀⠀⡇⡎⠀
⠀⠘⣄⠀⠸⡆⠀⠀⣿⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⢀⠟⠁⠀
⠀⠀⠘⠦⣀⣷⣀⡼⠽⢦⡀⠀⠀⢀⣀⣀⣀⠤⠄⠒⠁⠀⠀⠀
""")
        print(pyfiglet.figlet_format("Katie the Koala", font = "digital")) 
        return katie_koala
    elif selection == "c":
        print("""
                        ___
                     .-'   `'.
                    /         \ 
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\    '     \_.-' ,.--'`     `""`
   ( ,.--'`   ',__ /./;   ;, '.__.'`    __
   _`) )  .---.__.' / |   |\   \__..--""  ""--.,_
  `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
        | |  .' _.-' |  |  \  \  '.               `~---`
         \ \/ .'     \  \   '. '-._)
          \/ /        \  \    `=.__`~-.
          / /\         `) )    / / `"".`
    , _.-'.'\ \        / /    ( (     / /
     `--~`   ) )    .-'.'      '.'.  | (
            (/`    ( (`          ) )  '-;
             `      '-;         (-'
        """)
        print(pyfiglet.figlet_format("Ollie the Octopus", font = "digital")) 
        return ollie_octopus
    else:
        print("""
⠀⠀⠀⠐⢿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠟⠃
⠀⠀⢸⣿⣿⣿⣿⡿⠛⠉⠁⠀⢸⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣾⣿⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⣿⠿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡿⠛⠉⠀⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        print(pyfiglet.figlet_format("Danni the Doplphin", font = "digital")) 
        return danni_dolphin
  

if __name__ == '__main__':
    clearing.clear()
    print("Welcome to ...\n")
    print(pyfiglet.figlet_format("Tic Tac Toe"))
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    player_name = (input("What is your name?: "))
    print("Hello " + player_name.title() + "! So lovely to meet you. That's a great name.\n")
    time.sleep(0.8)
    user_player_1 = UserPlayer('X', player_name)
    pete_panda = EasyComputerPlayer('O', "Pete the Panda")
    katie_koala = EasyComputerPlayer('O', "Katie the Koala")
    ollie_octopus = ExpertComputerPlayer('O', "Ollie the Octopus")
    danni_dolphin = ExpertComputerPlayer('O', "Danni the Dolphin")
    standard_board = TicTacToe()
    while True:
        standard_board.reset_board() 
        opponent = select_opponent()
        print(f"You have selected {opponent.name} as your opponent today.  Good choice.") 
        play(standard_board, user_player_1, opponent)
        play_again = input("Thanks for playing today. Would you like to play again? (yes/no): ")
        if play_again.lower().strip().startswith('y'):
            continue
        else:
            break


    





