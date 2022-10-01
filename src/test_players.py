"""A series of tests run on the players.py file.

Classes:
    TestGetMoveUser- used to test get_move() method of the UserPlayer class.

Functions:
    fake_input(): Patchs input data with a "monkeypatch"

"""
import pytest
from main import UserPlayer, ExpertComputerPlayer, TicTacToeBoard
from players import RangeError, OccupiedError


user_player_1 = UserPlayer("X", "Dayle", "Dayle01")
ollie_octopus = ExpertComputerPlayer("O", "Ollie the Octopus")
standard_board = TicTacToeBoard()

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


class TestGetMoveUser:
    """A class used to test get_move() method of the UserPlayer class."""

    def test_get_move(self, monkeypatch):
        """Tests the method works as expected when given valid input.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,[1, 5, 9])
        assert user_player_1.get_move(standard_board) == 0 # One is subtracted form each.
        assert user_player_1.get_move(standard_board) == 4
        assert user_player_1.get_move(standard_board) == 8

    def test_above_range(self, monkeypatch):
        """Test the method raises a RangeError when given input < 1.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,[0, -1, -20])
        for i in range(3):
            with pytest.raises(RangeError):
                user_player_1.get_move(standard_board)

    def test_below_range(self, monkeypatch):
        """Test the method raises a RangeError when given input > 9.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,[10, 20, 50])
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

        A simulated board position is provided for this test

        Args:
            monkeypatch: an object imported from within pytest.
        """
        standard_board.board = ["O", " ", "X", " ", "X", " ", "X", " ", "O"]
        fake_input(monkeypatch,[1, 3, 5])
        with pytest.raises(OccupiedError):
            user_player_1.get_move(standard_board)

class TestGetMoveExpertComp:
    """A class used to test get_move() method of the
    ExpertComputerPlayer.

    """
    def test_take_obvious_win(self):
        """Test player takes the winning position when possible.

        This tests that the method returns the position on the board
        which would allow the player to win when it is possible to do
        so. Checks a horizontal, vertical and diagonal win. It also
        tests that the player takes a win before blocking a postential
        loss.
        """
        standard_board.board = ["O", " ", " ", " ", "X", " ", "O", " ", "X"]
        # With an "O" in position 0 and 6 the player will win if they
        # place their marker at position 3.
        assert ollie_octopus.get_move(standard_board) == 3
        standard_board.board = [" ", "O", "O", " ", "X", " ", " ", " ", "X"]
        # With an "O" in position 1 and 2 the player will win if they
        # place their marker at position 0.
        assert ollie_octopus.get_move(standard_board) == 0
        standard_board.board = ["X", " ", " ", "X", "O", " ", "O", " ", "X"]
        # With an "O" in position 1 and 2 the player will win if they
        # place their marker at position 0.
        assert ollie_octopus.get_move(standard_board) == 2
        standard_board.board = ["O", " ", " ", "X", "X", " ", " ", "O", "O"]
        # With an "O" in position 7 and 8 the player will win if they
        # place their marker at position 6. It is important to take
        # this win before blocking the opponents win (at position 5).
        assert ollie_octopus.get_move(standard_board) == 6
    
    def test_block_obvious_loss(self):
        """Test player takes the position to block the other player
        winning.

        This tests that the method returns the position on the board
        which would allow the player to block their opponent from
        winning.
        """
        standard_board.board = ["O", "X", " ", " ", "X", " ", " ", " ", "O"]
        # With an "X" in position 1 and 4 the player needs to block their
        # opponent's win by placing their marker at position 7.
        assert ollie_octopus.get_move(standard_board) == 7
        standard_board.board = ["O", " ", " ", "X", "X", " ", " ", " ", "O"]
        # With an "X" in position 3 and 4 the player needs to block their
        # opponent's win by placing their marker at position 5.
        assert ollie_octopus.get_move(standard_board) == 5
        standard_board.board = ["X", " ", "O", "O", "X", " ", " ", " ", " "]
        # With an "X" in position 0 and 4 the player needs to block their
        # opponent's win by placing their marker at position 8.
        assert ollie_octopus.get_move(standard_board) == 8
