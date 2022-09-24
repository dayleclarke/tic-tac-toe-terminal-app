class RangeError(Exception):
    """An error raised when an integer is outside of the valid range."""
    def __init__(self, val):
        super().__init__(
            f"{val} is not a valid position on the board. The number must be between 0 and 8.")


class OccupiedError(Exception):
    """An error raised when a player enters a number that is already
    occupied on the board.
    """
    def __init__(self, val):
        super().__init__(
            f"Position {val} is already occupied on the board. Please try again.")


class PasswordLengthError(Exception):
    """An error raised when a password is not the required length."""
    def __init__(self):
        super().__init__(
            "That is not a valid password length. Please enter a password "
            "that contains between 5 and 10 characters (inclusive)."
            )


class PasswordCaseError(Exception):
    """An error raised when a password does not contain at least one
    capital letter.
    """
    def __init__(self):
        super().__init__(
            "That is not a valid password. Please ensure your password "
            "contains at least one upper and one lower case character."
            )


class PasswordTypeError(Exception):
    """An error raised when a password does not contain at least one
    number.
    """
    def __init__(self):
        super().__init__(
            "That is not a valid password. Please ensure your password "
            "contains at least one number."
            )


class ConfirmationError(Exception):
    """An error raised when the confirmation password doesn't match the
    original password provided.
    """
    def __init__(self):
        super().__init__("The passwords entered do not match. Please try again.")
