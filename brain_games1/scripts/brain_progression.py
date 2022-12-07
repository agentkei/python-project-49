import random
import prompt


def brain_progression_game():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    z = 3
    print("What number is missing in the progression?")
    while z != 0:
        n = random.randint(5, 10)
        start = random.randint(0, 100)
        step = random.randint(1, 20)
        block = []
        while n != 0:
            block.append(start)
            start = start + step
            n = n - 1
        random_block = random.randint(0, len(block) - 1)
        random_element = block[random_block]
        random_element = str(random_element)
        str_block = (" ".join(map(str, block)))

        str_block = str_block.replace(random_element, ' ... ')
        print(str_block)
        user_answer = str(input())
        if user_answer == random_element:
            print("Correct!")
            z = z - 1
        else:
            return (f"{user_answer} is wrong answer ;(. Correct "
                    f"answer was {random_element}.\nLet's try again, {name}!")
    return (f"Congratulations, {name}!")


def main():
    print(brain_progression_game())


if __name__ == '__main__':
    main()
