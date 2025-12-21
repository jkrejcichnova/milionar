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
    def asdict(self) -> dict[str, int|float]:
        return {'user_id': self.user_id, 'achieved': self.achieved, 'time_played': self.time_played, 'timestamp': self.timestamp}
    def time_per_question(self) -> float:
        if not self.achieved:
            return self.achieved
        return self.time_played/self.achieved
    def __str__(self):
        return f"{self.user_id} achieved {self.achieved} correct questions in {self.time_played}s"

class UserResults:
    def __init__(self, user_id: int, games: list[Result]):
        self.user_id = user_id
        self.games = games
    def games_won(self) -> int:
        n = 0
        for g in self.games:
            n += g.successful
        return n
    def games_total(self) -> int:
        return len(self.games)
    def winrate(self) -> float:
        if not self.games_total():
            return 0
        return self.games_won()/self.games_total()
    def total_achieved(self) -> int:
        n = 0
        for g in self.games:
            n += g.achieved
        return n
    def average_achieved(self) -> float:
        if not self.games_total():
            return 0
        return self.total_achieved()/self.games_total()
    def average_time_per_game(self) -> float:
        n: float = 0.0
        if not self.games_total():
            return n
        for g in self.games:
            n += g.time_per_question()
        return n/self.games_total()
    def fastest_game(self) -> float:
        t: float = 0.0
        for g in self.games:
            if g.successful:
                if g.time_played < t or t == 0.0:
                    t = g.time_played
        return t
    def high_score(self) -> int:
        n = 0
        for g in self.games:
            if g.achieved > n:
                n = g.achieved
        return n
    def total_time(self) -> float:
        t: float = 0.0
        for g in self.games:
            t += g.time_played
        return t
    

class GlobalResults:
    def __init__(self,games: list[Result]):
        self.games = games
    def get_user_games(self, id: int) -> UserResults:
        games: list[Result] = []
        for g in self.games:
            if g.user_id == id:
                games.append(g)
        return UserResults(id, games)
    def games_won(self) -> dict[int, int]:
        games_won: dict[int, int] = {}
        for g in self.games:
            if g.successful:
                if g.user_id not in games_won.keys():
                    games_won[g.user_id] = 1
                else:
                    games_won[g.user_id] += 1
        return games_won
    def fastest_wins(self) -> dict[int, float]:
        fastest_winners: dict[int, float] = {}
        for g in self.games:
            if g.successful:
                if g.user_id not in fastest_winners.keys():
                    fastest_winners[g.user_id] = g.time_played
                else:
                    if g.timestamp < fastest_winners[g.user_id]:
                        fastest_winners[g.user_id] = g.time_played
        return fastest_winners
    def get_users(self) -> list[int]:
        users: list[int] = []
        for g in self.games:
            if g.user_id not in users:
                users.append(g.user_id)
        return users
    def highest_achieved(self) -> tuple[int, int]:
        highest_achieved: tuple[int, int] = (0,0)
        for u in self.get_users():
            results = self.get_user_games(u)
            if results.total_achieved() > highest_achieved[1]:
                highest_achieved = (u, results.total_achieved())
        return highest_achieved
    def fastest_game(self) -> tuple[int, float]:
        fastest_game: tuple[int, float] = (0, 0.0)
        for g in self.games:
            if g.successful:
                if g.time_played < fastest_game[1]:
                    fastest_game = (g.user_id, g.time_played)
        return fastest_game
    def most_games_played(self) -> tuple[int, int]:
        most_games: tuple[int, int] = (0,0)
        for u in self.get_users():
            results = self.get_user_games(u)
            if results.games_total() > most_games[1]:
                most_games = (u, results.games_total())
        return most_games

