import os
import time
from day1 import sonar_sweep
from day2 import dive
from advent_utils import file_help


def day1(input):
    # Convert input into list
    input_list = file_help.file_to_list(input)
    input_list = [int(x) for x in input_list]

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


def day2(input):
    # Convert input into list
    input_list = file_help.file_to_list(input)
    input_list = [x.split() for x in input_list]

    # Day 2: Part 1 solution
    my_sub = dive.Submarine()

    for command in input_list:
        my_sub.command(command[0], command[1])

    final_position = my_sub.get_sum()
    print(f"Final horizontal position by your final depth {final_position}")

    # Day 2: Part 2 solution
    my_sub2 = dive.SubmarineComplex()

    for command in input_list:
        my_sub2.command(command[0], command[1])

    final_position_complex = my_sub2.get_sum()
    print(f"Final horizontal position by your final depth {final_position_complex}")


def main():
    # Import data
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Day 1 Solution
    day1_file = file_help.get_data_filepath(basedir, "day1", "input.txt")
    day1(day1_file)

    # Day 2 Solution
    day2_file = os.path.join(basedir, "data", "day2", "input.txt")
    day2(day2_file)


if __name__ == "__main__":
    main()
