import os
from typing import dataclass_transform
import config
import csv
from user import User

class Database:
    def __init__(self, path: str):
        self.path: str = path
        self.data: dict[int, User] = {}
    def add_account(self, id, username, hashed_password) -> User:
        self.data[id] = User(id, username, hashed_password)
        return self.data[id]
    def get_ids(self) -> list[int]:
        return list(self.data.keys())
    def get_usernames(self) -> list[str]:
        usernames: list[str] = []
        for user in self.data.values():
            usernames.append(user.username)
        return usernames
    def get_id_from_username(self, username:str) -> int|None:
        for user in self.data.values():
            if user.username == username:
                return user.id
        return None
    def get_username_from_id(self, id:int) -> str:
        for user in self.data.values():
            if user.id == id:
                return user.username
        return str(id)


def get_database() -> Database:
    app_config = config.load_config()
    directory: str = app_config["paths"]["login_data"]
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename: str = app_config["paths"]["login_data_filename"]
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        return read_database(path)
    else:
        database = Database(path)
        write_database(database, path)
        return database

def write_database(database: Database, path:None|str=None):
    if path == None:
        path = database.path
    open_function = open(path, mode="w", encoding="UTF-8")
    if not os.path.isfile(path):
        open_function = open(path, mode="x", encoding="UTF-8")
    with open_function as file:
        w = csv.writer(file)
        w.writerow(["id", "username", "password"])
        for user in database.data.values():
            w.writerow(user.csv())

def read_database(path) -> Database:
    database = Database(path)
    with open(path, encoding="UTF-8") as file:
        r = csv.DictReader(file)
        for row in r:
            database.add_account(row['id'], row['username'], row['password'])
    return database
    
