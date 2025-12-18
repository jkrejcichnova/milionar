import matplotlib.pyplot as plt
from game_database import load_questions

def q_categories():
    questions = load_questions()
    categories: dict[str, int] = {}
    for q in questions:
        if q.category not in categories.keys():
            categories[q.category] = 1
        else:
            categories[q.category] += 1
    plt.xticks(rotation=45)
    plt.bar(categories.keys(), categories.values())
    plt.ylabel('Počet otázek')
    plt.title('Poměr kategorií v datasetu otázek')
    plt.show()
    
def q_difficulties():
    questions = load_questions()
    difficulties: dict[str, int] = {}
    for q in questions:
        if q.difficulty not in difficulties.keys():
            difficulties[q.difficulty] = 1
        else:
            difficulties[q.difficulty] += 1
    plt.xticks(rotation=45)
    plt.bar(difficulties.keys(), difficulties.values(), color=['green', 'orange', 'crimson'])
    plt.ylabel('Počet otázek')
    plt.title('Poměr kategorií v datasetu otázek')
    plt.show()
    