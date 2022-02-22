"""A more updated game of wordle."""

__author__ = "730477806"


def contains_char(word: str, character: str) -> bool:
    """Character is being searched for within the secret word."""
    assert len(character) == 1
    index: int = 0
    while index < len(word):
        if word[index] == character:
            return True
        else:
            index = index + 1
    return False

 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """The colored boxes of wordle."""
    assert len(guess) == len(secret)
    result: str = ""
    index: int = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            result = result + GREEN_BOX
        elif contains_char(secret, guess[index]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        index = index + 1
    return result


def input_guess(expected_length: int) -> str:
    """Guess is correct amount of letters."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret_word: str = "staub"
    index: int = 1
    guess: str = ""
    while index <= 6 and secret_word != guess:
        print(f"=== Turn {index}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if secret_word == guess:
            print(f"You won in {index}/6 turns!")  
        index = index + 1
    if index > 6:
        print("X/6 - Sorry, try again tomorrow!")
        

if __name__ == "__main__":
    main()
        

        



    
