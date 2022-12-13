#!/usr/bin/env python3


from brain_games.games import brain_gcd
from brain_games.logic_games import run_game


def main():
    run_game(brain_gcd)


if __name__ == '__main__':
    main()