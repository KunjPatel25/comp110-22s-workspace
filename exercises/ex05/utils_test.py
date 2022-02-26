"""The unit test functions."""

__author__ = "730477806"

from utils import only_evens, sub, concat


def test_only_evens_edge() -> None:
    """Testing an edge case for only_evens."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_use1() -> None:
    """Testing a use case for only_evens."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_only_evens_use2() -> None:
    """Testing another use case for only_evens."""
    xs: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_sub_edge() -> None:
    """Testing an edge case for sub."""
    xs: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 6
    assert sub(xs, start, end) == [20, 30, 40]


def test_sub_use1() -> None:
    """Testing a use case for sub."""
    xs: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == [20, 30]


def test_sub_use2() -> None:
    """Testing another use case for sub."""
    xs: list[int] = [1, 5, 9, 3, 7, 15, 12]
    start: int = 3
    end: int = 6
    assert sub(xs, start, end) == [3, 7, 15]


def test_concat_edge() -> None:
    """Testing an edge case for concat."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_use1() -> None:
    """Testing a use case for concat."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_use2() -> None:
    """Testing another use case for concat."""
    xs: list[int] = [60, 20, 200]
    ys: list[int] = [1000, 38, 96]
    assert concat(xs, ys) == [60, 20, 200, 1000, 38, 96]