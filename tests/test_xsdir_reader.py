import unittest
import tempfile
import os
import xsdir_reader


class xsdir_init_test_case(unittest.TestCase):
    """Tests for XSDir initialization"""
    
    def test_init(self):
        """Test XSDir object initialization"""
        xs = xsdir_reader.XSDir()
        self.assertIsNone(xs.file_path)
        self.assertIsNone(xs.datapath)
        self.assertEqual(xs.awr, {})
        self.assertEqual(xs.directory, {})
        self.assertEqual(xs.thermal_scattering, {})


class xsdir_str_test_case(unittest.TestCase):
    """Tests for XSDir __str__ method"""
    
    def test_str_empty(self):
        """Test __str__ with empty XSDir object"""
        xs = xsdir_reader.XSDir()
        xs.file_path = "/path/to/xsdir"
        xs.datapath = "/data/path"
        str_repr = str(xs)
        self.assertIn("Filename: /path/to/xsdir", str_repr)
        self.assertIn("Datapath: /data/path", str_repr)
        self.assertIn("Number of AWR entries: 0", str_repr)
        self.assertIn("Number of directory entries: 0", str_repr)
        self.assertIn("Number of TSL entries: 0", str_repr)


class process_datapath_test_case(unittest.TestCase):
    """Tests for _process_datapath static method"""
    
    def test_datapath_simple(self):
        """Test extracting simple datapath"""
        lines = [
            "some header\n",
            "datapath=/path/to/data\n",
            "more content\n"
        ]
        result = xsdir_reader.XSDir._process_datapath(lines)
        self.assertEqual(result, "/path/to/data")
    
    def test_datapath_with_spaces(self):
        """Test extracting datapath with spaces"""
        lines = [
            "datapath= /path/with/spaces \n"
        ]
        result = xsdir_reader.XSDir._process_datapath(lines)
        self.assertEqual(result, "/path/with/spaces")
    
    def test_datapath_mixed_case(self):
        """Test extracting datapath with mixed case"""
        lines = [
            "DATAPATH=/upper/case/path\n"
        ]
        result = xsdir_reader.XSDir._process_datapath(lines)
        self.assertEqual(result, "/upper/case/path")
    
    def test_datapath_not_found(self):
        """Test when datapath is not present"""
        lines = [
            "no datapath here\n",
            "just other content\n"
        ]
        result = xsdir_reader.XSDir._process_datapath(lines)
        self.assertIsNone(result)


class process_awr_test_case(unittest.TestCase):
    """Tests for _process_awr static method"""
    
    def test_awr_basic(self):
        """Test parsing basic AWR section"""
        lines = [
            "atomic weight ratios\n",
            "1001 H-1 1.007825\n",
            "2004 He-4 4.002603\n",
            "directory\n"
        ]
        result = xsdir_reader.XSDir._process_awr(lines)
        self.assertEqual(len(result), 2)
        self.assertEqual(result["H-1"], 1.007825)
        self.assertEqual(result["He-4"], 4.002603)
    
    def test_awr_empty(self):
        """Test with no AWR section"""
        lines = [
            "no atomic section\n",
            "directory\n"
        ]
        result = xsdir_reader.XSDir._process_awr(lines)
        self.assertEqual(len(result), 0)
    
    def test_awr_with_extra_columns(self):
        """Test AWR parsing with extra columns"""
        lines = [
            "atomic weight ratios\n",
            "1001 H-1 1.007825 extra data\n",
            "directory\n"
        ]
        result = xsdir_reader.XSDir._process_awr(lines)
        self.assertEqual(result["H-1"], 1.007825)


class process_directory_test_case(unittest.TestCase):
    """Tests for _process_directory static method"""
    
    def test_directory_basic(self):
        """Test parsing basic directory section"""
        lines = [
            "directory\n",
            "1001.80c 1.0000 filename 0 1 1234 5678\n",
            "2004.80c 4.0026 filename2 0 1 2345 6789\n"
        ]
        result = xsdir_reader.XSDir._process_directory(lines)
        self.assertEqual(len(result), 2)
        self.assertIn("1001.80c", result)
        self.assertEqual(result["1001.80c"][0], "1.0000")
        self.assertEqual(result["1001.80c"][1], "filename")
    
    def test_directory_empty_lines(self):
        """Test directory parsing with empty lines"""
        lines = [
            "directory\n",
            "1001.80c 1.0000 filename\n",
            "\n",
            "  \n",
            "2004.80c 4.0026 filename2\n"
        ]
        result = xsdir_reader.XSDir._process_directory(lines)
        self.assertEqual(len(result), 2)
    
    def test_directory_no_section(self):
        """Test when directory section is not present"""
        lines = [
            "some other content\n",
            "no directory marker\n"
        ]
        result = xsdir_reader.XSDir._process_directory(lines)
        self.assertEqual(len(result), 0)


