import random


GREETINGS = "What number is missing in the progression?"


def game_description():
    n = random.randint(5, 10)
    start = random.randint(0, 100)
    step = random.randint(1, 20)
    block = []
    while n != 0:
        block.append(start)
        start = start + step
        n = n - 1
    random_size = random.randint(0, len(block) - 1)
    random_element = block[random_size]
    correct_answer = str(random_element)
    progression_size = (" ".join(map(str, block)))
    return_question = progression_size.replace(correct_answer, '..')
    return return_question, correct_answer

