"""
Reads the output file and gets a list of the co-ordinates of the lost particles
"""
import argparse
import neut_utilities as ut
import output_utilities as o_ut


def output_lost_points(path, outpath="lost"):
    """ outputs a .3d file with the points particles got lost """
    lines = ut.get_lines(path)
    x = []
    y = []
    z = []
    
    for line in lines:
        if "x,y,z coordinates:" in line:
            x.append(float(line[28:40]))
            y.append(float(line[43:55]))
            z.append(float(line[58:70]))
            
    o_ut.output_points(x, y, z, outpath=outpath)


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
