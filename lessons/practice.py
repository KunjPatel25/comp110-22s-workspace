def repeat(word: str, num: int) -> str:
    """Doc"""
    i: int = 0
    result: str = ""
    while i <= num:
        result = result + word[0]
        i = i + 1
    return result