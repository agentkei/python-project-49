import random
import numexpr as ne


DESCRIPTION = "What is the result of the expression?"


def generate_round():
    first_arg = str(random.randint(1, 100))
    second_arg = str(random.randint(1, 100))
    math_operation = ['+', '-', '*']
    operator = random.choice(math_operation)
    math_expression = (f"{first_arg} {operator} {second_arg}")
    correct_answer = calculate_result(math_expression)
    return math_expression, correct_answer


def calculate_result(math_expression):
    result = str(ne.evaluate(math_expression))
    return result
