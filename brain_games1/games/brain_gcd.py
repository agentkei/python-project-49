import random
import math


GREETINGS = 'Find the greatest common divisor of given numbers.'


def game_description():
    one_number = random.randint(1, 100)
    two_number = random.randint(1, 100)
    correct_answer = str(math.gcd(one_number, two_number))
    return_question = (f"{one_number} {two_number}")
    return return_question, correct_answer
