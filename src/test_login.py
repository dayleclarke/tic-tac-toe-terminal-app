"""A series of tests run on the login.py file.

Classes:
    TestWinner-used to test winner() method of the TicTacToeBoard class.

Functions:
    test_empty_squares()- Tests empty_squares method() of the TicTacToeBoard class.
    test_free_positions()- Tests free_positions method() of the TicTacToeBoard class.
    test_num_empty_squares()- Tests num_empty_squares method() of the TicTacToeBoard class.
"""
import pytest
from login import create_password, get_username
from custom_exceptions import PasswordLengthError, PasswordCaseError, PasswordTypeError
from custom_exceptions import ConfirmationError, InvalidUserError



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

class TestCreatePassword:
    """A class used to test the create_password function."""
    def test_valid_password(self, monkeypatch):
        """Test the function works as expected given a valid password.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,["Password1", "Password1", "Test1", "Test1", "CheckM1", "CheckM1"])
        assert create_password() == "Password1"
        assert create_password() == "Test1"
        assert create_password() == "CheckM1"

    def test_confirm_password(self, monkeypatch):
        """Test the function raises a ConfirmationError when the
        confirmation password provided doesn't match the original
        input.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,["Password1", "Password2", "Test1", "TestM1", "CheckM1", "CheckE1"])
        for i in range(3):
            with pytest.raises(ConfirmationError):
                create_password()

    def test_short_password(self, monkeypatch):
        """Test the function raises a PasswordLengthError when given a
        password with < 5 characters.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,["test", "1234", "p"])
        for i in range(3):
            with pytest.raises(PasswordLengthError):
                create_password()

    def test_long_password(self, monkeypatch):
        """Test the function raises a PasswordLengthError when given a
        password with > 10 characters.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,["testpassword", "12345678910", "longpasswordtest"])
        for i in range(3):
            with pytest.raises(PasswordLengthError):
                create_password()

    def test_password_case(self, monkeypatch):
        """Test the function raises a PasswordCaseError when given a
        password doesn't contain at least one upper case and one lower
        case character.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,["password", "PASSWORD", "123456"])
        for i in range(3):
            with pytest.raises(PasswordCaseError):
                create_password()

    def test_password_type(self, monkeypatch):
        """Test the function raises a PasswordTypeError when given a
        password that doesn't contain at least one number.

        Args:
            monkeypatch: an object imported from within pytest.
        """
        fake_input(monkeypatch,["Password", "Testpass", "Nonumber"])
        for i in range(3):
            with pytest.raises(PasswordTypeError):
                create_password()


class TestGetUserName:
    """A class used to test the get_username function."""
    def test_get_username(self, monkeypatch):
        """Tests the function works as expected when given valid input."""
        fake_input(monkeypatch,["Dayle", "Joanne", "Gillian"])
        assert get_username() == "Dayle"
        assert get_username() == "Joanne"
        assert get_username() == "Gillian"

    def test_check_username(self, monkeypatch):
        """Tests the function raises an InvalidUserError when the
        username provided doesn't exsist in the csv file."""
        fake_input(monkeypatch,["Name No One Would Pick", "Testing Username"])
        for i in range(2):
            with pytest.raises(InvalidUserError):
                get_username()
                