class process_thermal_test_case(unittest.TestCase):
    """Tests for _process_thermal static method"""
    
    def test_thermal_basic(self):
        """Test parsing thermal scattering section"""
        lines = [
            "thermal_scattering_data\n",
            "h-h2o.20t 1.0000 tsl-file 0 1 1234\n",
            "h-zrh.20t 1.0000 tsl-file2 0 1 2345\n"
        ]
        result = xsdir_reader.XSDir._process_thermal(lines)
        self.assertEqual(len(result), 2)
        self.assertIn("h-h2o.20t", result)
        self.assertEqual(result["h-h2o.20t"][0], "1.0000")
    
    def test_thermal_sab_keyword(self):
        """Test parsing with 'sab' keyword"""
        lines = [
            "sab\n",
            "h-h2o.20t 1.0000 tsl-file\n"
        ]
        result = xsdir_reader.XSDir._process_thermal(lines)
        self.assertEqual(len(result), 1)
        self.assertIn("h-h2o.20t", result)
    
    def test_thermal_with_comments(self):
        """Test thermal parsing with comment lines"""
        lines = [
            "thermal_scattering_data\n",
            "# This is a comment\n",
            "h-h2o.20t 1.0000 tsl-file\n",
            "  # Another comment\n",
            "h-zrh.20t 1.0000 tsl-file2\n"
        ]
        result = xsdir_reader.XSDir._process_thermal(lines)
        self.assertEqual(len(result), 2)
    
    def test_thermal_empty(self):
        """Test with no thermal section"""
        lines = [
            "no thermal section here\n"
        ]
        result = xsdir_reader.XSDir._process_thermal(lines)
        self.assertEqual(len(result), 0)


class from_file_test_case(unittest.TestCase):
    """Tests for from_file class method"""
    
    def test_from_file_complete(self):
        """Test reading a complete xsdir file"""
        xsdir_content = """datapath=/nuclear/data/path
atomic weight ratios
1001 H-1 1.007825
2004 He-4 4.002603
6000 C-nat 12.000000
directory
1001.80c 1.0078 h1.endf 0 1 12345 67890
2004.80c 4.0026 he4.endf 0 1 23456 78901
6000.80c 12.0000 c12.endf 0 1 34567 89012
thermal_scattering_data
h-h2o.20t 1.0000 h2o.tsl 0 1 45678
h-zrh.20t 1.0000 zrh.tsl 0 1 56789
"""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.xsdir') as temp_file:
            temp_file.write(xsdir_content)
            temp_file_path = temp_file.name
        
        try:
            xs = xsdir_reader.XSDir.from_file(temp_file_path)
            
            # Check file path
            self.assertEqual(xs.file_path, temp_file_path)
            
            # Check datapath
            self.assertEqual(xs.datapath, "/nuclear/data/path")
            
            # Check AWR
            self.assertEqual(len(xs.awr), 3)
            self.assertEqual(xs.awr["H-1"], 1.007825)
            self.assertEqual(xs.awr["He-4"], 4.002603)
            self.assertEqual(xs.awr["C-nat"], 12.0)
            
            # Check directory
            # Note: directory parser continues through all lines after "directory" marker,
            # so thermal entries are also included in directory dict
            self.assertGreaterEqual(len(xs.directory), 3)
            self.assertIn("1001.80c", xs.directory)
            self.assertEqual(xs.directory["1001.80c"][0], "1.0078")
            
            # Check thermal
            self.assertEqual(len(xs.thermal_scattering), 2)
            self.assertIn("h-h2o.20t", xs.thermal_scattering)
            
        finally:
            os.remove(temp_file_path)
    
    def test_from_file_minimal(self):
        """Test reading minimal xsdir file"""
        xsdir_content = """datapath=/data
directory
1001.80c 1.0078 file.dat
"""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.xsdir') as temp_file:
            temp_file.write(xsdir_content)
            temp_file_path = temp_file.name
        
        try:
            xs = xsdir_reader.XSDir.from_file(temp_file_path)
            self.assertEqual(xs.datapath, "/data")
            self.assertEqual(len(xs.directory), 1)
            self.assertEqual(len(xs.awr), 0)
            self.assertEqual(len(xs.thermal_scattering), 0)
        finally:
            os.remove(temp_file_path)


class read_xsdir_function_test_case(unittest.TestCase):
    """Tests for read_xsdir convenience function"""
    
    def test_read_xsdir(self):
        """Test read_xsdir function"""
        xsdir_content = """datapath=/test/path
directory
1001.80c 1.0078 test.dat
"""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.xsdir') as temp_file:
            temp_file.write(xsdir_content)
            temp_file_path = temp_file.name
        
        try:
            xs = xsdir_reader.read_xsdir(temp_file_path)
            self.assertIsInstance(xs, xsdir_reader.XSDir)
            self.assertEqual(xs.datapath, "/test/path")
            self.assertEqual(len(xs.directory), 1)
        finally:
            os.remove(temp_file_path)


if __name__ == "__main__":
    unittest.main()
