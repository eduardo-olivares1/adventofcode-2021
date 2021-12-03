import os

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
            arr.append(line.rstrip())

    return arr

def get_data_filepath(basedir, folder,filename):
    filepath = os.path.join(basedir, "data", folder, filename)
    return filepath