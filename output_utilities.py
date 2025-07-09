"""
uesful utilities for common output options
"""
import neut_utilities as ut


def output_points(x_vals, y_vals, z_vals, data_val=None, outpath="lost"):
    """ outputs points in .3d format """

    # check cordinate list lengths match
    if len(x_vals) != len(y_vals) or len(x_vals) != len(z_vals):
        raise ValueError("Input lists must have the same length.")

    # check if there is a data value its length matches the co-ordinates
    if data_val is not None and len(data_val) != len(x_vals):
        raise ValueError("data_val must have the same length as x_vals, y_vals, and z_vals.")

    out_list = []
    out_list.append("x y z temp")

    i = 0
    if data_val is not None:
        while i < len(x_vals):
            out_list.append(str(x_vals[i]) +
                            " " +
                            str(y_vals[i]) +
                            " " +
                            str(z_vals[i]) + " " +
                            str(data_val[i]))
            i = i + 1
    else:
        while i < len(x_vals):
            out_list.append(str(x_vals[i]) +
                            " " +
                            str(y_vals[i]) +
                            " " +
                            str(z_vals[i]) +
                            " 1")
            i = i + 1

    outpath = outpath + ".3d"
    ut.write_lines(outpath, out_list)
