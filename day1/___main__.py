import os
import time
import sonar_sweep

basedir = os.path.abspath(os.path.dirname(__file__))
filepath = os.path.join(basedir, "data", "input", "input.txt")
input_list = sonar_sweep.file_to_list(filepath)
number_of_increases = sonar_sweep.count_increases(input_list)

print(
    f"Number of measurements are larger than the previous measurement: {number_of_increases}"
)
