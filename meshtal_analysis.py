# -*- coding: utf-8 -*-
"""
mesh tally tools

"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import argparse
import logging
import pandas as pd
import neut_utilities as ut
mpl.use('Agg')


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


def rel_err_hist(df, fname=None):
    """ Plots a histogram of the relative errors"""

    df.hist(column='rel_err', bins=15)
    plt.xlabel("Relative error")
    plt.ylabel("Number of voxels")
    if fname:
        plt.savefig(fname)
        logging.info("produced figure: %s", fname)
    else:
        plt.show()


# TODO: need to deal with energy bins
# TODO: need to generalize to any axis
def plot_slice(mesh, value, plane="XY", lmin=1e-15, lmax=1e-3, fname=None,
               err=False, norm=1.0, erg=None):
    """ plots a slice through the mesh"""
    plt.clf()
    data = mesh.data
    # filter by energy if needed
    if erg:
        data = data[data["Energy"] == erg]

    if plane == "XZ":
        midx = mesh.x_mids
        midy = mesh.z_mids
        v_mid = mesh.y_mids
        v_ind = "y"
        # ipos = "x"
        # jpos = "z"
        ilab = "X co-ord (cm)"
        jlab = "Z co-ord (cm)"
    elif plane == "XY":
        midx = mesh.x_mids
        midy = mesh.y_mids
        v_mid = mesh.z_mids
        v_ind = "z"
        # ipos = "x"
        # jpos = "y"

        ilab = "X co-ord (cm)"
        jlab = "Y co-ord (cm)"
    elif plane == "YZ":
        midx = mesh.y_mids
        midy = mesh.z_mids
        v_mid = mesh.x_mids
        v_ind = "x"
        # ipos = "y"
        # jpos = "z"

        ilab = "Y co-ord (cm)"
        jlab = "Z co-ord (cm)"

    # find closest mid point
    value = find_nearest_mid(value, v_mid)

    # filter to just the values in the plane
    data = data[data[v_ind] == value]

    # now find the slice values
    vals = np.zeros((len(midy), len(midx)))
    err_vals = np.zeros((len(midy), len(midx)))

    for (_, __, x, y, ____, val, rerr) in data.itertuples():

        x = np.float64(x)
        y = np.float64(y)
        i, = np.where(midx == x)
        j, = np.where(midy == y)

        vals[j, i] = val
        err_vals[j, i] = rerr

    # now plot
    if err:
        plt.subplot(2, 1, 2)
        plt.pcolormesh(midx, midy, err_vals)
        title = plane + " Slice at " + str(value) + " of mesh "
        title = title + str(mesh.idnum) + " rel err"
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


def find_nearest_mid(value, mids):
    """ finds midpoint with shortest absoloute distance to the value """
    return mids[min(range(len(mids)), key=lambda i: abs(mids[i]-value))]


def convert_to_df(mesh):
    """ converts mesh.data in raw format to a pandas dataframe """
    if mesh.ctype == "6col":
        cols = ("Energy", "x", "y", "z", "value", "rel_err")
    elif mesh.ctype == "5col":
        cols = ("x", "y", "z", "value", "rel_err")

    data = pd.DataFrame(mesh.data, columns=cols)
    data["x"] = pd.to_numeric(data["x"], downcast="float")
    data["y"] = pd.to_numeric(data["y"], downcast="float")
    data["z"] = pd.to_numeric(data["z"], downcast="float")
    data["value"] = pd.to_numeric(data["value"], downcast="float")
    data["rel_err"] = pd.to_numeric(data["rel_err"], downcast="float")

    return data


def extract_line(mesh, p1, p2, erg=None):
    """ currently support lines varying along a single axis
        p1 and p2 are tuples of the form (x,y,z) and
        describe two points on the line
        currently only either x,y or z can vary between the two points
    """

    data = mesh.data
    # find and filter the constant axis
    if p1[0] == p2[0]:
        x = p1[0]
        x = find_nearest_mid(x, mesh.x_mids)
        data = data[data["x"] == x]
    if p1[1] == p2[1]:
        y = p1[1]
        y = find_nearest_mid(y, mesh.y_mids)
        data = data[data["y"] == y]
    if p1[2] == p2[2]:
        z = p1[2]
        z = find_nearest_mid(z, mesh.z_mids)
        data = data[data["z"] == z]

    if erg:
        data = data[data["Energy"] == erg]

    result = data["value"]

    return result


def pick_point(x, y, z, mesh, erg=None):
    """ find the mesh value for the voxel that  point x, y, z is in"""
    x = find_nearest_mid(x, mesh.x_mids)
    y = find_nearest_mid(y, mesh.y_mids)
    z = find_nearest_mid(z, mesh.z_mids)

    data = mesh.data
    data = data[data["x"] == x]
    data = data[data["y"] == y]
    data = data[data["z"] == z]

    if erg:
        data = data[data["Energy"] == erg]

    result = data["value"]

    return result


def max_mesh(mesh1):
    """ adds the absoute max value based on the relative error """
    maxvals = mesh1.data["value"] + (mesh1.data["value"] * mesh1.data["rel_err"])
    mesh1.data["max_vals"] = maxvals

    return mesh1


def add_mesh(mesh1, mesh2):
    """ checks if boundaries of two meshes are equal
        and adds their values and errors
    """
    if ((mesh1.x_bounds != mesh2.x_bounds) or
            (mesh1.y_bounds != mesh2.y_bounds) or
            (mesh1.z_bounds != mesh2.z_bounds)):
        raise ValueError('bounds not equal')

    else:
        new_val = mesh1.data['value'] + mesh2.data['value']
        new_err = np.sqrt((mesh1.data['rel_err'])**2 +
                          (mesh2.data['rel_err'])**2)

        new_mesh = meshtally()
        cols = ("Energy", "x", "y", "z", "value", "rel_err")
        new_mesh.data = pd.DataFrame(columns=cols)
        new_mesh.ctype = "6col"
        new_mesh.x_bounds = mesh1.x_bounds
        new_mesh.y_bounds = mesh1.y_bounds
        new_mesh.z_bounds = mesh1.z_bounds

        new_mesh.x_mids = mesh1.x_mids
        new_mesh.y_mids = mesh1.y_mids
        new_mesh.z_mids = mesh1.z_mids

        new_mesh.data['value'] = new_val
        new_mesh.data['rel_err'] = new_err
        new_mesh.data['Energy'] = mesh1.data['Energy']
        new_mesh.data['x'] = mesh1.data['x']
        new_mesh.data['y'] = mesh1.data['y']
        new_mesh.data['z'] = mesh1.data['z']

        return(new_mesh)


# TODO: need to deal with energy bins
def convert_to_3d_array(mesh):
    """ converts the mesh into 3d numpy array
        one array for the values and another for the rel errs
    """
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
    """ finds the mid points given a set of bounds """
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
    count = mesh.data["value"].value_counts()[0.0]
    return count


def find_mesh_tally_numbers(data):
    """ find the different meshes in the file, the tally number
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

    for i, v in enumerate(mesh_data):
        if in_data:
            # v = " ".join(v.split())
            # mesh.data.append(v.split(" "))
            logging.info("Guru meditation error")
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
            break

        elif "X         Y         Z     Result" in v:
            in_data = True
            mesh.ctype = "5col"
            break

        elif "mesh tally." in v:
            v = " ".join(v.split())
            mesh.ptype = v.split(" ")[0]

    mesh_data = [" ".join(j.split()) for j in mesh_data[i:]]
    mesh.data = [j.split() for j in mesh_data[1:]]
    mesh.data = convert_to_df(mesh)

    mesh.x_mids = calc_mid_points(mesh.x_bounds)
    mesh.y_mids = calc_mid_points(mesh.y_bounds)
    mesh.z_mids = calc_mid_points(mesh.z_bounds)
    logging.info("finished reading mesh number: %s ", str(tnum))

    return mesh


def read_mesh_tally_file(fpath):
    """ reads all meshes in a meshtal file, returns a list of mesh objects """
    logging.info('Reading MCNP meshtal file: %s', fpath)
    all_data = ut.get_lines(fpath)
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

    meshes = read_mesh_tally_file(args.input)
