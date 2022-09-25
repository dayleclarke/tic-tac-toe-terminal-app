import pandas as pd
from custom_exceptions import PasswordLengthError, PasswordCaseError, PasswordTypeError, ConfirmationError
from custom_exceptions import InvalidUserError, IncorrectPasswordError

def create_password():
    """Returns a new password from user input.

    Raises:
        PasswordLengthError: when a password is not the required
            length.
        PasswordCaseError: when a password does not contain at least
            one upper and one lower case character.
        PasswordTypeError: when a password does not contain at least
            one number.
        ConfirmationError: when the confirmation password doesn't match
            the first password provided.
    """
    password = input("Password: ")
    if len(password) not in range(5, 11):
        raise PasswordLengthError()
    contains_uppercase = any(character.isupper() for character in password)
    contains_lowercase = any(character.islower() for character in password)
    contains_int = any(character.isdigit() for character in password)
    if not contains_uppercase or not contains_lowercase:
        raise PasswordCaseError()
    if not contains_int:
        raise PasswordTypeError()
    confirm_password = input("Confirm password: ")
    if password != confirm_password:
        raise ConfirmationError()

    return password


def register():
    """A function used to register a new user in the system.

    Collects a username and password from user input. These are then
    stored in a user_credentials.csv file and returned as a dictionary.

    Exceptions:
        PasswordLengthError: when a password is not the required
            length.
        PasswordCaseError: when a password does not contain at least
            one upper and one lower case character.
        PasswordTypeError: when a password does not contain at least
            one number.
        ConfirmationError: when the confirmation password doesn't match
            the first password provided.

    Returns:
        dict: storing the user's username and password with their
            associated values.
    """
    while True:
        username= input("Username: ")
        df1 = pd.read_csv("user_credentials.csv")
        df2 = df1.set_index("username", drop = False)
        if username in df2.iloc[:, 0]:
            print("That username is already taken.  Please choose a unique username.")
            continue
        print(f"You entered {username} for your username.\n")
        break

    print("""Enter a password to associate with your account.

Passwords must:
1) be between 5 and 10 characters in length.
2) contain at least one number 
3) contain one uppercase and one lowercase letter.
""")
    while True:
        try:
            password= create_password()
            break
        except PasswordLengthError as err:
            print(err)
        except PasswordCaseError as err:
            print(err)
        except PasswordTypeError as err:
            print(err)
        except ConfirmationError as err:
            print(err)
    df1 = pd.read_csv("user_credentials.csv")
    df1.loc[len(df1)]=[username, password]
    df1.to_csv("user_credentials.csv", index=False)
    print(f"Registration successfull! Welcome to Animal TicTacToe {username}!\n")
    return {"username": username, "password": password}


def get_username():
    """Collects and returns username from user input.

    Checks that the username exsits in the user_credentials dataframe.
    If is does the username is returned otherwise an InvalidUserError
    is raised.

    Raises:
        InvalidUserError: when the provided username does not exsist in
        the user_credentials dataframe.

    Returns:
        str: the users username collect from input
    """
    username = input("Username: ")
    df1 = pd.read_csv("user_credentials.csv")
    df2 = df1.set_index("username", drop = False)
    if username not in df2.iloc[:, 0]:
        raise InvalidUserError(username)
    return username

def match_password(username):
    """Collects the user's password though user input and matches
    this password with their records in the user_credentials.csv file.
    Returns their password if valid.

    Args:
        username (str): the username associated with the user.

    Raises:
        IncorrectPasswordError: when the password the user enters doesn't match
    the user_credentials.csv dataframe

    Returns:
        str: the user's password.
    """
    df1 = pd.read_csv("user_credentials.csv")
    df2 = df1.set_index("username", drop = False)
    stored_password = df2.loc[username,"password"]
    user_password = input("Password: ")
    if user_password != stored_password:
        raise IncorrectPasswordError()
    return user_password

def login():
    """A function used to log an exsisting user into the system.

    Exceptions: InvalidUserError: when the provided username does not exsist in
        the user_credentials dataframe.

    Returns:
        NoneType: None if the user is unable to remember their username
        or password within three attempts.
        dict: storing the user's username and password with their
            associated values.
    """
    print("Welcome back. Please enter your log_in credentials.")
    for i in range(3):
        try:
            username = get_username()
            break
        except InvalidUserError as err:
            print(err)
    else:
        print("You seem to be having difficulty remembering your username.\n")
        return None
    
    for i in range(3):
        try:
            password = match_password(username)
            break
        except IncorrectPasswordError as err:
            print(err) 
    else:
        print("You seem to be having difficulty remembering your password.\n")
        return None   
    print(f"Registration successfull! Welcome back to Animal TicTacToe {username}!\n")
    return {"username": username, "password": password}
