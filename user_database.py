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
    with open(path, mode="rw", encoding="UTF-8") as file:
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
    
