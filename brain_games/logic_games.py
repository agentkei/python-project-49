import prompt


MAX_ROUNDS = 3


def run_game(game):
    number_of_rounds = 0
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f"Hello, {player_name}!")
    print(game.CONDITIONS)
    while number_of_rounds != MAX_ROUNDS:
        question, correct_answer = game.creating_game()
        print(f'Question: {question}')
        user_answer = input()
        if user_answer == correct_answer:
            number_of_rounds = number_of_rounds + 1
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct "
                  f"answer was {correct_answer}."
                  f"\nLet's try again,{player_name}!")
            return
    print(f"Congratulations, {player_name}!")
