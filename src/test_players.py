"""A series of tests run on the players.py file.

Classes:
    TestGetMove- used to test get_move() method of the UserPlayer class.

Functions:
    fake_input(): Patchs input data with a "monkeypatch"

"""
import pytest
from main import UserPlayer, EasyComputerPlayer, TicTacToe
from players import RangeError, OccupiedError


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
