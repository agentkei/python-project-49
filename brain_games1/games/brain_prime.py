import random
from math import sqrt


GREETINGS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_description():
    simple = True
    return_question = random.randint(2, 100)
    i = 2
    while i <= sqrt(return_question):
        if return_question % i == 0:
            simple = False
            break
        i = i + 1
    if simple:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return return_question, correct_answer
