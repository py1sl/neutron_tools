"""
uesful utilities for common output options
"""
import neut_utilities as ut
import logging as ntlogger


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


def html_output(mc_object, fname):
    """produces html output of file """
    # TODO refactor this to be more generic

    hlines = []
    hlines.append("<!DOCTYPE html><HTML><HEAD>")
    hlines.append("<meta charset=\"utf-8\">")
    hlines.append("<meta name=\"viewport\" content=\"width=device-width\">")
    hlines.append("</HEAD>")

    hlines.append("<title>" + mc_object.file_name + "</title>")

    hlines.append("<body>")
    hlines.append("<H1>" + mc_object.file_name + "</H1>")
    hlines.append("Date run: " + mc_object.date)
    hlines.append("Time run: " + mc_object.start_time)
    hlines.append("Rendevous: " + str(mc_object.num_rendevous))
    hlines.append("Number of warnings: " + str(len(mc_object.warnings)))

    # add tally specific data
    for tdat in mc_object.tally_data:
        hlines.append("<p><H2> Tally Number: " + str(tdat.number) + "</H2>")
        hlines.append("Particle: " + tdat.particle)

        if tdat.eng:
            hlines.append("Number Energy Bins: " + str(len(tdat.eng)))
        if tdat.times:
            hlines.append("Number Time Bins: " + str(len(tdat.times)))

        if tdat.stat_tests:
            hlines.append("Statistical test results")

            stat_string = "<table><tr><th>Test</th><th>Result</th></tr>"
            stat_string += "<tr><td>" + "Mean behaviour" + \
                "</td> <td>" + tdat.stat_tests[0] + "</td></tr>"
            stat_string += "<tr><td>" + "Rel err value" + \
                "</td> <td>" + tdat.stat_tests[1] + "</td></tr>"
            stat_string += "<tr><td>" + "rel err behavior" + \
                "</td> <td>" + tdat.stat_tests[2] + "</td></tr>"
            stat_string += "<tr><td>" + "rel err rate" + \
                "</td> <td>" + tdat.stat_tests[3] + "</td></tr>"
            stat_string += "<tr><td>" + "Variance value" + \
                "</td> <td>" + tdat.stat_tests[4] + "</td></tr>"
            stat_string += "<tr><td>" + "Variance behavior" + \
                "</td> <td>" + tdat.stat_tests[5] + "</td></tr>"
            stat_string += "<tr><td>" + "Variance rate" + \
                "</td> <td>" + tdat.stat_tests[6] + "</td></tr>"
            stat_string += "<tr><td>" + "FOM value constant" + \
                "</td> <td>" + tdat.stat_tests[7] + "</td></tr>"
            stat_string += "<tr><td>" + "FOM behavior random" + \
                "</td> <td>" + tdat.stat_tests[8] + "</td></tr>"
            stat_string += "<tr><td>" + "PDF slope" + \
                "</td> <td>" + tdat.stat_tests[9] + "</td></tr>"
            stat_string += "</table>"
            hlines.append(stat_string)

        else:
            hlines.append("Warning Statistical test data not found")

        # add tally type specific data
        if tdat.tally_type == "4":
            hlines.append("Number Cells: " + str(len(tdat.cells)))
            cell_string = "".join(tdat.cells)
            hlines.append("Cells: " + cell_string)
            hlines.append("Volumes: " + "".join(tdat.vols))
            # add result plots
            if tdat.eng and len(tdat.cells) == 1:
                pname = "tally_" + str(tdat.number) + \
                    "_" + str(tdat.cells[0]) + ".png"
                title = tdat.particle + \
                    " Spectra for cell " + str(tdat.cells[0])
                # plot_spectra(tdat, pname, title, sp="neutron")

                hlines.append(
                    "<img src=" +
                    pname +
                    " alt=\"simulated spectrum\">")
            else:
                print("no energy bins or more than one cell")

        hlines.append("</p>")

    hlines.append("</body>")
    hlines.append("</HTML>")

    # output the file
    ut.write_html(fname, hlines)
    ntlogger.info("produced html file: %s", fname)


def html_f4_tab_out(data, fname):
    """ produces f4 tally data as html table output """
    # this might be redundant in future it is not very flexible
    if not isinstance(data, list):
        data = [data]

    strTable = "<html><table><tr><th>Tally Number</th><th>CellNumber"
    strTable = strTable + "</th><th>Result</th><th>Relative error</th></tr>"
    for tall in data:
        for i, cell in enumerate(tall.cells):
            strTable = strTable + "<tr><td>" + str(tall.number) + "</td>"
            strTable = strTable + "<td>" + str(tall.cells[i]) + "</td>"
            strTable = strTable + "<td>" + str(tall.result[i]) + "</td>"
            strTable = strTable + "<td>" + str(tall.err[i]) + "</td>"
            strTable = strTable + "</tr>"

    strTable = strTable + "</table></html>"

    hs = open(fname, 'w')
    hs.write(strTable)
    ntlogger.info("produced html file: %s", fname)


def csv_out(data, fname):
    """ produces  tally data as csv output   """
    # refactor to be more generic
    if not isinstance(data, list):
        data = [data]

    lines = []
    for tall in data:
        for i, cell in enumerate(tall.cells):
            ltext = str(tall.number) + ", "
            ltext = ltext + str(tall.cells[i]) + ", "
            ltext = ltext + str(tall.result[i]) + ", "
            ltext = ltext + str(tall.err[i])
            lines.append(ltext)

    ut.write_lines(fname, lines)
    ntlogger.info("produced csv file: %s", fname)
