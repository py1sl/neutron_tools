"""
uesful utilities for common output options
"""
import csv
import neut_utilities as ut


def output_points(x_vals, y_vals, z_vals, data_val=None, outpath="lost"):
    """ Outputs points in .3d format """

    # Initialize output list with the header
    out_list = ["x y z temp"]

    # Generate points with associated data or default value '1'
    if data_val is not None:
        out_list.extend(
            f"{x} {y} {z} {d}" for x, y, z, d in zip(x_vals, y_vals, z_vals, data_val)
        )
    else:
        out_list.extend(
            f"{x} {y} {z} 1" for x, y, z in zip(x_vals, y_vals, z_vals)
        )

    # Append the file extension
    outpath = f"{outpath}.3d"

    # Write the list of points to the file
    ut.write_lines(outpath, out_list)


def output_csv(data, outpath="output.csv"):
    """Outputs a list of lists as a CSV file.

    """
    with open(outpath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

        
def list_to_html_table(data):
    """Converts a list of lists into an HTML table.

    """
    html = "<table border='1'>\n"
    
    for row in data:
        html += "  <tr>\n"
        for item in row:
            html += f"    <td>{item}</td>\n"
        html += "  </tr>\n"
    
    html += "</table>"
    return html