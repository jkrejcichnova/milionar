from enum import Enum
#i miss rust

class Difficulty(Enum):
    easy = 1
    medium = 2
    hard = 3

class Question:
    def __init__(self, difficulty: Difficulty, category: str, question: str, answer: bool):
        self.difficulty = difficulty
        self.category = category
        self.question = question
        self.answer = answer
    def __str__(self):
        return f"{self.question}"
    
class Questions:
    def __init__(self, questions: list[Question]):
        self.easy: list[Question] = []
        self.medium: list[Question] = []
        self.hard: list[Question] = []
        for q in questions:
            match q.difficulty.name:
                case 'easy': self.easy.append(q)
                case 'medium': self.medium.append(q)
                case 'hard': self.hard.append(q)
                case _: raise ValueError("Unknown difficulty encountered")