import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = random.randint(1, 100)
    if is_even(random_number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return random_number, correct_answer,


def is_even(number):
    return number % 2 == 0
