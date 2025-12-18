import auth
from user import User
import game
from graph import q_categories, q_difficulties

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

def valid_input(prompt: str, validator_function, input_char: str|None = ": ") -> str:
    while True:
        user_input = input(prompt+str(input_char))
        try:
            validator_function(user_input)
            return user_input
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

def username_validator(username: str) -> ValueError|None:
    if not username:
        raise ValueError("Username cannot be empty.")
    
def password_validator(password: str) -> ValueError|None:
    if not password:
        raise ValueError("Password cannot be empty")
    if len(password) < 4:
        raise ValueError("Password must be at least 4 characters long.")

def register() -> User:
    username: str = valid_input("Create a username", username_validator) 
    while True:
        try:
            password: str = valid_input("Create a password", password_validator)
            password_check: str = input("Enter your password again: ")
            if password != password_check:
                raise ValueError("Passwords do not match!")
            return auth.register(username, password)
        except ValueError as e:
            print("Error: {e}")
    

def login() -> User|None:
    username: str = input("Enter your username: ") 
    password: str = input("Enter your password: ")
    user = None
    try:
        user = auth.login(username, password)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    return user

def logged_in_menu(user: User):
    exit = False
    while not exit:
        menu: str = f"Hello {user.username}:\n1) View question statistics\n2) List all winners\n3) Play \"Cichna wants to be a millionare\"\n4) Exit\n"
        input_char: str = f"> "
        user_input_raw: str = input(menu+input_char).strip().lower()
        if not user_input_raw.isdigit():
            user_input = -1
        else:
            user_input: int = int(user_input_raw)
        try:
            match user_input:
                case 1:
                    print("View stats")
                    # TODO
                case 2:
                    print("List all winners")
                    #  TODO
                case 3:
                    print(game.launch(user))
                case 4:
                    exit = True
                case _:
                    raise ValueError("Incorrect menu option.")
        except ValueError as e:
            print(f"Error: {e}")

def graph_menu():
    exit = False
    while not exit:
        menu: str = f"View graphs:\n1) Question difficulties\n2) Question categories\n3) Exit\n"
        input_char: str = f"> "
        user_input_raw: str = input(menu+input_char).strip().lower()
        if not user_input_raw.isdigit():
            user_input = -1
        else:
            user_input: int = int(user_input_raw)
        try:
            match user_input:
                case 1:
                    q_difficulties()
                    # TODO
                case 2:
                    q_categories()
                    #  TODO
                case 3:
                    exit = True
                case _:
                    raise ValueError("Incorrect menu option.")
        except ValueError as e:
            print(f"Error: {e}")

def main_menu():
    exit = False
    while not exit:
        menu: str = f"Welcome! Would you like to:\n1) Log-In\n2) Register\n3) View question statistics\n4) Exit\n"
        input_char: str = f"> "
        user_input_raw: str = input(menu+input_char).strip().lower()
        if not user_input_raw.isdigit():
            user_input = -1
        else:
            user_input: int = int(user_input_raw)
        try:
            match user_input:
                case 1:
                    user = login()
                    if user == None:
                        continue
                    print(user)
                    logged_in_menu(user)
                    # TODO
                case 2:
                    user = register()
                    logged_in_menu(user)
                    # TODO
                case 3:
                    graph_menu()
                case 4:
                    exit = True
                case _:
                    raise ValueError("Incorrect menu option.")
        except ValueError as e:
            print(f"Error: {e}")
            
