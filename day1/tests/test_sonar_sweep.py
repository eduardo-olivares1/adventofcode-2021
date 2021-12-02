import pytest
from .. import sonar_sweep

def test_count_increase():
    assert sonar_sweep.count_increases([1,2,3,4,5]) == 4
    assert sonar_sweep.count_increases([1,1,1,1,1]) == 0
    assert sonar_sweep.count_increases([1,3,1,3,1]) == 2
    assert sonar_sweep.count_increases([5,4,3,2,1]) == 0
    assert sonar_sweep.count_increases([5,2,3,4,5]) == 3

def test_sliding_window_sum():
    assert sonar_sweep.sliding_window_sum([199,200,208,210,200,207,240, 269,260, 263]) == [607,618,618,617,647,716,769,792]
    assert sonar_sweep.sliding_window_sum([1,2,3,4,5,6,7,8,9,10]) == [6,9,12,15,18,21,24,27]