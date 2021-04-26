"""
Reads MCNP ptrac output file
"""
# import datetime
import argparse
import logging
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
        self.e = 0
        self.wgt = 1.0
        self.energy = 1
        self.par = 1
        self.cell = None


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
    cur_event.cell = event_data[3]
    cur_event.x = event_data[8]
    cur_event.y = event_data[9]
    cur_event.z = event_data[10]
    cur_event.u = event_data[11]
    cur_event.v = event_data[12]
    cur_event.w = event_data[13]
    cur_event.wgt = event_data[14]
    cur_event.energy = event_data[15]
    cur_event.par = event_data[0]

    return cur_event


def process_tracks(tracks):
    """ processes the tracks section with the events
        input is a list
        output is a list of history objects
    """

    i = 0
    histories = []
    cur_history = None

    while i < len(tracks):
        line = tracks[i]
        line = ut.string_cleaner(line)
        line = line.split(" ")

        # check if a new history
        if len(line) == 2:
            if cur_history:
                histories.append(cur_history)
            cur_history = history()
            cur_history.nps = line[0]

        # check linelength to determine if a new event or a continuation
        # first event line of a history is shorter
        elif len(line) == 7 or len(line) == 6:
            temp_line = line
            temp_line.append("0")

        elif len(line) == 8:    # first line of a new event
            temp_line = line

        elif len(line) == 9:    # continuation of an event

            temp_line = temp_line + line
            event = process_event(temp_line)
            cur_history.events.append(event)

        i = i + 1

    # need to catch the last history
    histories.append(cur_history)

    return histories


def read_ptrac(path):
    """ reads and processes MCNP ptrac file
        input is a path to a file
        returns a list of histories
    """

    logging.info('Reading MCNP ptrac file: %s', path)
    ofile_data = ut.get_lines(path)

    head, tracks = remove_header(ofile_data)

    hist = process_tracks(tracks)

    return hist


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Read MCNP output file")
    parser.add_argument("input", help="path to the output file")
    args = parser.parse_args()
