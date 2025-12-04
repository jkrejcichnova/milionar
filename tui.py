import auth
from user import User
def menu_boilerplate():
    exit = False
    while not exit:
        menu: str = f"TITLE:\n1) Option\n2) Option\n3) Exit\n"
        input_char: str = f"> "
        user_input_raw: str = input(menu+input_char).strip().lower()
        if not user_input_raw.isdigit():
            user_input = -1
        else:
            user_input: int = int(user_input_raw)
        try:
            match user_input:
                case 1:
                    print()
                    # TODO
                case 2:
                    print()
                    #  TODO
                case 3:
                    exit = True
                case _:
                    raise ValueError("Incorrect menu option.")
        except ValueError as e:
            print(f"Error: {e}")

def register() -> User:
    # TODO! create a reusable valid input helper
    username: str = input("Create a username: ")
    password_ok = False
    valid_password: str = "" 
    while not password_ok:
        password: str = input("Create a password: ")
        if len(password) < 4:
            print("Error: Password must be at least 4 characters long.\n")
            continue  
        password_check: str = input("Enter your password again: ")
        if password == password_check:
            valid_password = password
            password_ok = True
        else:
            print("Error: Passwords do not match. Please try again.\n")
    return auth.register(username, valid_password)


def main():
    exit = False
    while not exit:
        menu: str = f"Welcome! Would you like to:\n1) Log-In\n2) Register\n3) Exit\n"
        input_char: str = f"> "
        user_input_raw: str = input(menu+input_char).strip().lower()
        if not user_input_raw.isdigit():
            user_input = -1
        else:
            user_input: int = int(user_input_raw)
        try:
            match user_input:
                case 1:
                    print()
                    # TODO
                case 2:
                    user = register()
                    # TODO
                case 3:
                    exit = True
                case _:
                    raise ValueError("Incorrect menu option.")
        except ValueError as e:
            print(f"Error: {e}")
            
