"""Helper functions for https://adventofcode.com/2021/day/1 solution

"""


def count_increases(arr):
    """Count the number of elements that are larger that the previous element in an array.

    Parameters
    ----------
    arr : list
        List of unordered integers.

    Returns
    -------
    int
        Number of elements that are larger than the previous measurement in the given array.
    """
    increase_count = 0
    for i in range(0, len(arr)):
        # Begin counting after the first element in the list
        if i > 0:
            # Check if element is larger than last
            if arr[i] > arr[i - 1]:
                # Increase the count
                increase_count += 1
            # Check if element is smmaller than last
            elif arr[i] < arr[i - 1]:
                pass
            # Check if element is equal to the last
            elif arr[i] == arr[i - 1]:
                pass
        # Don't count if the index is the first element
        elif i == 0:
            pass

    return increase_count


def file_to_list(filepath):
    """Create a list from a file. Convert each line in the file into an element in the list.

    Parameters
    ----------
    filepath : str
        Path to file

    Returns
    -------
    list
        List of file lines. Each line from the file is appended to the list.
    """
    arr = []

    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            arr.append(int(line.rstrip()))

    return arr


def sliding_window_sum(arr):
    """Takes an array and sums the starting element and next two elements for each element.

    Parameters
    ----------
    arr : list
        Unordered list of integers.

    Returns
    -------
    list
        List of summed elements.
    """
    # Empty list to append values to
    sliding_window_arr = []

    for i in range(0, len(arr)):
        try:
            # Sum the next two elements for each element in the list
            sum_two_ahead = arr[i] + arr[i + 1] + arr[i + 2]
            sliding_window_arr.append(sum_two_ahead)
        # If the index is out of range that means that that is the max that can be summed.
        except IndexError:
            break

    return sliding_window_arr
