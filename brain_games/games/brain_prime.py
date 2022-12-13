import random
from sympy import *


CONDITIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def checking_is_prime():
    random_number = random.randint(2, 100)
    feature = isprime(random_number)
    return random_number, feature


def creating_game():
    question, prime = checking_is_prime()
    if prime:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(question), correct_answer
