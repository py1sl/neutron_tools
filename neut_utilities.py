"""utility functions for use by neutron tools"""
import logging
import numpy as np


def setup_ntlogger():
    """ setting up logging """
    ntlogger = logging.getLogger('nt_logger')
    ntlogger.setLevel(level=logging.DEBUG)
    return ntlogger


def write_lines(path, lines):
    """ writes lines list to file at path """
    with open(path, 'w') as f:
        for line in lines:
            f.write(f"{line}\n")


def get_lines(path):
    """ reads file at path and returns a list with 1 entry per line """
    with open(path) as f:
        lines = f.read().splitlines()
    return lines


def find_line(text, lines, num):
    """ finds first index of the line in lines where the text is present
        in the first num characters
    """
    for i, line in enumerate(lines):
        if line[:num] == text:
            return i
    raise ValueError(f"'{text}' not found within the first {num} characters of any line.")


def string_cleaner(text):
    """ returns cleaned up line """
    text = text.strip()
    text = " ".join(text.split())
    return text


def string_clean_and_split(text, spliter=" "):
    """ clean and split text on spaces """
    text = string_cleaner(text)
    text_list = text.split(spliter)
    return text_list


def find_ind(data, sub):
    """ finds first index in data which contains sub string """
    for i, s in enumerate(data):
        if sub in s:
            return i
    raise ValueError(f"The substring - '{sub}' was not found.")


def find_first_non_zero(val_list):
    """ finds the first non zero value in a list and returns its position """
    arr = np.asarray(val_list)
    nonzero_indices = np.nonzero(arr)[0]
    if nonzero_indices.size > 0:
        return int(nonzero_indices[0])
    else:
        return None


def find_first_zero(val_list):
    """ finds the first zero value in a list and returns its position """
    arr = np.asarray(val_list)
    zero_indices = np.where(arr == 0)[0]
    if zero_indices.size > 0:
        return int(zero_indices[0])
    else:
        return None


def get_list_dimensions(lst):
    """ finds dimensions of a list or list of lists etc"""
    if not isinstance(lst, list):
        return []

    dimensions = []
    while isinstance(lst, list):
        dimensions.append(len(lst))
        lst = lst[0] if len(lst) > 0 else []

    return dimensions


def text_replace(fname, old_string, new_string):
    """ replaces strings in place in a file """

    # replace string
    with open(fname, 'r') as file:
        data = file.read()
        data = data.replace(old_string, new_string)

    # output modified data
    with open(fname, 'w') as file:
        file.write(data)


def is_same_value(v1, v2, tolerance=1e-6):
    """ check if two float values are effectively equal within tolerance."""
    return abs(v1 - v2) < tolerance
