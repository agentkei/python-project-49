import random


CONDITION = "What number is missing in the progression?"


def generate_round():
    length = random.randint(5, 10)
    start = random.randint(0, 100)
    step = random.randint(1, 20)
    progression = generate_progression(start, length, step)
    random_element_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[random_element_index])
    progression[random_element_index] = '..'
    question = (" ".join(map(str, progression)))
    return question, correct_answer


def generate_progression(start, length, step):
    progression = []
    while length != 0:
        progression.append(start)
        start = start + step
        length = length - 1
    return progression
