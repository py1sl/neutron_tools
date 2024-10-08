"""
uesful utilities for common output options
"""
import csv
import neut_utilities as ut
import pandas


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
    html = "<table style='border-collapse: collapse; width: 100%;'> \n "

    for i, row in enumerate(data):
        if i == 0:
            html += "<tr style='background-color: green; color: white;'>\n"
        else:
            html += "<tr>\n"

        for item in row:
            html += f"    <td style='border: 1px solid black; padding: 8px;'>{item}</td>\n"
        html += "  </tr>\n"

    html += "</table>"
    return html


def output_html(tables, title="Results", fname="output.html"):
    """ output and html file from a list of html strings """
    if isinstance(tables, str):
        tables = [tables]

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            table {{border-collapse: collapse; width: 100%; margin-bottom: 20px;}}
            th, td {{border: 1px solid black; padding: 8px;}}
            tr:first-child {{background-color: green; color: white;}}
        </style>
    </head>
    <body>
    <h1>{title}</h1>
    """

    # Add each table to the body
    for table in tables:
        html += table + "\n"

    # Close the tags
    html += """
    </body>
    </html>
    """

    # write to file
    with open(fnam, "w") as f:
        f.write(html)


def dataframe_to_html_table(df):
    """Converts  DataFrame into an HTML table.

    """
    # CSS for table styling
    styles = """ <style>
    table {
        border-collapse: collapse;
        width: 100%;
    }
    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }
    thead tr {
        background-color: green;
        color: white;
    }
    </style>
    """
    
    # add top part
    html = f"\n {styles} \n <table> \n <thead> \n <tr>\n"
    
    # Add the column names
    for col in df.columns:
        html += f"<th>{col}</th>"
    
    html += "</tr></thead><tbody>"
    
    # loop over rows
    for _, row in df.iterrows():
        html += "<tr>"
        for item in row:
            html += f"<td>{item}</td>"
        html += "</tr>"
    
    # add the closing tags
    html += "</tbody></table>"
    
    return html
