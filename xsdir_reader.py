import argparse
import neut_utilities as ut

class XSDir:
    def __init__(self):
        self.file_path = None
        self.datapath = None
        self.awr = {}
        self.directory = {}
        self.thermal_scattering = {}

    def __str__(self):
        return (
            f"Filename: {self.file_path}\n"
            f"Datapath: {self.datapath}\n"
            f"Number of AWR entries: {len(self.awr)}\n"
            f"Number of directory entries: {len(self.directory)}"
        )

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
            if line.strip().startswith("datapath"):
                return line.split("=")[1].strip()
        return None

    @staticmethod
    def _process_awr(lines):
        """Parse atomic weight ratios section into a dict."""
        awr_data = {}
        in_awr = False
        for line in lines:
            if line.strip().startswith("atomic_weight_ratios"):
                in_awr = True
                continue
            if in_awr:
                if line.strip().startswith("directory"):
                    break  # end of AWR section
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
    
        @staticmethod
    def _process_thermal(lines):
        """Parse thermal scattering data section if present."""
        thermal = {}
        in_thermal = False
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("thermal_scattering_data") or line.startswith("sab"):
                in_thermal = True
                continue
            if in_thermal:
                parts = line.split()
                if len(parts) < 2:
                    continue
                entry = parts[0]
                thermal[entry] = parts[1:]
        return thermal

    
def read_xsdir(fpath):
    xsdir_file = XSDir.from_file(fpath)
    return xsdir_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reads xsdir file")
    parser.add_argument("input", help="path to the xsdir file")
    args = parser.parse_args()

    read_xsdir(args.input)
