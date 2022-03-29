"""
Reads Cinder output file
"""
import argparse
import logging as ntlogger
import numpy as np
import pandas as pd
import neut_utilities as ut


class cinder_output():
    """ cinder output data"""
    def __init__(self):
        """ define data"""
        self.file_name = ""
        self.table1 = None
        self.table2 = None
        self.table3 = None
        self.table4 = None
        self.table5 = None
        self.table6 = None


def process_tab4_headings(headings):
    """processes the headings
       joins the time and time unit to a single string
    """

    all_headings = []
    for hr in headings:
        hr = hr.split()
        all_headings = all_headings + hr

    headings = [all_headings[0], all_headings[1]]
    x = 2
    while x < len(all_headings):
        head = all_headings[x]
        if head != "NUCLIDE" and head !="HALFLIFE,S":
            headings.append(str(head) + str(all_headings[x+1]))
        x = x +2
    
    # print(headings)
    return headings

   
def times_to_cumulative(time_list):
    """ convert time list to cumulative time """
    ctimes = []
    
    for time in time_list:
        tvalue = float(time[:-1])
        tunit = time[-1]
        
        if tunit == "S":
            ctimes.append(tvalue)
        elif tunit == "D":
            ctimes.append(tvalue*24*3600)
        elif tunit == "Y":
            ctimes.append(tvalue*365.25*24*3600)
        else:
            raise ValueError(" Time unit not recognised:", tunit)

    ctimes = np.array(ctimes)
    ctimes = np.cumsum(ctimes)
    
    return ctimes

    
def read_tab1(lines):
    """"""
    return lines
    
    
def read_tab2(lines):
    """ """
    return lines
    
    
def read_tab3(lines):
    """ """
    return lines

    
def read_tab4(lines):
    """ reads TOTAL ACTIVITY table 4"""
    start_ind = ut.find_ind(lines, "TOTAL ACTIVITY")
    end_ind = ut.find_ind(lines, "DECAY POWER DENSITY")
    
    all_data = lines[start_ind+4:end_ind-1]
    
    data = []
    data_block = []
    block_ind = []
    start_ind = 0
    headings = []
    
    for i, line in enumerate(all_data):
        if "TABLE   4 (CONTINUED AT SUBSEQUENT TIMES" in line:
            block_ind.append(i)
    # add 
    block_ind.append(-1)
    
    for i, block in enumerate(block_ind):
        #print("block:", i)
        end_ind = block
        datablock = all_data[start_ind:end_ind]
        start_ind = block
        nuc_count = 0
        data_block = []
        
        for row in datablock:
            if "NUCLIDE" in row and nuc_count < 1 :
                headings.append(row)
                
                nuc_count = nuc_count + 1
            elif "+" == row[0] or "<" in row or "UP" in row or "DOWN" in row or "NUCLIDE" in row or "TABLE" in row:
                x=""
            elif "TOTAL" in row:
                break
                
            else:
                data_row = []
                data_row.append(ut.string_cleaner(row[:10]))
              
                row = ut.string_cleaner(row[10:])
                data_row = data_row + [float(item) for item in row.split()]
                data_block.append(data_row)
        
        data_block = pd.DataFrame(data_block, index = [item[0] for item in data_block])
        data_block.drop(data_block.columns[[0, 1]], axis=1, inplace=True)
        data.append(data_block)
        
    headings = process_tab4_headings(headings)
    headings = times_to_cumulative(headings[2:])

    df = pd.concat(data, axis=1, sort=False)
    df.columns = headings
     
    return df


def read_tab5(lines):
    """ """
    return lines


def read_tab6(lines):
    """ """
    return lines


def convert_timestep_units(table, unit="d"):
    """ """
    cols = table.columns
    unit = unit.lower()
    
    if unit == "d":
        cols = cols / (3600*24)
    elif unit == "y":
        cols = cols / (3600*24*365.25)
    elif unit == "h":
        cols = cols / 3600
        
    else:
        raise ValueError

    table.columns = cols
    return table


def read_output_file(path):
    ntlogger.info('Reading Cinder output file: %s', path)
    ofile_data = ut.get_lines(path)
    cinder_op = cinder_output()

    # general
    cinder_op.file_name = path
    cinder_op.table4 = read_tab4(ofile_data)
    
    return cinder_op    
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Read Cinder output file")
    parser.add_argument("input", help="path to the output file")
    args = parser.parse_args()

    read_output_file(args.input)
