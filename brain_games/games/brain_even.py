import random


CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = random.randint(1, 100)
    even_answer = "yes"
    odd_answer = "no"
    even = is_even(random_number)
    if even is True:
        correct_answer = even_answer
    else:
        correct_answer = odd_answer
    return random_number, correct_answer,


def is_even(number):
    if number % 2 == 0:
        return True
    return False
