"""
Reads MCNP output file
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import sys
import argparse


class MCNPOutput():
    """ MCNP output data"""
    def __init__(self):
        """ define data"""
        self.file_name = ""
        self.version = ""
        self.date = ""
        self.start_time = ""
        self.cell_mass_volume = []
        self.surface_area = []
        self.num_tallies = 1
        self.num_rendevous = 1
        self.tally_data = []
        self.summary_data = []
        self.tfc_data = []
        

class MCNP_tally_data():
    """ data for an individual tally """
    def __init__(self):
        self.number = 1
        self.type = 1
        self.particle = "neutron"
        self.nps = 1 
        # for type 4

        # for type 5 tallies
        self.x = None
        self.y = None
        self.z = None
        self.cell_scores = None
        self.uncoll_flux = None
        self.uncoll_err = None
        # for type 6
        # for type 8
        # general
        self.result = []
        self.err = []
        self.eng = []
        self.stat_tests = None




class MCNP_summary_data():
    """ data for an individual tally """
    def __init__(self):
        self.number = 1
        self.type = 1


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
    # TODO: add a catch if it doesnt find any match

def get_version(data):
    """ """
    return 1


def get_cell_mass(data):
    """ """
    return 1


def get_surface_area(data):
    """ """
    return 1


def get_num_tallies(data):
    """ """
    return 1


def get_num_rendevous(data):
    """ """
    return 1


def get_summary(data, ptype, rnum):
    """ """
    return 1


def get_tally(lines, tnum, rnum=-1):
     """reads the lines and extracts the  tally results"""
     
     tally_data = MCNP_tally_data()
     tally_data.number = tnum

     # todo add ability to do all rendevous
     # reduce to only the final result set
     term_line = find_line("      run terminated when", lines, 25)
     lines = lines[term_line:]

     # reduce to only the tally results section
     fline = "1tally" + ((9-len(str(tnum)))*" ")
     res_start_line = find_line(fline + str(tnum), lines, 15)

     tally_data.particle = lines[res_start_line+2][24:33]
     tally_data.nps = lines[res_start_line][28:40]
     tally_data.type = lines[res_start_line + 1][22]
     
     lines = lines[res_start_line + 1:]
     tal_end_line = find_line("1tally", lines, 6)
     lines = lines[:tal_end_line-1]

     write_lines("tally_test.txt", lines) # temp remove

     # debug
     print("")
     print(tnum)
     print(term_line)
     print(res_start_line)
     print(tal_end_line)
     print(tally_data.particle)
     print(tally_data.nps)
     print(tally_data.type)
     print("")

     # depending on tally type choose what to do now
     if tally_data.type == "4" or tally_data.type == "6":
         print("volume")

         # if volume type, need to find how which cells
         cells = []
         vols = []

         if "volumes" in lines[3]:
             for l in lines[3:]:
                 if l == "":
                     break
                  
                 elif "cell:" in l:
                     l = l.strip()
                     l = l.split()
                     data = l[1:]
                     for c in data:
                         cells.append(c)
         # now need to get actual data
         c_count = 0
         while c_count < len(cells):
             erg = [0.0]
             ph = []
             err = [0.0]
             c_count = c_count + 1
     elif tally_data.type == "5":
         print("type 5")

         # read detector position
         loc_line_id=find_line(" detector located", lines, 17)
         loc_line = lines[loc_line_id]
         loc_line = loc_line.split("=")[1]
         loc_line = loc_line.split(" ")
         tally_data.x = loc_line[1]
         tally_data.y = loc_line[2]
         tally_data.z = loc_line[3]
         res_line = lines[loc_line_id + 1]

         # check if energy dependant
         if res_line == "      energy   ":
             print("energy dependant")
             loc_line_id2=find_line(" detector located", lines[loc_line_id+1:], 17)
             erg_lines = lines[loc_line_id + 2:loc_line_id + loc_line_id2-1]
             for l in erg_lines:
                 l=l.strip()
                 l=l.split(" ")
                 tally_data.eng.append(float(l[0]))
                 tally_data.result.append(float(l[3]))
                 tally_data.err.append(float(l[4]))
             
         else:
             res_line = res_line.split(" ")[-2:]
             tally_data.result.append(res_line[0])
             tally_data.err.append(res_line[1])

     elif tally_data.type == "1" or tally_data.type == "2":
         print("surface")
     elif tally_data.type == "8":
         print("pulse height tally")

     stat_res_line_id = find_line(" passed", lines, 7)
     stat_line = lines[stat_res_line_id]
     stat_line = stat_line.strip()
     stat_line = " ".join(stat_line.split())
     stat_line = stat_line.split(" ")[1:]
    

     return tally_data


def read_output_file(path, tnum):
    """ """

    ofile_data = get_lines(path)
    mc_data = MCNPOutput()

    td1 = get_tally(ofile_data, tnum) # temporary remove later
    return td1


def plot_hist(res, ptype, xlog=True, ylog=True, leth=False):
    """ """
    a = res[0]
    w = res[1][1:]
    w.append(0.0)
    x = res[0][1:]

    if not leth:
        n, bins, patches = plt.hist(x, bins=a, weights=w, histtype='step',
                                    label=ptype)
    else:
        leth_v = a[0]
# TODO : sort lethagy plot out
        n, bins, patches = plt.hist(leth_v, bins=a, weights=w, histtype='step',
                                    label=ptype)
    if xlog:
        plt.xscale('log')
    if ylog:
        plt.yscale('log')
    plt.xlabel("Energy (MeV)")
    if not leth:
        plt.ylabel("Particle flux 1/cm2/s/source proton")
    if leth:
        plt.ylabel("Lethargy Particle flux 1/cm2/s/MeV/source proton")
    plt.legend(loc='upper left')

    plt.show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Read MCNP output file")
    parser.add_argument("input", help="path to the output file")
    args = parser.parse_args()

    read_output_file(args.input)
