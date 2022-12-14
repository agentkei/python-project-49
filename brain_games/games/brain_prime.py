import random
from math import sqrt


CONDITIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def checking_is_prime():
    prime = True
    random_number = random.randint(2, 100)
    check_number = 2
    while check_number <= sqrt(random_number):
        if random_number % check_number == 0:
            prime = False
            break
        check_number = check_number + 1
    return random_number, prime


def creating_game():
    question, prime = checking_is_prime()
    if prime:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
