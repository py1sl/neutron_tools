"""utility functions for use by neutron tools"""
import logging


def setup_logging():
    msg_format = '%(levelname)s:%(message)s'
    logging.basicConfig(format=msg_format, level=logging.DEBUG)
    logging.info("Starting calculation")


def write_lines(path, lines):
    """ writes lines list to file at path """
    f = open(path, 'w')
    for line in lines:
        f.write("%s\n" % line)
    f.close()


def write_points_file(path, x, y, z):
    """ writes a visit compatible points file, from 3 lists
        each one a list of co-ords for a dimension
    """
    out_data = []
    out_data.append("x y z temp")
    for i, px in enumerate(x):
        py = y[i]
        pz = z[i]
        out_data.append(str(px) + " " + str(py) + " " + str(pz) + " 1")

    write_lines(path, out_data)


def get_lines(path):
    """ reads file at path and returns a list with 1 entry per line """
    with open(path) as f:
        lines = f.read().splitlines()
    f.close()
    return lines


def find_line(text, lines, num):
    """finds a index of the line in lines where the text is present in
       the first num characters
    """
    i = 0
    for line in lines:
        i = i + 1
        if line[0:num] == text:
            return i - 1
    raise ValueError
    # TODO: add a catch if it doesnt find any match


def string_cleaner(text):
    """ returns cleaned up line"""
    text = text.strip()
    text = " ".join(text.split())
    return text


def find_first_non_zero(val_list):
    """ finds the first non zero value in a list and returns its position """
    for i, val in enumerate(val_list):
        if (val > 0.0) or (val < 0.0):
            return i
            break
    return None


def find_first_zero(val_list):
    """ finds the first zero value in a list and returns its position"""
    for i, val in enumerate(val_list):
        if val == 0:
            return i
            break
    return None
