"""utility functions for use by neutron tools"""
import logging


def setup_logging():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info("Starting calculation")
    

def write_lines(path, lines):
    f = open(path, 'w')
    for l in lines:
        f.write(l)
        f.write("\n")
    f.close()

    
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
    for l in lines:
        i = i + 1
        if l[0:num] == text:
            return i - 1
    raise ValueError
    # TODO: add a catch if it doesnt find any match
    
    
def string_cleaner(text):
    """ returns cleaned up line"""
    text = text.strip()
    text = " ".join(text.split())
    return text
 
 
def find_first_non_zero(val_list):
    """ """
    for i, val in enumerate(val_list):
        if val > 0:
            return i
            break