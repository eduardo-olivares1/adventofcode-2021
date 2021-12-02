import pytest
from ..day2 import dive



def test_forward():
    my_sub = dive.Submarine()
    my_sub.forward(5)
    my_sub.forward(10)
    assert my_sub.horizontal == 15

def test_down():
    my_sub2 = dive.Submarine()
    my_sub2.down(10)
    my_sub2.down(10)
    assert my_sub2.depth == 20

def test_up():
    my_sub3 = dive.Submarine()
    my_sub3.up(5)
    my_sub3.up(11)
    my_sub3.depth == -16

def test_get_sum():
    my_sub4 = dive.Submarine()
    my_sub4.down(10)
    my_sub4.forward(33)
    assert my_sub4.get_sum() == 330