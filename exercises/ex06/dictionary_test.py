"""The tests for the dictionary functions."""

__author__ = "730477806"

from dictionary import invert, favorite_color, count


def test_invert_edge() -> None:
    """Testing an edge case for invert."""
    invert_result: dict[str, str] = {}
    assert invert(invert_result) == {}


def test_invert_use1() -> None:
    """Testing a use case for invert."""
    invert_result: dict[str, str] = {"Kunj": "Patel", "Josh": "Tu"}
    assert invert(invert_result) == {"Patel": "Kunj", "Tu": "Josh"}


def test_invert_use2() -> None:
    """Testing another use case for invert."""
    invert_result: dict[str, str] = {"Kunj": "Blue", "Kris": "Green"}
    assert invert(invert_result) == {"Blue": "Kunj", "Green": "Kris"}


def test_favorite_color_edge() -> None:
    """Testing an edge case for favorite color."""
    color_result: dict[str, str] = {}
    assert favorite_color(color_result) == ""


def test_favorite_color_use1() -> None:
    """Testing a use case for favorite color."""
    color_result: dict[str, str] = {"Kunj": "Blue", "Josh": "Blue", "Kris": "Green"}
    assert favorite_color(color_result) == "Blue"


def test_favorite_color_use2() -> None:
    """Testing another use case for favorite color."""
    color_result: dict[str, str] = {"Kunj": "Green", "Josh": "Green", "Kris": "Blue", "Alex": "Blue"}
    assert favorite_color(color_result) == "Green"


def test_count_edge() -> None:
    """Test an edge case for count."""
    count_result: list[str] = []
    assert count(count_result) == {}


def test_count_use1() -> None:
    """Test a use case for count."""
    count_result: list[str] = ["Kunj", "Kunj", "Kris", "Josh"]
    assert count(count_result) == {"Kunj": 2, "Kris": 1, "Josh": 1}


def test_count_use2() -> None:
    """Test another use case for count."""
    count_result: list[str] = ["Kunj", "Kunj", "Kunj", "Kunj"]
    assert count(count_result) == {"Kunj": 4}
