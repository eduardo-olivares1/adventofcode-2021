import pytest
from ..day3 import binary_diagnostic

test_matrix= [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]

test_matrix = [list(x) for x in test_matrix]

def test_transpose_matrix():
    assert binary_diagnostic.tranpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
    assert binary_diagnostic.tranpose([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [[1,5,9],[2,6,10],[3,7,11],[4,8,12]]

def test_common_bit():
    assert binary_diagnostic.get_common_bit(["0","1","0","1","0"]) == "0"

def test_invert_binary():
    assert binary_diagnostic.invert_binary("11111") == "00000"
    assert binary_diagnostic.invert_binary("10101") == "01010"

def test_get_generator_rating():
    assert binary_diagnostic.get_rating(test_matrix, "generator") == 23

def test_get_scrubber_rating():
    assert binary_diagnostic.get_rating(test_matrix, "scrubber") == 10