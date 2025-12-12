from user import User
from game_backend import Question, Questions
from game_database import load_questions
import time
import random


class Result:
    def __init__(self, user: User, achieved: int, time_played: float):
        self.user: User = user
        self.achieved: int = achieved
        self.successful: bool = achieved == 15 
        self.time_played: float = time_played
        # how long in seconds it took for the game to finish
        self.timestamp: float = time.time()
        # time since unix epoch
    def __str__(self):
        return f"{self.user.username} achieved {self.achieved} correct questions in {self.time_played}s"

def launch(user: User) -> Result:
    all_questions: Questions = Questions(load_questions())
    chosen_questions: list[Question] = []
    chosen_questions.extend(random.choices(all_questions.easy, k=5))
    chosen_questions.extend(random.choices(all_questions.medium, k=5))
    chosen_questions.extend(random.choices(all_questions.hard, k=5))
    print("Time to start!")
    return game(user, Questions(chosen_questions))
    

def game(user: User, questions: Questions) -> Result:
    total_questions_answered: int = 0
    start_time = time.time()
    for q in questions.easy:
        if not ask_question(q):
            return Result(user, total_questions_answered, time.time()-start_time)
        else:
            total_questions_answered += 1
    for q in questions.medium:
        if not ask_question(q):
            return Result(user, total_questions_answered, time.time()-start_time)
        else:
            total_questions_answered += 1
    for q in questions.hard:
        if not ask_question(q):
            return Result(user, total_questions_answered, time.time()-start_time)
        else:
            total_questions_answered += 1
    return Result(user, total_questions_answered, time.time()-start_time)


def ask_question(question: Question) -> bool:
    question_prompt: str = f"{question.question}\nIs that [T]rue or [F]alse?\n"
    prompt: str = "> "
    result: bool | None = None
    true: list[str] = ["t", "true", "p", "pravda", "1"]
    false: list[str] = ["f", "false", "l", "lez", "0"]
    print(question_prompt)
    while result == None:
        guess: str = input(prompt)
        guess_cleaned: str = guess.lower().strip()
        if guess_cleaned in true:
            result = True
        elif guess_cleaned in false:
            result = False
        else:
            print("Sorry, couldn't understand the input.\nType \"t\" for True, Type \"f\" for False.")
    return result == question.answer

    

