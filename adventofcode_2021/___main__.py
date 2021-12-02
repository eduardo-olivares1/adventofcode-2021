import os
import time
from day1 import sonar_sweep

def main():
    # Import data
    basedir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(basedir, "data", "input", "input.txt")
    input_list = sonar_sweep.file_to_list(filepath)

    # Day 1: Part 1 solution
    number_of_increases = sonar_sweep.count_increases(input_list)
    print(
        f"Number of measurements are larger than the previous measurement: {number_of_increases}"
    )

    # Day 1: Part 2 solution
    sliding_window_arr = sonar_sweep.sliding_window_sum(input_list)
    sliding_window_increases = sonar_sweep.count_increases(sliding_window_arr)
    print(
        f"Three-measurement Sliding Window - number of measurements are larger than the previous measurement: {sliding_window_increases} "
    )

if __name__ == '__main__':
    main()