import random
import math
import prompt


def brain_nod_games():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    n = 3
    print("Find the greatest common divisor of given numbers.")
    while n != 0:

        one_number = random.randint(1, 100)
        two_number = random.randint(1, 100)
        print(f'Question: {one_number} {two_number}')
        user_answer = (input())
        correct_answer = str(math.gcd(one_number, two_number))
        if str(user_answer) == correct_answer:
            print('Correct!')
            n = n - 1
        else:
            return (f"{user_answer} is wrong answer ;(. Correct "
                    f"answer was {correct_answer}.\nLet's try again, {name}!")
    return (f"Congratulations, {name}!")


def main():
    print(brain_nod_games())


if __name__ == '__main__':
    main()
