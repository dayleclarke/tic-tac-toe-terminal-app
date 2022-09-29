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

    def __repr__(self):
        return f"""An instance of the TicTacToe class.

The board currently has the following markers placed: {self.board}. 

The winner is currently set to {self.current_winner}.
"""

    def __str__(self):
        return "This refers to the 3x3 TicTacToe board."

    @staticmethod
    def board_number_indices():
        """Visualisation of board with number indices.

        A visualisation printed to the terminal showing the 3x3 board
        which shows which number each position corresponds to.
        """
        # number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        number_board = [[str(i + 1) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
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
