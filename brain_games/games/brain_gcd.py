import random
import math


CONDITIONS = 'Find the greatest common divisor of given numbers.'


def creating_game():
    one_number = random.randint(1, 100)
    two_number = random.randint(1, 100)
    correct_answer = str(math.gcd(one_number, two_number))
    question = (f"{one_number} {two_number}")
    return question, correct_answer
