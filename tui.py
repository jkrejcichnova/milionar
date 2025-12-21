import re
from typing import Any, Optional
import auth
from user import User
import game
from game_database import get_results
from graph import q_categories, q_difficulties
from result import UserResults, GlobalResults
from user_database import get_database

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

def get_output_lengths(l: list[Any]) -> list[int]:
    list_str: list[int] = []
    for i in l:
        list_str.append(len(str(i)))
    return list_str
      

def output_dict_as_table(d: dict, title: str | None = None, headers: tuple[str,str] | None = None) -> str:
    output = ""
    keys: list[Any] = list(d.keys())
    keys.append(0)
    values: list[Any] = list(d.values())
    values.append(0)
    width_col1 = max(get_output_lengths(keys))
    width_col2 = max(get_output_lengths(values))
    if headers != None:
        width_col1 = max([width_col1, len(headers[0])])
        width_col2 = max([width_col2, len(headers[1])])
    padding = 1
    col_width = max([width_col1, width_col2, len(str(title))]) + padding*2
    total_inner_width = col_width*2+2
    if title != None:
        output += f"╔{total_inner_width*"═"}╗\n"
        output += f"║{title.center(total_inner_width)}║\n"
        output += f"╚{total_inner_width*"═"}╝\n"
    if headers:
        output += f" {headers[0].center(col_width)} {headers[1].center(col_width)} \n"
    output += f"╭{col_width*"─"}┬{col_width*"─"}╮\n"
    for i in d.items():
        output += f"│{str(i[0]).center(col_width)}│{str(i[1]).center(col_width)}│\n"
    output += f"╰{col_width*"─"}┴{col_width*"─"}╯\n"
    return output

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

def top_dict(d: dict[Any, Any], top=5, r=False) -> dict[Any, Any]:
    sorted_keys = sorted(d, key=d.get, reverse=r)
    top_keys = sorted_keys[:min(top, len(d))]
    final = {}
    for key in top_keys:
        final[key] = d[key]    
    return final

def replace_id_with_name_in_dict(d: dict[int, Any]) -> dict[str, Any]:
    database = get_database()
    result: dict[str, Any] = {}
    for item in tuple(d.items()):
        result[database.get_username_from_id(item[0])] = item[1]
    return result

def view_user_stats(user: User):
    global_stats: GlobalResults = GlobalResults(get_results())
    stats: UserResults = global_stats.get_user_games(user.id)
    winrate = stats.winrate()*100
    print(output_dict_as_table({
        "Games won": stats.games_won(),
        "Games total": stats.games_total(),
        "Winrate": f"{round(winrate, 2)}%",
        "  ": "",
        "Total correct questions": stats.total_achieved(),
        "Average questions per game": f"{round(stats.average_achieved(), 2)}",
        "Highest score": stats.high_score(),
        "   ": "",
        "Average time per game": f"{round(stats.average_time_per_game(), 2)}s",
        "Fastest won game": f"{round(stats.fastest_game(), 2)}s",
        "Total time spent playing": f"{round(stats.total_time(), 2)}s",
    }, title=f"{user.username}'s statistics"))

def view_global_stats():
    global_stats: GlobalResults = GlobalResults(get_results())
    database = get_database()
    total_q = global_stats.highest_achieved()
    fastest_g = global_stats.fastest_game()
    most_games = global_stats.most_games_played()
    print(output_dict_as_table({
        "Highest total questions answered correctly": f"{database.get_username_from_id(total_q[0])} with {total_q[1]} questions.",
        "Most games played": f"{database.get_username_from_id(most_games[0])} with {most_games[1]} games"
    }, title=f"World records"))
    print(output_dict_as_table(replace_id_with_name_in_dict(top_dict(global_stats.games_won())), title="Most games won"))
    print(output_dict_as_table(replace_id_with_name_in_dict(top_dict(global_stats.fastest_wins())), title="Fastest wins"))



def logged_in_menu(user: User):
    exit = False
    while not exit:
        menu: str = f"Hello {user.username}:\n1) View your statistics\n2) View global statistics\n3) Play \"Cichna wants to be a millionare\"\n4) Exit\n"
        input_char: str = f"> "
        user_input_raw: str = input(menu+input_char).strip().lower()
        if not user_input_raw.isdigit():
            user_input = -1
        else:
            user_input: int = int(user_input_raw)
        try:
            match user_input:
                case 1:
                    view_user_stats(user)
                case 2:
                    view_global_stats()
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
                case 2:
                    q_categories()
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
                case 2:
                    user = register()
                    logged_in_menu(user)
                case 3:
                    graph_menu()
                case 4:
                    exit = True
                case _:
                    raise ValueError("Incorrect menu option.")
        except ValueError as e:
            print(f"Error: {e}")