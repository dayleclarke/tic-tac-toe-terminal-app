from main import UserPlayer, EasyComputerPlayer, TicTacToe, select_starting_player
from players import RangeError, OccupiedError
import pytest 


user_player_1 = UserPlayer("X", "Dayle")
pete_panda = EasyComputerPlayer("O", "Pete the Panda")
standard_board = TicTacToe()

def fake_input(monkeypatch, user_input):
    """Patchs input data with a "monkeypatch" (fake inputs).

    This allows dynamic (run-time) modiciations of the program. It
    allows the test to mock user inputs and test them one at at
    time.

    Args:
        monkeypatch: an object imported from within pytest.
        user_input(list): user input to be added one at a time. This
        replaces user input with mock data.
    """
    test_inputs = iter(user_input)
    monkeypatch.setattr("builtins.input", lambda prompt: next(test_inputs))


class TestGetMove:
    """A class used to test get_move() method of the UserPlayer class."""

    def test_get_move(self, monkeypatch):
        """Tests the method works as expected when given valid input.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,[0, 5, 8])
        assert user_player_1.get_move(standard_board) == 0
        assert user_player_1.get_move(standard_board) == 5
        assert user_player_1.get_move(standard_board) == 8

    def test_above_range(self, monkeypatch):
        """Test the method raises a RangeError when given input < 0.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,[-1, -20, -50])
        for i in range(3):
            with pytest.raises(RangeError):
                user_player_1.get_move(standard_board)

    def test_below_range(self, monkeypatch):
        """Test the method raises a RangeError when given input > 8.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,[9, 20, 50])
        for i in range(3):
            with pytest.raises(RangeError):
                user_player_1.get_move(standard_board)

    def test_type_conversion(self, monkeypatch):
        """Test method raises a ValueError when input cannot be
        converted to an integer.

        Writing out numbers in long hand or floats entered into user
        input (as it is entered as a string) are not able to be converted
        into an integer. This should raise a ValueError.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,["three", "five", "-0.5", "1.5"])
        with pytest.raises(ValueError):
            user_player_1.get_move(standard_board)

    def test_occupied_error(self, monkeypatch):
        """Test the method raises an OccupiedError when position is already
        occupied on the board.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        standard_board.board = ["O", " ", "X", " ", "X", " ", "X", " ", "O"]
        fake_input(monkeypatch,[0, 2, 4])
        with pytest.raises(OccupiedError):
            user_player_1.get_move(standard_board)


class TestWinner:
    """A class used to test winner() method of the TicTacToe class."""

    def test_winner_diagonal(self):
        """Test method's ability to identify a diagonal win.

        Tests whether the method correctly identifies a winner when a
        player's letter (either "X" or "O") occupies 3 in a row along
        a diagonal (either [0, 4 and 8] or [2, 4, 6]).
        Different simulated board positions are provided for this test.
        """
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
    """Used to test empty_squares method() of the TicTacToe class."""
    standard_board.board = ["X", " ", " ", "X", "O", " ", "X", " ", "O"]
    assert standard_board.empty_squares() is True
    standard_board.board = ["X", "X", "O ", "X", "O", "O", "X", "O", "O"]
    assert standard_board.empty_squares() is False

def test_free_positions():
    """Used to test free_positions method() of the TicTacToe class.

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
    """Used to test num_empty_squares method() of the TicTacToe class.

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
