from re import U
from user import User
import user
import user_database
import random

def generate_id(existing_ids: list[int]) -> int:
    id = random.randint(0,2**32-1)
    while id in existing_ids:
        id = random.randint(0,2**32-1)
    return id

def hash_password(cleartext_password: str) -> str:
    # TODO HASH PASSWORD!
    return cleartext_password

def login(username: str, cleartext_password: str) -> User:
    database = user_database.get_database()
    id = database.get_id_from_username(username)
    if id == None:
        raise ValueError("User not found.")
    user = database.data[id]
    if user.hashed_password == hash_password(cleartext_password):
        return user
    else:
        raise ValueError("The provided password is incorrect.")
    
def register(username: str, cleartext_password: str) -> User:
    database = user_database.get_database()
    id = generate_id(database.get_ids())
    hashed_password = hash_password(cleartext_password)
    user = database.add_account(id, username, hashed_password)
    user_database.write_database(database)
    return user
    
    