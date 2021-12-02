import pytest
from ..day2 import dive

def test_case1():
    my_sub = dive.Submarine()
    my_sub.forward(5)
    my_sub.down(5)
    my_sub.forward(8)
    my_sub.up(3)
    my_sub.down(8)
    my_sub.forward(2)
    assert my_sub.get_sum() == 150

def test_case2():
    my_sub5 = dive.SubmarineComplex()
    my_sub5.forward(5)
    my_sub5.down(5)
    my_sub5.forward(8)
    my_sub5.up(3)
    my_sub5.down(8)
    my_sub5.forward(2)
    assert my_sub5.get_sum() == 900