"""Dictionary functions."""

__author__ = "730477806"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert the key and value items in the dictionary."""
    invert_result: dict[str, str] = {}
    for key in a:
        value: str = a[key]
        if value in invert_result:
            raise KeyError
        else:
            invert_result[value] = key
    return invert_result


def favorite_color(b: dict[str, str]) -> str:
    """Returning the color that appears most frequesntly."""
    color_result: dict[str, int] = {}
    max: int = 0
    color: str = ""
    for key in b:
        if b[key] in color_result:
            color_result[b[key]] += 1
        else:
            color_result[b[key]] = 1
    for key in color_result:
        if color_result[key] > max:
            max = color_result[key]
            color = key
    return color


def count(b: list[str]) -> dict[str, int]:
    count_result: dict[str, int] = {}
    for key in b:
        if key in count_result:
            count_result[key] += 1
        else:
            count_result[key] = 1
    return count_result
