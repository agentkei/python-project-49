import random


DESCRIPTION = "What number is missing in the progression?"


def generate_round():
    length = random.randint(5, 10)
    first_elem = random.randint(0, 100)
    step = random.randint(1, 20)
    progression = generate_progression(first_elem, length, step)
    random_element_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[random_element_index])
    progression[random_element_index] = '..'
    question = (" ".join(map(str, progression)))
    return question, correct_answer


def generate_progression(first_elem, length, step):
    progression = []
    counter = 0
    while counter != length:
        progression.append(first_elem + step * counter)
        counter += 1
    return progression
