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
    random_block = random.randint(0, len(block) - 1)
    random_element = block[random_block]
    correct_answer = str(random_element)
    return_question = (" ".join(map(str, block)))
    return_question = return_question.replace(correct_answer, '..')
    return return_question, correct_answer
