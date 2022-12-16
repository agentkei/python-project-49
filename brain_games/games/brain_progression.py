import random


CONDITION = "What number is missing in the progression?"


def generate_round():
    length = random.randint(5, 10)
    start = random.randint(0, 100)
    step = random.randint(1, 20)
    progression = generate_progression(start, length, step)
    random_element_index = random.randint(0, len(progression) - 1)
    random_element_progression = progression[random_element_index]
    correct_answer = str(random_element_progression)
    question = (" ".join(map(str, progression)))
    question = question.replace(correct_answer, '..')
    return question, correct_answer


def generate_progression(start, length, step):
    progression = []
    while length != 0:
        progression.append(start)
        start = start + step
        length = length - 1
    return progression
