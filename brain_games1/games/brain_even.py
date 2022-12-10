import random


GREETINGS = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_description():
    even_answer = "yes"
    odd_answer = "no"
    return_question = random.randint(1, 100)
    if return_question % 2 == 0:
        correct_answer = even_answer
    elif return_question % 2 != 0:
        correct_answer = odd_answer
    return return_question, correct_answer
