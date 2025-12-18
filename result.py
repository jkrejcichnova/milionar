from user import User
import time
class Result:
    def __init__(self, user_id: int, achieved: int, time_played: float, timestamp: float):
        self.user_id: int = user_id
        # user name
        self.achieved: int = achieved
        self.successful: bool = achieved == 15 
        self.time_played: float = time_played
        # how long in seconds it took for the game to finish
        self.timestamp: float = timestamp
        # time since unix epoch
    def __str__(self):
        return f"{self.user_id} achieved {self.achieved} correct questions in {self.time_played}s"