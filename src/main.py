from random import choice
import time
import pandas as pd
import pyfiglet
from simple_term_menu import TerminalMenu
import clearing
from players import UserPlayer, EasyComputerPlayer, ExpertComputerPlayer
from custom_exceptions import RangeError, OccupiedError, ConfirmationError
from custom_exceptions import PasswordLengthError, PasswordCaseError, PasswordTypeError
from custom_exceptions import InvalidUserError
from login import register,login


class TicTacToeBoard:
    """A class used to represent a 3x3 TicTactoe board

    Attributes:
        board(list): A list to represent the 9 positions of the board.
        current_winner (bool or str): False if there is no current
            winner or the letter belonging to the current winner if
            there is one.
    """
    def __init__(self):
        # Creates a "board" which is a list containing 9 " " strings
        self.board = [" " for i in range(9)]
        # Keeps track of the winner which starts out as None.
        self.current_winner = None

    @staticmethod
    def board_number_indices():
        """Visualisation of board with number indices.

        A visualisation printed to the terminal showing the 3x3 board
        which shows which number each position corresponds to.
        """
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print("-------------")
        for row in number_board:
            print("| " + " | ".join(row) + " |")
        print("-------------\n")

    def print_board(self):
        """Visualisation of the 3X3 board showing where letters have
        been placed and where free spaces remain.
        """
        print("-------------")
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
        print("-------------")

    def free_positions(self):
        """List comprehension which returns all the number indices of
        all free spots available on the board.

        Returns:
            list: the number indices of all " " positions on the board.
        """
        return [i for i, position in enumerate(self.board) if position == " "]

    def empty_squares(self):
        """This method returns True if empty spaces remain on the
        board. It will return False otherwise.

        Returns:
            bool: True if a " " string item remains in the board. False
                otherwise.
        """
        return " " in self.board

    def num_empty_squares(self):
        """This method returns the number of empty spaces remaining on
        the board.

        Returns:
            int: The number of " " string items remaining on the board.
        """
        return self.board.count(" ")

    def make_move(self, position, letter):
        """A method to place a player's letter onto the board.

        Args:
            position (int): the position (between 0-8) on the board to
            place the letter.
            letter (str): "X" or "O" depending on whose turn it is.
        """
        if self.board[position] == " ":
            self.board[position] = letter
            if self.winner(position, letter):
                self.current_winner = letter


    def winner(self, position, letter):
        """A method that checks to see if the last move made
        created a winner.

        It will analyse the current state of the board at the provided
        position to see if the last player's letter appears 3 times in
        a row either horizontally, vertically or diagonally.

        Limitations: Must be called after the player has made their move.
        It accesses the win state based on the position provided.
        But both diagonals of the board are checked. Returns True if
        there is a winner but doesn't return or print which player is
        the winner.

        Args:
            position (int): the position (between 0-8) on the board
                that was last played.
            letter (str): "X" or "O" depending on which player last
                made a move.

        Returns:
            bool: True if there is a current winner, False otherwise.
        """
        # Analysing the row at the position last played
        # The number of times the position index is divisable by 3
        # indicates it's row index (either 0, 1 or 2).
        row_index = (position // 3)
        # This selects the entire row that the position is in.
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        # If the letter is in all of the squares on this row
        # then there is a winner.
        if all(square == letter for square in row):
            return True
        # Analysing the column at the position last played
        # Position modulus 3 will indicate its column index
        # (either 0, 1 or 2).
        col_index = (position % 3)
          # This selects the entire column that the position is in.
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all(square == letter for square in column):
            return True
        # Analysing both diagonal positions (0, 4, 8) and (2, 4, 6).
        diagonal1 = [self.board[i] for i in [0, 4, 8]]
        if all(square == letter for square in diagonal1):
            return True
        diagonal2 = [self.board[i] for i in [2, 4, 6]]
        if all(square == letter for square in diagonal2):
            return True
        # If all checks fail there is no winner return False
        return False

    def reset_board(self):
        """Resets the board to all blank squares with no winner.

        Replaces the "board" to the original list of " " strings.
        Returns the current winner to None.
        """
        self.board = [" " for i in range(9)]
        self.current_winner = None


def select_opponent():
    """Collects user input and returns the opponent they have selected
    to play against."""
    print(
"""Lots of players are around today who would love to play Tic-Tac-Toe with you.
They each have different skill levels and experience.
Here is a table outlining info about each player including their win, tie, and loss history:\n
"""
        )
    time.sleep(0.8)
    df = pd.read_csv("player_scores.csv")
    pd.options.display.float_format = "{:.2%}".format
    print(df,"\n")
    print(
        "To help select the correct player for you, what difficulty level would you like"
        " to play on? \nMenu entries can be selected with the arrow or j/k keys.\n"
        )
    difficulty_options = ["Easy Mode", "Expert Mode"]
    difficulty_terminal_menu = TerminalMenu(difficulty_options, title="Game difficulty level:")
    difficulty_entry_index = difficulty_terminal_menu.show()
    user_difficulty = difficulty_options[difficulty_entry_index]
    print(f"You have chosen to play on {user_difficulty}.")
    time.sleep(0.8)

    if user_difficulty == "Easy Mode":
        print("There are two players who I recommend you challenge to a game.\n")
        print(
            f"Firstly there is the {df.at[0,'personality']} {df.at[0,'player_name']}. "
            f"He has won {df.at[0,'wins']} games out of {df.at[0,'total_games']} and"
            " has still not discovered a reliable strategy to win.\n"
            )
        print(
            f"Secondly there is {df.at[1,'player_name']}. "
            f"She is {df.at[0,'personality']} but is too busy eating "
            "eucalyptus leaves to focus long enough to consistently win. "
            f"She has won {df.at[0,'wins']} games out of {df.at[0,'total_games']}.\n"
            )
        print(
            "You can select any player you like but if you wish to play on easy "
            "mode those are the two I recommend.\n"
            )
    elif user_difficulty == "Expert Mode":
        print("There are two players I recommend you challenge to a game.\n")
        print(
            f"Firstly there is the {df.at[2,'personality']} {df.at[2,'player_name']}. "
            "He is currently undefeated having never lost a game. He has won "
            f"{df.at[0,'wins']} games out of {df.at[0,'total_games']}."
            )
        print(
            f"Secondly there is {df.at[1,'player_name']}. "
            f"She is {df.at[0,'personality']} and also remains undefeated. "
            f"She has won {df.at[0,'wins']} games out of {df.at[0,'total_games']}.\n"
            )
        print(
            "You can select any player that you like but if you wish to play on expert "
            "mode those are the two I recommend to appropriately test your abilities.\n"
            )

    opponent_options = [
        "Pete the Panda (easy mode)",
        "Katie the Koala (easy mode)",
        "Ollie the Octopus (expert mode)",
        "Danni the Dolphin (expert mode)",
        ]
    print("Menu entries can be selected with the arrow or j/k keys.\n")
    opponent_terminal_menu = TerminalMenu(
            opponent_options, title = "Which character would you like to play with today?:"
            )
    opponent_entry_index = opponent_terminal_menu.show()
    opponent_player = opponent_options[opponent_entry_index]
    opponent_player = opponent_player.split()[0]

    if opponent_player == "Pete":
        print(
            """⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
        )
        print(pyfiglet.figlet_format("Pete the Panda", font="digital"))
        return pete_panda
    if opponent_player == "Katie":
        print(
            """
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
"""
        )
        print(pyfiglet.figlet_format("Katie the Koala", font="digital"))
        return katie_koala
    if opponent_player == "Ollie":
        print("""
                        ___
                     .-'   `'.
                    /         \\ 
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\\    '     \\_.-' ,.--'`     `""`
   ( ,.--'`   ',__ /./;   ;, '.__.'`    __
   _`) )  .---.__.' / |   |\\   \\__..--""  ""--.,_
  `---' .'.''-._.-'`_./  /\\ '.  \\ _.-~~~````~~~-._`-.__.'
        | |  .' _.-' |  |  \\  \\  '.               `~---`
         \\ \\/ .'     \\  \\   '. '-._)
          \\/ /        \\  \\    `=.__`~-.
          / /\\         `) )    / / `"".`
    , _.-'.'\\ \\        / /    ( (     / /
     `--~`   ) )    .-'.'      '.'.  | (
            (/`    ( (`          ) )  '-;
             `      '-;         (-'
        """
        )
        print(pyfiglet.figlet_format("Ollie the Octopus", font="digital"))
        return ollie_octopus
    print(
            """
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
⡿⠛⠉⠀⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
        )
    print(pyfiglet.figlet_format("Danni the Doplphin", font="digital"))
    return danni_dolphin

def select_starting_player(user_player, computer_player):
    """Returns the starting player

    A function used to determine the starting player based on the
    outcome of a scissors-paper-rock game.

    Args:
        user_player: an instance of the HumanPlayer class.
        computer_player: an instance of the Player class
            based on the opponent previously selected by the user.

    Returns:
        the starting player which will either be the user player or the
            computer player depending on who won scissors-paper-rock.
    """
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
""",
}
    print("We will begin by playing scissors-paper-rock to determine which player will start.")
    while True:
        print("Menu entries can be selected with the arrow or j/k keys.")
        gesture_options = list(hand_gestures.keys())
        gesture_terminal_menu = TerminalMenu(
            gesture_options,
            title="Please select one of the following hand gestures:")
        gesture_entry_index = gesture_terminal_menu.show()
        user_choice = gesture_options[gesture_entry_index]
        print(hand_gestures[user_choice])
        print(f"{user_player} has chosen to play {user_choice}.")
        time.sleep(0.8)
        opponent_choice = choice(list(hand_gestures.keys()))
        time.sleep(0.8)
        print(hand_gestures[opponent_choice])
        print(f"{computer_player} has chosen to play {opponent_choice}.")
        time.sleep(0.8)
        if user_choice == opponent_choice:
            print(pyfiglet.figlet_format("Draw!"))
            print(
                f"Great minds think alike! You both selected {user_choice}. Please select again."
            )
            continue
        break

    if user_choice == "paper":
        if opponent_choice == "scissors":
            print(pyfiglet.figlet_format("Defeat!"))
            print(
                f"{computer_player}'s scissors cuts {user_player}'s paper. "
                f"{computer_player} wins and will go first!"
                )
            return computer_player
        print(pyfiglet.figlet_format("You Win!"))
        print(
            f"{user_player}'s paper covers {computer_player}'s scissors. "
            f"{user_player} wins and will go first!"
            )
        return user_player

    if user_choice == "scissors":
        if opponent_choice == "paper":
            print(pyfiglet.figlet_format("You Win!"))
            print(
                f"{user_player}'s scissors cuts {computer_player}'s paper. "
                f"{user_player} wins and will go first!"
                )
            return user_player
        print(pyfiglet.figlet_format("Defeat!"))
        print(
            f"{computer_player}'s rock crushes {user_player}'s scissors. "
            f"{computer_player} wins and will go first!"
            )
        return computer_player

    if user_choice == "rock":
        if opponent_choice == "paper":
            print(pyfiglet.figlet_format("Defeat!"))
            print(
                f"{computer_player}'s paper covers {user_player}'s rock. "
                f"{computer_player} wins and will go first!"
                )
            return computer_player
        print(pyfiglet.figlet_format("Victory!"))
        print(
            f"{user_player}'s rock crushes {computer_player}'s scissors. "
            f"{user_player} wins and will go first!"
            )
        return user_player


def play(game, x_player, o_player):
    """A function used to play one complete game of TicTacToe.

    This function calls the select_starting_player() function to
    determine which player will start the game. While there are free
    positions left on the board players will alternate turns (by
    invoking the make_move() method of each player) and placing
    their marker in one of the 9 positions on the board. The game will
    continue in this way until a player places 3 markers in a row
    horizontally, vertically or diagonally or the board fills up.
    The win status is checked in the make_method() after each player
    places their marker. Instructions are printed to the terminal to
    guide the user how to place the game.

    At the end of the game the outcome is printed to the terminal and
    both player's score history is updated in a seperate player_scores
    csv file.

    Args:
        game: an instance of the TicTacToeBoard class.
        x_player: an instance of the HumanPlayer class.
        o_player: an instance of the Player class.
            based on the opponent previously selected by the user.
    """
    turn = select_starting_player(user_player_1.name, opponent.name)
    print("Our game will be played on a 3 by 3 board using the following positions.\n")
    standard_board.board_number_indices()
    print("Commencing game....")
    while game.free_positions():
        if turn == x_player.name:
            while True:
                try:
                    position = x_player.get_move(game)
                    break
                except RangeError as err:
                    print(err)
                except OccupiedError as err:
                    print(err)
                except ValueError:
                    print("That isn't a valid integer. Please enter a number with no decimal places.")
            game.make_move(position, "X")
            print(f"{x_player.name} makes a move to position {position}")
            game.print_board()
            if game.current_winner:
                print("Congratulations!!!")
                print(pyfiglet.figlet_format("You Win!"))
                print(
                    """
                                   .''.
       .''.      .        *''*    :_\\/_:     .
      :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .'.:.'.
  .''.: /\\ :   ./)\\   ':'* /\\ * :  '..'.  -=:o:=-
 :_\\/_:'.:::.    ' *''*    * '.\'/.' _\\(/_'.':'.'
 : /\\ : :::::     *_\\/_*     -= o =-  /)\\    '  *
  '..'  ':::'     * /\\ *     .'/.\\'.   '
      *            *..*         :
        *
        """)
                print(o_player.update_scores("losses"))
                break
            turn = o_player.name
            continue
        if turn == o_player.name:
            time.sleep(1)
            position = o_player.get_move(game)
            game.make_move(position, "O")
            print(f"{o_player.name} makes a move to position {position}")
            game.print_board()
            if game.current_winner:
                print(f"Better luck next time! {o_player.name} won the game this time.")
                print(o_player.update_scores("wins"))
                break
            turn = x_player.name
            continue
    else:
        print("It's a tie!")
        print(o_player.update_scores("ties"))



if __name__ == "__main__":
    clearing.clear()
    pete_panda = EasyComputerPlayer("O", "Pete the Panda")
    katie_koala = EasyComputerPlayer("O", "Katie the Koala")
    ollie_octopus = ExpertComputerPlayer("O", "Ollie the Octopus")
    danni_dolphin = ExpertComputerPlayer("O", "Danni the Dolphin")
    standard_board = TicTacToeBoard()
    print("Welcome to ...\n")
    print(pyfiglet.figlet_format("Tic Tac Toe"))
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    
    print("How would you like to begin today?")
    print("Menu entries can be selected with the arrow or j/k keys.\n")
    while True:
        login_options = [
                        "Register as a new user",
                        "Login as an exsiting user",
                        "Play as a guest (no log-in required)",
                        ]
        terminal_login_menu = TerminalMenu(login_options)
        menu_entry_index = terminal_login_menu.show()
        log_in_choice = login_options[menu_entry_index]
        print(log_in_choice)
        if log_in_choice == "Register as a new user":
            register()
        elif log_in_choice == "Login as an exsiting user":
            login = login()
            if login is None:
                continue
                

    while True:
        player_name = input("What is your first name?: ")
        print(
            "Hello "
            + player_name.title()
            + "! So lovely to meet you. That's a great name. "
            "Can you please confirm I have your name spelt correctly? "
            "Menu entries can be selected with the arrow or j/k keys.\n"
            )
        user_options = [f"Yes, my name is {player_name.title()}",
                        "No, I wish to enter my name again."]
        terminal_menu = TerminalMenu(user_options)
        menu_entry_index = terminal_menu.show()
        name_confirmation = user_options[menu_entry_index]
        if name_confirmation == "No, I wish to enter my name again.":
            continue
        break
    print("Thank you for confirming that for me. I would hate to call you by the wrong name.")
    time.sleep(0.8)
    user_player_1 = UserPlayer("X", player_name)

    while True:
        standard_board.reset_board()  # Resets the board to commence a new game
        opponent = select_opponent()  # User selects difficulty level and choses an
        print(
            f"You have selected {opponent.name} as your opponent today.  Good choice."
        )
        play(standard_board, user_player_1, opponent)
        play_again = input(
            "Thanks for playing today. Would you like to play again? (yes/no): "
        )
        if play_again.lower().strip().startswith("y"):
            continue
        break




