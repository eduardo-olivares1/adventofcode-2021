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
                print(f"{arr[i]} (increased)")
                # Increase the count
                increase_count += 1
            # Check if element is smmaller than last
            elif arr[i] < arr[i - 1]:
                print(f"{arr[i]} (decreased)")
            # Check if element is equal to the last
            elif arr[i] == arr[i - 1]:
                print(f"{arr[i]} (no change)")
        # Don't count if the index is the first element
        elif i == 0:
            print(f"{arr[i]} (N/A - no previous measurement)")

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
