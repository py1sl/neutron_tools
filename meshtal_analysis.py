# -*- coding: utf-8 -*-
"""
mesh tally tools

Created on Fri Apr 20 08:26:06 2018

@author: gai72996
"""

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import argparse
import logging


class meshtally:
    idnum = None
    ptype = None
    x_bounds = None
    y_bounds = None
    z_bounds = None
    e_bounds = None
    data = None
    x_mids = None
    y_mids = None
    z_mids = None
    ctype = None


def rel_err_hist(data):
    """ """
    data = np.array(data).astype(float)
    rel_errs = []
    for r in data:
        if r[5] != 0:
            rel_errs.append(r[5])

    bins = (0, 0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
            0.7, 0.8, 0.9, 1)
    plt.hist(rel_errs, bins)
    plt.xlabel("Relative error")
    plt.ylabel("Number of voxels")
    plt.show()


# TODO: need to deal with energy bins
# TODO: need to generalize to any axis
def plot_slice(mesh, value, plane="XY", lmin=1e-15, lmax=1e-3, fname=None, err = True):
    """ """
    plt.clf()
    data = mesh.data
    data = np.array(data).astype(float)
     

    if plane == "XZ":
        midx = mesh.x_mids
        midy = mesh.z_mids
        v_bounds = mesh.y_bounds
        if mesh.ctype == "6col":
            ipos = 1
            jpos = 3
            vpos = 2
            data_pos = 4
        elif mesh.ctype == "5col":
            ipos = 0
            jpos = 2
            vpos = 1
            data_pos = 3
        ilab = "X co-ord (cm)"
        jlab = "Z co-ord (cm)"
    elif plane == "XY":
        midx = mesh.x_mids
        midy = mesh.y_mids
        v_bounds = mesh.z_bounds
        if mesh.ctype == "6col":
            ipos = 1
            jpos = 2
            vpos = 3
            data_pos = 4
        elif mesh.ctype == "5col":
            ipos = 0
            jpos = 1
            vpos = 2
            data_pos = 3
        ilab = "X co-ord (cm)"
        jlab = "Y co-ord (cm)"
    elif plane == "YZ":
        midx = mesh.y_mids
        midy = mesh.z_mids
        v_bounds = mesh.x_bounds
        if mesh.ctype == "6col":
            ipos = 2
            jpos = 3
            vpos = 1
            data_pos = 4
        elif mesh.ctype == "5col":
            ipos = 1
            jpos = 2
            vpos = 0
            data_pos = 3
        ilab = "Y co-ord (cm)"
        jlab = "Z co-ord (cm)"

    # find closest mid point
    pos = 0
    
    for i, v in enumerate(v_bounds):
        if value > float(v):
            pos = i
    
    value = (float(v_bounds[pos]) + float(v_bounds[pos + 1])) / 2.0

    # now find the slice values
    vals = np.zeros((len(midy), len(midx)))
    err_vals = np.zeros((len(midy), len(midx)))

    for r in data:
        if (r[vpos]) == value:
            i, = np.where(midx == r[ipos])
            j, = np.where(midy == r[jpos])

            vals[j, i] = r[data_pos]
            err_vals[j, i] = r[data_pos + 1]


    # now plot
    if err :
        plt.subplot(2, 1, 2)
        plt.pcolormesh(midx, midy, err_vals)
        title = plane + " Slice at " + str(value) + " of mesh " + str(mesh.idnum) + " rel err"
        plt.title(title)
        plt.colorbar()
        plt.xlabel(ilab)
        plt.ylabel(jlab)
        plt.xlim(xmin=min(midx), xmax=max(midx))
        plt.ylim(ymin=min(midy), ymax=max(midy))

        plt.subplot(2, 1, 1)
        plt.tight_layout()
    
    plt.pcolormesh(midx, midy, vals, norm=colors.LogNorm(vmin=lmin, vmax=lmax))
    title = plane + " Slice at " + str(value) + " of mesh " + str(mesh.idnum)
    plt.title(title)
    
    plt.colorbar()
    plt.xlabel(ilab)
    plt.ylabel(jlab)
    plt.xlim(xmin=min(midx), xmax=max(midx))
    plt.ylim(ymin=min(midy), ymax=max(midy))

    if fname:
        plt.savefig(fname)
        logging.info("produced figure: %s", fname)
    else:
        plt.show()


# TODO:
def output_as_vtk():
    """ """
    print("not ready yet")


# TODO:
def plot_line():
    """ """
    print("not ready yet")


