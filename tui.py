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
                    print()
                    #  TODO
                case 3:
                    exit = True
                case _:
                    raise ValueError("Incorrect menu option.")
        except ValueError as e:
            print(f"Error: {e}")
            
