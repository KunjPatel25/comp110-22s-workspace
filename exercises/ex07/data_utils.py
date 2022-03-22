"""Dictionary related utility functions."""

__author__ = "730477806"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(row_table: list[dict[str, str]], column: str) -> list[str]:
    """A list of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in row_table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforming a table of a list of rows into a dictionary of columns."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(headers: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data."""
    result: dict[str, list[str]] = {}
    for columns in headers:
        i: int = 0
        store: list[str] = []
        if n >= len(headers):
            for items in headers[columns]:
                store.append(items)
        else: 
            while i < n:
                store.append(headers[columns][i])
                i += 1
        result[columns] = store
    return result


def select(selected: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for columns in names:
        result[columns] = selected[columns]

    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for columns in a:
        result[columns] = a[columns]
    for columns in b:
        if columns in result:
            for item in b[columns]:
                result[columns].append(item)
        else:
            result[columns] = b[columns]
    
    return result


def count(count: list[str]) -> dict[str, int]:
    """Count the number of times the value appeared in the input list."""
    result: dict[str, int] = {}
    for items in count:
        if items in result:
            result[items] += 1
        else:
            result[items] = 1

    return result