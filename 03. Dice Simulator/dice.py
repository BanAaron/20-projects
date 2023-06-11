from random import randint


def roll_dice(amount: int) -> list[int]:
    return [randint(1, 6) for _ in range(amount)]


def main():
    while True:
        user_input: str = input("How many dice would you like to roll? ")

        # if the user enters 'exit', we should end the program
        if user_input.lower() == "exit":
            print("Thanks for playing!")
            break

        # try convert to int
        try:
            user_input_as_int: int = int(user_input)
            if user_input_as_int <= 0:
                raise ValueError
        except ValueError:
            print("Please inter a valid integer.")
            continue

        rolls: list[int] = roll_dice(user_input_as_int)
        # unpack with the splat (*) operator
        print(*rolls, sep=", ")
        print(f"Total: {sum(rolls)}")


if __name__ == "__main__":
    main()
