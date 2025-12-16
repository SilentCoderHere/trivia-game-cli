def get_integer_in_range(
    prompt: str, min_value: int, max_value: int, empty_ok: bool = True
) -> int:
    while True:
        option = input(prompt)
        if empty_ok and not option:
            return 0

        try:
            option = int(option)
            if option < min_value or option > max_value:
                print("Invalid option")
                continue

            return option
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_boolean(prompt: str) -> bool:
    while True:
        answer = input(prompt).lower()
        if answer in ("true", "false", "t", "f"):
            return answer in ("true", "t")
        else:
            print("Invalid. Please enter 't' or 'f'.")
