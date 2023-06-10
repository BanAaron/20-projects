
from enum import StrEnum


class WordType(StrEnum):
    noun = 'noun'
    verb = 'verb'
    adjective = 'adjective'


def prompt_user(word_type: WordType) -> str:
    user_input: str = input(f'Enter a {word_type}: ')
    return user_input


if __name__ == '__main__':
    noun = prompt_user(WordType.noun)
    verb = prompt_user(WordType.verb)
    adjective = prompt_user(WordType.adjective)

    print(
        f'You like to {verb} {adjective} {noun}.'
    )
