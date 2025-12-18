import config
import csv
from result import Result
from game_backend import Question
import os

def load_questions() -> list[Question]:
    app_config = config.load_config()
    filename: str = app_config["paths"]["question_data"]
    questions: list[Question] = []
    with open(filename, encoding="UTF-8") as file:
        r = csv.DictReader(file)
        for row in r:
            questions.append(Question(row['difficulty'], row['category'], row['question'], row['correct_answer']=="True"))
    return questions

def get_results() -> list[Result]:
    app_config = config.load_config()
    filename: str = app_config["paths"]["winner_data"]
    results: list[Result] = []
    with open(filename, encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            results.append(Result(row['user'], row['achieved'], row['time_played']))
    return results
    
# tenhle kod je fakt... fuj...
# nejspise prepisu aby to nacetlo results do list[Results] a tam proste appendne Result... neucinne ale asi prehlednejsi
    
def assert_results_file(path):
    if os.path.isfile(path):
        with open(path, mode="r+", encoding="UTF-8") as file:
            if not file.read():
                writer = csv.writer(file)
                writer.writerow(['user', 'achieved', 'time_played', 'timestamp'])
    else:
        with open(path, mode="w", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow(['user', 'achieved', 'time_played', 'timestamp'])


def add_to_results(result: Result):
    app_config = config.load_config()
    filename: str = app_config["paths"]["winner_data"]
    assert_results_file(filename)
    with open(filename, mode="a", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow([result.user_id, result.achieved, result.time_played, result.timestamp])
        