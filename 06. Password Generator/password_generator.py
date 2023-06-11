from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice


def generate_password(length: int, symbols: bool = True, uppercase: bool = True) -> str:
    character_set: str = ascii_lowercase + digits
    if symbols:
        character_set += punctuation
    if uppercase:
        character_set += ascii_uppercase

    while True:
        generated_password = ""
        contains_symbols: bool = False
        contains_uppercase: bool = False
        for _ in range(length):
            generated_password += choice(character_set)

        for char in generated_password:
            if char in punctuation:
                contains_symbols = True
            elif char in ascii_uppercase:
                contains_uppercase = True

        if symbols and uppercase:
            if contains_uppercase and contains_symbols:
                return generated_password
        elif symbols and not uppercase:
            if contains_symbols:
                return generated_password
        elif uppercase and not symbols:
            if contains_uppercase:
                return generated_password
        else:
            return generated_password


def contains_upper(new_password: str) -> bool:
    for char in new_password:
        if char.isupper():
            return True
    return False


def contains_symbol(new_password: str) -> bool:
    for char in new_password:
        if char in punctuation:
            return True
    return False


if __name__ == "__main__":
    for x in range(100):
        password = generate_password(30, symbols=True, uppercase=True)
        print(f"{x + 1}:\t{password}", end="\t")
        print(f"(U: {contains_upper(password)}, S: {contains_symbol(password)})")
