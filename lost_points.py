"""
Reads the output file and gets a list of the co-ordinates of the lost particles
"""
import argparse
import output_utilities as o_ut


def output_lost_points(path, outpath="lost"):
    """ outputs a .3d file with the points particles got lost """
    x = []
    y = []
    z = []
    n_points = 0
    with open(path, 'r') as file:
        for line in file:
            if "x,y,z coordinates:" in line:
                x.append(float(line[28:40].strip()))
                y.append(float(line[43:55].strip()))
                z.append(float(line[58:70].strip()))
                n_points += 1
    if n_points > 0:
        o_ut.output_points(x, y, z, outpath=outpath)
    else:
        print("No lost points found")
    return n_points


if __name__ == "__main__":
    desc_txt1 = "extracts location of lost particles from MCNP output file"
    desc_txt2 = " and output to a .3d  file compatible with VisIt"
    parser = argparse.ArgumentParser(description=desc_txt1 + desc_txt2)
    parser.add_argument("input", help="path to the input file")
    parser.add_argument("-o", "--output", action="store", dest="output",
                        help="path to the output file")
    args = parser.parse_args()

    if args.output:
        output_lost_points(args.input, args.output)
    else:
        output_lost_points(args.input)
