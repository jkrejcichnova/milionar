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
            results.append(Result(int(row['user']), int(row['achieved']), float(row['time_played']), float(row['timestamp'])))
    return results


def add_to_results(result: Result):
    app_config = config.load_config()
    filename: str = app_config["paths"]["winner_data"]
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", encoding="UTF-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(result.asdict().keys()))
        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()
        writer.writerow(result.asdict())
        