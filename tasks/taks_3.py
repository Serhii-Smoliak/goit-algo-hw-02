def check_delimiters(string):
    """Checks the symmetry of delimiter sequence in a string."""

    stack = []
    opening = "([{"
    closing = ")]}"
    pairs = {"(": ")", "[": "]", "{": "}"}

    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return "Asymmetrically"
            top = stack.pop()
            if pairs[top] != char:
                return "Asymmetrically"

    if stack:
        return "Asymmetrically"
    else:
        return "Symmetrically"


def check_delimiters_interactively():
    """Check if input delimiter sequences are symmetric."""

    while True:
        delimiters_to_check = input(
            "Enter a sequence of delimiters to check if they are symmetric (or 'quit' to exit): ")

        if delimiters_to_check.lower() == 'stop':
            break

        result = check_delimiters(delimiters_to_check)
        print("Delimiters sequence:", result)


if __name__ == "__main__":
    check_delimiters_interactively()
