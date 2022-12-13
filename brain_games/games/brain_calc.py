import random
import numexpr as ne


CONDITIONS = "What is the result of the expression?"


def create_math_arguments():
    math_operations = ["+", "-", "*"]
    first_argument = str(random.randint(1, 100))
    second_argument = str(random.randint(1, 100))
    index_math_operation = random.randint(0, 2)
    random_math_operation = math_operations[index_math_operation]
    math_expression = (f"{first_argument} {random_math_operation} {second_argument}")
    return math_expression


def creating_game():
    question = create_math_arguments()
    correct_answer = str(ne.evaluate(question))
    return question, correct_answer
