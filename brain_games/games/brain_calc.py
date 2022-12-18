import random
import numexpr as ne


CONDITION = "What is the result of the expression?"


def generate_round():
    first_arg = str(random.randint(1, 100))
    second_arg = str(random.randint(1, 100))
    index_math_operation = random.randint(0, 2)
    math_operations = ["+", "-", "*"]
    rndm_operat = math_operations[index_math_operation]
    math_expression = (f"{first_arg} {rndm_operat} {second_arg}")
    cor_answer = calculate_result(math_expression)
    return math_expression, cor_answer


def calculate_result(math_expression):
    result = str(ne.evaluate(math_expression))
    return result
