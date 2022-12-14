import random


CONDITIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def creating_game_data():
    even_answer = "yes"
    odd_answer = "no"
    random_number = random.randint(1, 100)
    return even_answer, odd_answer, random_number


def creating_game():
    even_number, odd_number, question = creating_game_data()
    if question % 2 == 0:
        correct_answer = even_number
    elif question % 2 != 0:
        correct_answer = odd_number
    return question, correct_answer
