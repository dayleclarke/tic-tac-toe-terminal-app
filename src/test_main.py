"""A series of tests run on the main.py file.

Classes:
    TestWinner-used to test winner() method of the TicTacToeBoard class.

Functions:
    test_empty_squares()- Tests empty_squares method() of the TicTacToeBoard class.
    test_free_positions()- Tests free_positions method() of the TicTacToeBoard class.
    test_num_empty_squares()- Tests num_empty_squares method() of the TicTacToeBoard class.
"""
import pytest
from main import UserPlayer, EasyComputerPlayer, TicTacToeBoard

user_player_1 = UserPlayer("X", "Dayle")
pete_panda = EasyComputerPlayer("O", "Pete the Panda")
standard_board = TicTacToeBoard()

class TestWinner:
    """A class used to test winner() method of the TicTacToeBoard class."""

    def test_winner_diagonal(self):
        """Test method's ability to identify a diagonal win.

        Tests whether the method correctly identifies a winner when a
        player's letter (either "X" or "O") occupies 3 in a row along
        a diagonal (either [0, 4 and 8] or [2, 4, 6]).
        Different simulated board positions are provided for this test.
        """
        standard_board.board = ["O", " ", "X", " ", "X", " ", "X", " ", "O"]
        assert standard_board.winner(4, "X") is True
        standard_board.board = ["O", " ", "", " ", "O", " ", "X", " ", "O"]
        assert standard_board.winner(2, "X") is False
        standard_board.board = ["O", " ", "X", " ", "O", " ", "X", " ", "O"]
        assert standard_board.winner(4, "O") is True
        standard_board.board = [" ", "X", "X", " ", "O", " ", "X", " ", "O"]
        assert standard_board.winner(0, "O") is False

    def test_winner_rows(self):
        """Test method's ability to identify a horizontal win.

        Tests whether the method correctly identifies a winner when a
        player's letter (either "X" or "O") occupies 3 in a row along
        a horizontal row [0, 1, 2] [3, 4, 5] or [6, 7, 8]. Different
        simulated board positions are provided for this test.
        """
        standard_board.board = ["X", "X", "X", " ", "O", " ", " ", " ", "O"]
        assert standard_board.winner(1, "X") is True
        standard_board.board = ["X", " ", "X", " ", "O", " ", "X", " ", "O"]
        assert standard_board.winner(1, "X") is False
        standard_board.board = ["X", " ", "X", "O", "O", "O", " ", " ", "X"]
        assert standard_board.winner(3, "O") is True
        standard_board.board = ["X", " ", "X", "O", "X", "O", " ", "O", "X"]
        assert standard_board.winner(3, "O") is False

    def test_winner_columns(self):
        """Test method's ability to identify a vertical win.

        Tests whether the method correctly identifies a winner when a
        player's letter (either "X" or "O") occupies 3 in a row along
        a vertical column [0, 3, 6] [1, 4, 7] or [2, 5, 8]. Different
        simulated board positions are provided for this test.
        """
        standard_board.board = ["X", " ", " ", "X", "O", " ", "X", " ", "O"]
        assert standard_board.winner(0, "X") is True
        standard_board.board = ["O", " ", " ", "X", "O", " ", "X", " ", "O"]
        assert standard_board.winner(0, "X") is False
        standard_board.board = ["X", "O", " ", "X", "O", " ", " ", "O", "X"]
        assert standard_board.winner(1, "O") is True
        standard_board.board = ["X", "O", " ", "X", "X", " ", "O", "O", "X"]
        assert standard_board.winner(1, "O") is False

def test_empty_squares():
    """Used to test empty_squares method() of the TicTacToeBoard class."""
    standard_board.board = ["X", " ", " ", "X", "O", " ", "X", " ", "O"]
    assert standard_board.empty_squares() is True
    standard_board.board = ["X", "X", "O ", "X", "O", "O", "X", "O", "O"]
    assert standard_board.empty_squares() is False

def test_free_positions():
    """Used to test free_positions method() of the TicTacToeBoard class.

    Different simulated board positions are provided for this test to
    ensure it returns the index position of any free positions
    (indicated by an " " on the board)
    """
    standard_board.board = ["X", " ", " ", "X", "O", " ", "X", " ", "O"]
    assert standard_board.free_positions() == [1, 2, 5, 7]
    standard_board.board = [" ", " ", "O ", "X", "O", "O", "X", "O", " "]
    assert standard_board.free_positions() == [0, 1, 8]
    standard_board.board = ["X", "X", "O ", "X", "O", "O", "X", "O", "O"]
    assert standard_board.free_positions() == []

def test_num_empty_squares():
    """Used to test num_empty_squares method() of the TicTacToeBoard class.

    Different simulated board positions are provided for this test to
    ensure it returns the total number of free positions remaining on
    the board ("free positions" are indicated by an " ").
    """
    standard_board.board = ["X", " ", " ", "X", "O", " ", "X", " ", "O"]
    assert standard_board.num_empty_squares() == 4
    standard_board.board = ["X", " ", "O ", "X", "O", "O", "X", "O", " "]
    assert standard_board.num_empty_squares() == 2
    standard_board.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    assert standard_board.num_empty_squares() == 9
    standard_board.board = ["X", "O", "O", "X", "O", "X", "X", "O", "X"]
    assert standard_board.num_empty_squares() == 0

def test_board_number_indices(capsys):
    standard_board.board_number_indices()
    stdout, stderr = capsys.readouterr()
    assert stdout == '-------------\n| 0 | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |\n-------------\n\n'