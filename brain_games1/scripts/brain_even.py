import random
import prompt


def brain_even_games():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    even_answer = "yes"
    odd_answer = "no"
    while n != 3:
        a = random.randint(1, 100)
        print('Question: ' + str(a))
        user_answer = input()
        print('Your answer: ' + str(user_answer))
        if a % 2 == 0 and user_answer == even_answer:
            print('Correct!')
            n += 1
        elif a % 2 != 0 and user_answer == odd_answer:
            print('Correct!')
            n += 1
        elif a % 2 == 0 and user_answer != even_answer:
            return (f"{user_answer} is wrong answer ;(. Correct "
                    f"answer was {even_answer}.\nLet's try again, {name}!")
        elif a % 2 != 0 and user_answer != odd_answer:
            return (f"{user_answer} is wrong answer ;(. Correct "
                    f"answer was {odd_answer}.\nLet's try again, {name}!")
    return (f"Congratulations, {name}!")


def main():
    print(brain_even_games())


if __name__ == '__main__':
    main()
