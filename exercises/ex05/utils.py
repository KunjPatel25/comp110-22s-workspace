"""Implementation of skeleton function."""

__author__ = "730477806"


def main() -> None:
    """The necessary main function to run the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    print(only_evens(xs))


def only_evens(xs: list[int]) -> list[int]:
    """Return list of even numbers from the list inputted."""
    evens_list: list[int] = list()
    for num in xs:
        if num % 2 == 0:
            evens_list.append(num)
    return evens_list


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returing a indicated subset of the full list."""
    sub_list: list[int] = list()
    if len(xs) == 0 or start > len(xs) or end <= 0:
        return []
    while start < end:
        sub_list.append(xs[start])
        if start < 0:
            sub_list.append(xs[0])
        if end > len(xs):
            sub_list.append(xs[len(xs) - 1])
        start += 1
    return sub_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatinating two lists together to become one."""
    concat_list: list[int] = list()
    concat_list = xs + ys
    return concat_list
    

if __name__ == "__main__":
    main()