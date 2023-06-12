from pathlib import Path
from string import ascii_lowercase, punctuation, digits
from itertools import product


def check_common_passwords(password_to_crack: str) -> str | None:
    _common_passwords_path = Path("common_words.txt")
    with open(_common_passwords_path) as _file:
        _common_passwords: list[str] = _file.readlines()

    for index, common_password in enumerate(_common_passwords):
        if common_password == password_to_crack:
            return f"Found in common passwords: {common_password}"


def brute_force(password_to_crack: str, length: int, has_digits: bool = False, has_symbols: bool = False) -> str:
    character_set: str = ascii_lowercase
    if has_digits:
        character_set += digits
    if has_symbols:
        character_set += punctuation

    attempts: int = 0

    for guess in product(character_set, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == password_to_crack:
            return f"Password '{password_to_crack}' was cracked in {attempts:,} attempts."


def main():
    print("searching")
    password: str = 'abc1'

    if common_match := check_common_passwords(password):
        print(common_match)
    else:
        if cracked := brute_force(password, length=4, has_digits=True, has_symbols=False):
            print(cracked)
            return ''
        else:
            print("There was no match.")


if __name__ == '__main__':
    main()
