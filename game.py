from user import User
from game_backend import Question, Questions
from game_database import load_questions, add_to_results
from result import Result
import time
import random

def launch(user: User) -> Result:
    all_questions: Questions = Questions(load_questions())
    chosen_questions: list[Question] = []
    chosen_questions.extend(random.choices(all_questions.easy, k=5))
    chosen_questions.extend(random.choices(all_questions.medium, k=5))
    chosen_questions.extend(random.choices(all_questions.hard, k=5))
    print("Time to start!")
    result = game(user, Questions(chosen_questions))
    add_to_results(result)
    return result
    

def game(user: User, questions: Questions) -> Result:
    total_questions_answered: int = 0
    start_time = time.time()
    for q in questions.easy:
        if not ask_question(q):
            return Result(user.id, total_questions_answered, time.time()-start_time, time.time())
        else:
            total_questions_answered += 1
    for q in questions.medium:
        if not ask_question(q):
            return Result(user.id, total_questions_answered, time.time()-start_time, time.time())
        else:
            total_questions_answered += 1
    for q in questions.hard:
        if not ask_question(q):
            return Result(user.id, total_questions_answered, time.time()-start_time, time.time())
        else:
            total_questions_answered += 1
    return Result(user.id, total_questions_answered, time.time()-start_time, time.time())


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

    

