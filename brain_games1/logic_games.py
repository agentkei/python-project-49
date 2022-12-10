import prompt


def run_game(game):
    index = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.GREETINGS)
    while index != 3:
        question, correct = game.game_description()
        print(f'Question: {question}')
        user_answer = input()
        if user_answer == correct:
            index = index + 1
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct "
                  f"answer was {correct}.\nLet's try again, {name}!")
            break
    if index == 3:
        print(f"Congratulations, {name}!")
