class User:
    def __init__(self, id: int, username: str, hashed_password: str):
        self.id = id
        self.username = username
        self.hashed_password = hashed_password
    def __str__(self):
        return f"ID: {self.id}\nUsername: {self.username}"