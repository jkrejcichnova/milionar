import config
import csv
from game_backend import Question

def load_questions() -> list[Question]:
    app_config = config.load_config()
    filename: str = app_config["paths"]["question_data"]
    questions: list[Question] = []
    with open(filename, encoding="UTF-8") as file:
        r = csv.DictReader(file)
        for row in r:
            questions.append(Question(row['difficulty'], row['category'], row['question'], row['correct_answer']=="True"))
    return questions