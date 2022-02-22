"""The creation of the game Worlde."""

__author__ = "730477806"

secret_word: str = "cuddle"
guess: str = input(print(f"What is your {len(secret_word)}-letter guess?"))

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
result: str = ""

while index < len(secret_word):
    if guess[index] == secret_word[index]:
        result = result + GREEN_BOX
    else:
        yellow: bool = False
        alt_int: int = 0
        while not yellow and alt_int < len(secret_word):
            if guess[index] == secret_word[alt_int]:
                result = result + YELLOW_BOX
                yellow = True
            alt_int = alt_int + 1  
        if guess[index] != secret_word[index] and not yellow:
            result = result + WHITE_BOX
    index = index + 1  
print(result)