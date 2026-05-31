import os

from neutron_tools.utilities import neut_utilities as ut

ntlogger = ut.get_ntlogger()

class files_file:
    """Class to represent a FISPACT files file"""
    def __init__(self, fpath: str):
        self.fpath = fpath
        self.lines = read_fispact_files_file(fpath) if fpath else []
        self.parameters = {}

    def __repr__(self):
        return f"files_file(fpath={self.fpath}, parameters={self.parameters})"
    
    def __str__(self):
        return f"files_file with parameters: {self.parameters}"
    
    def output_files_file(self, output_path: str):
        """Outputs the files_file object to a new file"""
        with open(output_path, "w") as f:
            for line in self.lines:
                f.write(line + "\n")
        ntlogger.info("wrote FISPACT files file to %s", output_path)
                

def process_files_file(lines) -> files_file:
    """Processes the lines of a FISPACT files file and extracts parameters"""
    files_file_obj = files_file("")  # Create an empty files_file object
    files_file_obj.lines = lines

    for line in lines:
        if line.startswith("#"):
            continue  # Skip comments
        elif line.strip() == "":
            continue  # Skip empty lines
        elif " " in line:
            line = line.strip()
            key, value = line.split(maxsplit=1)
            files_file_obj.parameters[key.strip()] = value.strip()
    return files_file_obj


def read_fispact_files_file(fpath: str) -> list[str]:
    """ reads a fispact files file and returns the data as a list of lines """
    ntlogger.info("reading FISPACT files file %s", fpath)
    if not os.path.exists(fpath):
        raise FileNotFoundError(f"FISPACT files file not found: {fpath}")

    if not os.path.isfile(fpath):
        raise ValueError(f"Path is not a file: {fpath}")

    try:
        lines = ut.get_lines(fpath)
    except Exception as e:
        raise IOError(f"Failed to read FISPACT files file {fpath}: {e}") from e

    ntlogger.info("loaded %d lines from FISPACT files file %s", len(lines), fpath)
    return lines

if __name__ == "__main__":
    lines = read_fispact_files_file("path/to/fispact_files_file.txt")