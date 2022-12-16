import random


CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = random.randint(1, 100)
    correct_answer = check_the_number_for_even(random_number)
    return random_number, correct_answer,


def check_the_number_for_even(number):
    even_answer = "yes"
    odd_answer = "no"
    if number % 2 == 0:
        correct_answer = even_answer
    elif number % 2 != 0:
        correct_answer = odd_answer
    return correct_answer
