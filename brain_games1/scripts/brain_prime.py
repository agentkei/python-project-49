import random
from math import sqrt
import prompt


def brain_game_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = 3
    simple = True
    while n != 0:
        random_number = random.randint(2, 100)
        i = 2
        while i <= sqrt(random_number):
            if random_number % i == 0:
                simple = False
                break
            i = i + 1

        if simple:
            correct_answer = "yes"
        else:
            correct_answer = "no"

        random_number = str(random_number)
        print(f'Question: {random_number}')
        user_answer = str(input())
        print(f'Your answer: {user_answer}')
        if user_answer == correct_answer:
            print("Correct!")
            n = n - 1
        else:
            return (f"{user_answer} is wrong answer ;(. Correct "
                    f"answer was {correct_answer}.\nLet's try again, {name}!")
    return (f"Congratulations, {name}!")


def main():
    print(brain_game_prime())


if __name__ == '__main__':
    main()
