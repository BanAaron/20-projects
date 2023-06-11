import os
from enum import StrEnum
from random import choice


class Moves(StrEnum):
    rock = 'rock',
    paper = 'paper',
    scissors = 'scissors',


valid_moves: dict[str, str] = {
    Moves.rock: '🪨',
    Moves.paper: '📃',
    Moves.scissors: '✂️',
}


def main():
    user_score: int = 0
    ai_score: int = 0

    while True:
        print(f'Your score: {user_score}\t\tAI score: {ai_score}')
        users_move: str = input('Rock, paper, or scissors? ').strip().lower()
        ai_move: str = choice(list(valid_moves.keys()))

        if users_move == 'exit':
            print('Thanks for playing')
            break

        # validate input
        if users_move not in valid_moves:
            print('Please enter a valid move.')
            continue

        os.system('cls||clear')
        # display each player choice
        print('---')
        print(f'You: {valid_moves[users_move]}')
        print(f'AI: {valid_moves[ai_move]}')
        print('---')

        # check if we have a winner
        if users_move == ai_move:
            print('Draw.')
        # rocks
        elif users_move == Moves.rock and ai_move == Moves.scissors:
            print('You Win!')
            user_score += 1
        # papers
        elif users_move == Moves.paper and ai_move == Moves.rock:
            print('You win!')
            user_score += 1
        # scissors
        elif users_move == Moves.scissors and ai_move == Moves.paper:
            print('You win!')
            user_score += 1

        else:
            print('You Lose.')
            ai_score += 1

        print()  # new line


if __name__ == '__main__':
    main()
