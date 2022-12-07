#!/usr/bin/env python3
from brain_games1.scripts.cli import welcome_user


def hello_user():
    print('Welcome to the Brain Games!')
    return (welcome_user())


def main():
    print(hello_user())


if __name__ == '__main__':
    main()
