from collections import deque


def is_palindrome(input_word: str):
    """Check if a word is a palindrome."""

    input_word = input_word.lower().replace(" ", "")
    char_queue = deque(input_word)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True


def check_palindrome():
    """Check if input words are palindromes."""

    while True:
        word_to_check = input("Enter a word to check if it's a palindrome (or 'stop' to exit): ")

        if word_to_check.lower() == 'stop':
            break

        result = is_palindrome(word_to_check)

        if result:
            print("Word is a palindrome.")
        else:
            print("Word is not a palindrome.")


if __name__ == "__main__":
    check_palindrome()
