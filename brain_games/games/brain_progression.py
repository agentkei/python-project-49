import random


CONDITIONS = "What number is missing in the progression?"


def creating_progression():
    progression_length = random.randint(5, 10)
    start_progression = random.randint(0, 100)
    step_progression = random.randint(1, 20)
    game_progression = []
    while progression_length != 0:
        game_progression.append(start_progression)
        start_progression = start_progression + step_progression
        progression_length = progression_length - 1
    return game_progression


def creating_game():
    game_progression = creating_progression()
    random_element_index = random.randint(0, len(game_progression) - 1)
    random_element_progression = game_progression[random_element_index]
    correct_answer = str(random_element_progression)
    question = (" ".join(map(str, game_progression)))
    question = question.replace(correct_answer, '..')
    return question, correct_answer
