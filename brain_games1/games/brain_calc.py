import random


GREETINGS = "What is the result of the expression?"


def game_description():
    operations = ["+", "-", "*"]
    one_number = random.randint(1, 100)
    two_number = random.randint(1, 100)
    play_operations = random.randint(0, 2)
    x = operations[play_operations]
    question_play = [str(one_number), str(x), str(two_number)]
    question_play = ' '.join(question_play)
    return_question = question_play
    correct_answer = eval(question_play)
    correct_answer = str(correct_answer)
    return return_question, correct_answer
