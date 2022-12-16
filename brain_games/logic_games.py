import prompt


MAX_ROUNDS = 3


def run_game(game):
    round_number = 0
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f"Hello, {player_name}!")
    print(game.CONDITION)
    while round_number != MAX_ROUNDS:
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            round_number = round_number + 1
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct "
                  f"answer was {correct_answer}."
                  f"\nLet's try again, {player_name}!")
            return
    print(f"Congratulations, {player_name}!")
