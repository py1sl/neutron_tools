"""
Reads MCNP ptrac output file
"""
# import datetime
import argparse
import logging as ntlogger
# import numpy as np
import neut_utilities as ut


class history():
    """ history class - contains all the events and data for a
        single monte carlo history.
    """

    def __init__(self):
        self.nps = 1
        self.events = []


class event():
    """ event class """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.type = ""
        self.u = 0
        self.v = 0
        self.w = 0
        self.wgt = 1.0
        self.energy = 1
        self.par = 1
        self.cell = None
        self.time = 0

    def __eq__(self, other):
        if not isinstance(other, event):
            return NotImplementedError
        same = True

        if self.x != other.x:
            same = False
        elif self.y != other.y:
            same = False
        elif self.z != other.z:
            same = False
        elif self.type != other.type:
            same = False
        elif self.u != other.u:
            same = False
        elif self.v != other.v:
            same = False
        elif self.w != other.w:
            same = False
        elif self.wgt != other.wgt:
            same = False
        elif self.par != other.par:
            same = False
        elif self.cell != other.cell:
            same = False
        elif self.time != other.time:
            same = False
        elif self.energy != other.energy:
            same = False

        return same


def remove_header(lines):
    """ splits lines into the header section and the tracks section """
    head = lines[:9]
    tracks = lines[9:]
    return head, tracks


def mean_num_events(hists):
    """ calculate mean number of events
       input is a list of history objects
       output is the mean number of events per history (float)
    """

    n_hist = float(len(hists))
    n_events = 0
    for hist in hists:
        n_events = n_events + len(hist.events)

    ave = n_events/n_hist
    return ave


def process_event(event_data):
    """ processes an event
        input is a list of all the event variables
        output is an event object
    """

    event_data = [float(i) for i in event_data]
    cur_event = event()
    cur_event.type = event_data[0]
    if len(event_data) == 16:
        cur_event.cell = event_data[2]
        cur_event.x = event_data[7]
        cur_event.y = event_data[8]
        cur_event.z = event_data[9]
        cur_event.u = event_data[10]
        cur_event.v = event_data[11]
        cur_event.w = event_data[12]
        cur_event.wgt = event_data[14]
        cur_event.energy = event_data[13]
        cur_event.par = event_data[3]
        cur_event.time = event_data[15]
    elif len(event_data) == 15:
        cur_event.cell = event_data[2]
        cur_event.x = event_data[6]
        cur_event.y = event_data[7]
        cur_event.z = event_data[8]
        cur_event.u = event_data[9]
        cur_event.v = event_data[10]
        cur_event.w = event_data[11]
        cur_event.wgt = event_data[13]
        cur_event.energy = event_data[12]
        cur_event.par = event_data[3]
        cur_event.time = event_data[14]
    else:
        cur_event.cell = event_data[3]
        cur_event.x = event_data[8]
        cur_event.y = event_data[9]
        cur_event.z = event_data[10]
        cur_event.u = event_data[11]
        cur_event.v = event_data[12]
        cur_event.w = event_data[13]
        cur_event.wgt = event_data[15]
        cur_event.energy = event_data[14]
        cur_event.par = event_data[4]
        cur_event.time = event_data[16]

    return cur_event


def process_tracks(tracks):
    """ processes the tracks section with the events
        input is a list
        output is a list of history objects
    """

    i = 0
    histories = []
    cur_history = None
    temp_line = ""

    while i < len(tracks):
        line = tracks[i]
        line = ut.string_cleaner(line)
        line = line.split(" ")

        # check if a new history
        if len(line) == 2 or len(line) == 3:
            if cur_history:
                histories.append(cur_history)
            cur_history = history()
            cur_history.nps = int(line[0])

        # check linelength to determine if a new event or a continuation
        # first event line of a history is shorter

        elif len(line) == 9:    # continuation of an event

            temp_line = temp_line + line
            event = process_event(temp_line)
            cur_history.events.append(event)

        else:    # first line of a new event
            temp_line = line

        i = i + 1

    # need to catch the last history
    histories.append(cur_history)

    return histories


def write_all_hists_to_vtk(hists):
    """ """
    for i, hist in enumerate(hists):
        fname = "hist_" + str(i) + ".vtk"
        write_hist_vtk(hist, fname)


def write_hist_vtk(hist, fname):
    """ """
    eve_count = len(hist.events)
    event_type = []
    x = []
    y = []
    z = []
    u = []
    v = []
    w = []
    erg = []
    time = []
    wgt = []
    par_type = []
    
    for event in hist.events:
        x.append(event.x)
        y.append(event.y)
        z.append(event.z)
        u.append(event.u)
        v.append(event.v)
        w.append(event.w)
        erg.append(event.energy)
        time.append(event.time)
        wgt.append(event.wgt)
        par_type.append(event.par)
        event_type.append(event.type)
        
    vtk_lines = ["# vtk DataFile Version 2.0",
                 "Unstructured grid Example",
                 "ASCII",
                 "",
                 "DATASET UNSTRUCTURED_GRID",
                 "POINTS " +str(eve_count) + " float"]
    
    for j, pos in enumerate(x):
        vtk_lines.append(str(x[j])+" "+str(y[j])+" "+str(z[j]))
        
    vtk_lines.append("CELL_TYPES " + str(eve_count))
    j = 0
    while j < eve_count:
        j = j + 1
        vtk_lines.append("1")
    
    vtk_lines.append("POINT_DATA " + str(eve_count))    
    vtk_lines.append("SCALARS energy float 1")
    vtk_lines.append("LOOKUP_TABLE default")
    for j, pos in enumerate(erg):
        vtk_lines.append(str(erg[j]))
        
    vtk_lines.append("SCALARS weight float 1")
    vtk_lines.append("LOOKUP_TABLE default")
    for j, pos in enumerate(wgt):
        vtk_lines.append(str(wgt[j]))
    
    vtk_lines.append("SCALARS time float 1")
    vtk_lines.append("LOOKUP_TABLE default")
    for j, pos in enumerate(time):
        vtk_lines.append(str(time[j]))        
    
    vtk_lines.append("SCALARS particle float 1")
    vtk_lines.append("LOOKUP_TABLE default")
    for j, pos in enumerate(par_type):
        vtk_lines.append(str(par_type[j]))
    
    vtk_lines.append("SCALARS event float 1")
    vtk_lines.append("LOOKUP_TABLE default")
    for j, pos in enumerate(event_type):
        vtk_lines.append(str(event_type[j]))
        
    vtk_lines.append("VECTORS vectors float")
    for j, pos in enumerate(u):
        vtk_lines.append(str(u[j]) +" " + str(v[j]) + " " + str(w[j]))
    
    ut.write_lines(fname, vtk_lines)


def read_ptrac(path):
    """ reads and processes MCNP ptrac file
        input is a path to a file
        returns a list of histories
    """

    ntlogger.info('Reading MCNP ptrac file: %s', path)
    ofile_data = ut.get_lines(path)

    head, tracks = remove_header(ofile_data)

    hist = process_tracks(tracks)

    return hist


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Read MCNP output file")
    parser.add_argument("input", help="path to the output file")
    args = parser.parse_args()
