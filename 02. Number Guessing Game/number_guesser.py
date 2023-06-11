from random import randint


def random_number(_minimum: int, _maximum: int) -> int:
    return randint(_minimum, _maximum)


if __name__ == "__main__":
    minimum: int = 1
    maximum: int = 100
    target: int = random_number(minimum, maximum)

    while True:
        guess: str = input(f"Guess the number between {minimum}-{maximum}: ")
        if guess == "exit":
            break
        try:
            guess_as_int: int = int(guess)
        except ValueError:
            print(f"{guess} is not an integer.")
            continue

        if guess_as_int == target:
            print(f"You win! The correct answer was {target}")
            break
        elif guess_as_int < target:
            print("Too low.")
        elif guess_as_int > target:
            print("Too high.")
