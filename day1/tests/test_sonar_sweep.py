import pytest
from .. import sonar_sweep

def test_count_increase():
    assert sonar_sweep.count_increases([1,2,3,4,5]) == 4
    assert sonar_sweep.count_increases([1,1,1,1,1]) == 0
    assert sonar_sweep.count_increases([1,3,1,3,1]) == 2
    assert sonar_sweep.count_increases([5,4,3,2,1]) == 0
    assert sonar_sweep.count_increases([5,2,3,4,5]) == 3