# TODO:
def pick_point(x, y, z, mesh):
    """ """
    print("not ready yet")

    # find closest mid point
    xpos = 0
    for i, v in enumerate(mesh.x_bounds):
        if x > float(v):
            xpos = i

    ypos = 0
    for i, v in enumerate(mesh.y_bounds):
        if y > float(v):
            ypos = i

    zpos = 0
    for i, v in enumerate(mesh.z_bounds):
        if z > float(v):
            zpos = i


# TODO:
def add_mesh(mesh1, mesh2):
    """ """
    print("not ready yet")


# TODO: need to deal with energy bins
def convert_to_3d_array(mesh):
    """ """
    data = mesh.data
    data = np.array(data).astype(float)

    midx = mesh.x_mids
    midy = mesh.y_mids
    midz = mesh.z_mids

    vals = np.zeros((len(midx), len(midy), len(midz)))
    err_vals = np.zeros((len(midx), len(midy), len(midz)))

    for r in data:
        i, = np.where(midx == r[1])
        j, = np.where(midy == r[2])
        k, = np.where(midz == r[3])

        vals[i, j, k] = r[4]
        err_vals[i, j, k] = r[5]

    return vals, err_vals


def calc_mid_points(bounds):
    """ """
    mids = []
    bounds = np.array(bounds).astype(float)
    i = 0
    while i < len(bounds) - 1:
        val = (bounds[i] + bounds[i+1]) / 2.0
        val = round(val, 5)
        mids.append(val)
        i = i + 1

    return mids


def count_zeros(mesh):
    """ counts number of voxels with a zero value"""
    count = 0
    for l in mesh.data:
        if float(l[4]) == 0.0:
            count = count + 1
    return count


def get_lines(path):
    with open(path) as f:
        lines = f.read().splitlines()
    f.close()
    return lines


def find_mesh_tally_numbers(data):
    """ find the differnt meshes in the file, the tally number
        and the line it starts on"""
    tdict = {}
    for i, l in enumerate(data):
        if "Mesh Tally Number" in l:
            talid = int(l.split(" ")[-1])
            tdict[talid] = i
    return tdict


def find_next_mesh(tnum, tdict):
    """ finds the start location of the next numerical mesh tally"""
    keylist = sorted(tdict.keys())
    if tnum == keylist[-1]:
        return -1
    else:
        for i, v in enumerate(keylist):
            if v == tnum:
                return tdict[keylist[i+1]]


def read_mesh(tnum, data, tdict):
    """ reads and individual mesh tally into mesh class """
    mesh = meshtally()
    mesh.idnum = tnum
    mesh.data = []
    mesh.ctype = "6col"
    logging.info("reading mesh number: %s ", str(tnum))
    # reduce data to just the selected mesh tally
    start_pos = tdict[tnum]
    end_pos = find_next_mesh(tnum, tdict)

    if end_pos == -1:
        mesh_data = data[start_pos:]
    else:
        mesh_data = data[start_pos:end_pos - 1]

    # read through and assign mesh variables
    in_data = False

    for v in mesh_data:
        if in_data:
            v = " ".join(v.split())
            mesh.data.append(v.split(" "))
        elif "X direction:" in v:
            v = " ".join(v.split())
            mesh.x_bounds = v.split(" ")[2:]
        elif "Y direction:" in v:
            v = " ".join(v.split())
            mesh.y_bounds = v.split(" ")[2:]
        elif "Z direction:" in v:
            v = " ".join(v.split())
            mesh.z_bounds = v.split(" ")[2:]
        elif "Energy bin boundaries:" in v:
            v = " ".join(v.split())
            mesh.e_bounds = v.split(" ")[3:]
        elif ("Energy         X         Y         Z     Result" in v):
            in_data = True
           
        elif "X         Y         Z     Result" in v:
            in_data = True
           
            mesh.ctype = "5col"
        elif "mesh tally." in v:
            v = " ".join(v.split())
            mesh.ptype = v.split(" ")[0]

    mesh.x_mids = calc_mid_points(mesh.x_bounds)
    mesh.y_mids = calc_mid_points(mesh.y_bounds)
    mesh.z_mids = calc_mid_points(mesh.z_bounds)

    return mesh


def read_mesh_tally_file(fpath):
    """ """
    logging.info('Reading MCNP meshtal file: %s', fpath)
    all_data = get_lines(fpath)
    tally_dict = find_mesh_tally_numbers(all_data)
    meshes = []
    for tnum in tally_dict.keys():
        mesh = read_mesh(tnum, all_data, tally_dict)
        meshes.append(mesh)
    return meshes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meshtally ploting")
    parser.add_argument("input", help="path to the Meshtal file")
    args = parser.parse_args()
    
    meshes=read_mesh_tally_file(args.input)
