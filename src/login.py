import pandas as pd
from custom_exceptions import PasswordLengthError, PasswordCaseError, PasswordTypeError, ConfirmationError
from custom_exceptions import InvalidUserError

def create_password():
 
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

def get_username():
    username = input("Username: ")
    df1 = pd.read_csv("user_credentials.csv")
    df2 = df1.set_index("username", drop = False)
    if username not in df2.iloc[:, 0]:
        raise InvalidUserError(username)
    return username

def login():
    print("Welcome back. Please enter your log_in credentials.")
    for i in range(3):
        try:
            username = get_username()
            break
        except InvalidUserError as err:
            print(err)
    else:
        print("You seem to be having difficulty remembering your username.")
        return None
    print(f"You entered {username} for your username")
    df1 = pd.read_csv("user_credentials.csv")
    df2 = df1.set_index("username", drop = False)
    stored_password = df2.loc[username,"password"]
    for i in range(3):
        user_password = input("Password: ")
        if user_password == stored_password:
            print(f"Registration successfull! Welcome back to Animal TicTacToe {username}!")
            return username
        print("Incorrect password try again.")
    return None



def register():
    """A function used to register a new user in the system.
    
    Collects a username and password from the user and stores these
    details in a user_credentials.csv file.

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
    print(f"Registration successfull! Welcome to Animal TicTacToe {username}!")
    return {"username": username, "password": password}
    
    