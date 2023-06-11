from random import choice

with open('words.txt') as file:
    words: list[str] = file.readlines()

# choose a random word
secret_word: str = choice(words).removesuffix('\n')
secret_word_length = len(secret_word)
secret_word_hidden: list[str] = ['~'] * secret_word_length

# keep track of guesses in seen
seen: list[str] = []

# set the starting lives
STARTING_LIVES: int = max(8, secret_word_length // 3 * 2)


def main(current_lives=STARTING_LIVES):
    print('Welcome to Hangman.')
    while True:
        print(''.join(secret_word_hidden))
        print('Previous guesses: ', end='')
        print(*seen, sep=', ')
        print(f'Lives: {current_lives}')
        guess: str = input('New guess: ').lower().strip()

        if not guess.isalpha():
            print(f'{guess} is not a valid string.\n')
            continue
        if guess in seen:
            print(f'You have already guessed {guess}.\n')
            continue
        else:
            seen.append(guess)
            seen.sort()

        # check win condition
        if guess == secret_word:
            print(f'You were correct! The secret word was {secret_word}.')
            break

        # check each letter
        found: bool = False
        for index, character in enumerate(secret_word):
            if character == guess:
                secret_word_hidden[index] = character
                found = True

        if ''.join(secret_word_hidden) == secret_word:
            print(f'You were correct! The secret word was {secret_word}.')
            break

        if not found:
            current_lives -= 1

        # check if we have died
        if current_lives <= 0:
            print(f'Sorry, you lost. The secret word was {secret_word}.')
            break
        else:
            print()


if __name__ == '__main__':
    main()
