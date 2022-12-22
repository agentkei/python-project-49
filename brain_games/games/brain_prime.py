import random
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = random.randint(0, 100)
    if is_prime(random_number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return random_number, correct_answer


def is_prime(number):
    check_number = 2
    if number <= 1:
        return False
    while check_number <= sqrt(number):
        if number % check_number == 0:
            return False
        check_number += 1
    return True
