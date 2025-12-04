def main():
    exit = False
    while not exit:
        menu: str = f"Welcome! Would you like to:\n1) Log-In\n2) Register\n3) Exit\n"
        input_char: str = f"> "
        user_input_raw: str = input(menu+input_char).strip().lower()
        if not user_input_raw.isdigit:
            user_input_raw = -1
        user_input: int = int(user_input_raw)
        match user_input:
            case 1:
                print()
                # TODO
            case 2:
                print()
                # TODO
            case 3:
                exit = True
