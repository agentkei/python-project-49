import random
import numexpr as ne


CONDITION = "What is the result of the expression?"


def generate_round():
    first_arg = str(random.randint(1, 100))
    second_arg = str(random.randint(1, 100))
    index_math_operation = random.randint(0, 2)
    math_operations = ["+", "-", "*"]
    rndm_operat = math_operations[index_math_operation]
    question, cor_answer = calculate_result(first_arg, rndm_operat, second_arg)
    return question, cor_answer


def calculate_result(first_argument, math_operations, second_argument):
    math_expression = (f"{first_argument} {math_operations} {second_argument}")
    result = str(ne.evaluate(math_expression))
    return math_expression, result
