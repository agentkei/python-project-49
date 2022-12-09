import random
import prompt


def brain_calc_game():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    operations = ["+", "-", "*"]
    n = 3
    print('What is the result of the expression?')
    while n != 0:
        one_number = random.randint(1, 100)
        two_number = random.randint(1, 100)
        play_operations = random.randint(0, 2)

        x = operations[play_operations]
        question_play = [str(one_number), str(x), str(two_number)]
        question_play = ' '.join(question_play)
        print(f'Question: {question_play}')
        user_answer = input()
        print(f'Your answer: {user_answer}')
        correct_answer = eval(question_play)
        if str(user_answer) == str(correct_answer):
            print('Correct!')
            n = n - 1
        else:
            return (f"{user_answer} is wrong answer ;(. Correct "
                    f"answer was {correct_answer}.\nLet's try again, {name}!")

    return (f"Congratulations, {name}!")


def main():
    print(brain_calc_game())


if __name__ == '__main__':
    main()
