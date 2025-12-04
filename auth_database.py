import os
import app
import csv
from user import User

class Database:
    def __init__(self):
        self.data: dict[int, User] = {}
    def add_account(self, id, username, hashed_password):
        self.data[id] = User(id, username, hashed_password)

def get_database() -> Database:
    directory: str = app.load_config()['paths']['login_data']
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename: str = app.load_config()['paths']['login_data_filename']
    path = directory+filename
    if os.path.isfile(path):
        read_database(path)

def read_database(path) -> Database:
    database = Database()
    with open(path, encoding="UTF-8") as file:
        r = csv.DictReader(file)
        for row in r:
            database.add_account(row['id'], row['username'], row['password'])
    return database
    

def logins_get_ids() -> list[int]:
