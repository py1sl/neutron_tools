import argparse
from neutron_tools.utilities import neut_utilities as ut

class XSDir:
    def __init__(self):
        self.file_path = None
        self.datapath = None
        self.awr = {}
        self.directory = {}

    def __str__(self):
        return (
            f"Filename: {self.file_path}\n"
            f"Datapath: {self.datapath}\n"
            f"Number of AWR entries: {len(self.awr)}\n"
            f"Number of directory entries: {len(self.directory)}"
        )
    
    def is_nuclide_in_directory(self, nuclide_key):
        """Check if a nuclide is in the directory regardless of library."""
        nuclide = nuclide_key.split(".")[0]
        for key in self.directory.keys():
            if key.split(".")[0] == nuclide:
                return True
        return False
    
    def get_all_nuclide_entries(self, nuclide_key):
        """Get all entries for a nuclide regardless of library."""
        nuclide = nuclide_key.split(".")[0]
        entries = []
        for key, value in self.directory.items():
            if key.split(".")[0] == nuclide:
                entries.append((key, value))
        return entries

    def is_nuclide_in_directory_and_library(self, nuclide_key):
        """Check if a nuclide with a specific library is in the directory."""
        return nuclide_key in self.directory
    
    def get_nuclide_with_type(self, zaid, lib_type="c"):
        """Get all entries for a nuclide with a specific library type."""
        found_entries = []
        for key, entry in self.directory.items():
            if key.startswith(zaid) and key.endswith(lib_type):
                found_entries.append((key, entry))
        if found_entries:
            return found_entries
        return None
    
    def get_all_library_entries(self, lib=".70c"):
        """Get all entries for a specific library."""
        entries = []
        for key, entry in self.directory.items():
            if key.endswith(lib):
                entries.append((key, entry))
        return entries

    @classmethod
    def from_file(cls, fpath):
        """Read and parse an xsdir file into an XSDir object."""
        lines = ut.get_lines(fpath)
        xs = cls()
        xs.file_path = fpath

        # Find datapath
        xs.datapath = cls._process_datapath(lines)

        # Parse sections
        xs.awr = cls._process_awr(lines)
        xs.directory = cls._process_directory(lines)
  
        return xs

    @staticmethod
    def _process_datapath(lines):
        """Extract datapath= line from xsdir."""
        for line in lines:
            line = line.lower()
            if line.strip().startswith("datapath"):
                datapath = line.split("=")[1].strip()
                return datapath
        return None

    @staticmethod
    def _process_awr(lines):
        """Parse atomic weight ratios section into a dict."""
        awr_data = {}
        in_awr = False
        for line in lines:
            line = line.strip()
            if line.startswith("atomic"):
                in_awr = True
                continue
            if in_awr:
                if line.startswith("directory"):
                    break 
                parts = line.split()
                if len(parts) >= 3:
                    awr_data[parts[1]] = float(parts[2])
        return awr_data

    @staticmethod
    def _process_directory(lines):
        """Parse the directory section into a dict."""
        directory = {}
        in_dir = False
        for line in lines:
            if line.strip().startswith("directory"):
                in_dir = True
                continue
            if in_dir:
                parts = line.split()
                if len(parts) < 2:
                    continue
                isotope = parts[0]
                directory[isotope] = parts[1:]
        return directory


def read_xsdir(fpath):
    xsdir_file = XSDir.from_file(fpath)
    return xsdir_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads xsdir file")
    parser.add_argument("input", help="path to the xsdir file")
    args = parser.parse_args()

    read_xsdir(args.input)
