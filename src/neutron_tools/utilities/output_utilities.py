"""
useful utilities for common output options
"""
from os import PathLike
from typing import Any, List, Mapping, Optional, Protocol, Sequence, Union

import pandas as pd

from neutron_tools.utilities import neut_utilities as ut
import logging as ntlogger

FilePath = Union[str, PathLike[str]]


class TallyProtocol(Protocol):
    number: Any
    particle: str
    eng: Optional[Sequence[Any]]
    times: Optional[Sequence[Any]]
    stat_tests: Optional[Sequence[Any]]
    tally_type: str
    cells: Sequence[str]
    vols: Sequence[str]
    result: Mapping[int, pd.DataFrame]


class MCObjectProtocol(Protocol):
    file_name: str
    date: Any
    start_time: Any
    num_rendevous: Any
    warnings: Sequence[Any]
    tally_data: Sequence[TallyProtocol]


def wrap_tokens(
    prefix: Any,
    tokens: Sequence[Any],
    max_len: int = 80,
    cont_prefix: str = '     '
) -> List[str]:
    """ wraps a list of tokens into lines with a given prefix and max length """
    # normalize cont_prefix to ensure a separating space is present
    if cont_prefix and not cont_prefix.endswith(' '):
        cont_prefix = cont_prefix + ' '

    lines = []
    current = str(prefix) + ' '

    # handle None or empty tokens gracefully
    if not tokens:
        return [current.rstrip()]

    for tok in tokens:
        tok = str(tok).strip()
        if tok == '':
            # skip empty tokens
            continue

        # raise an error if a single token is longer than max_len
        if len(tok) > max_len:
            raise ValueError(f"Token length {len(tok)} exceeds max_len {max_len}: {tok}")

        # if adding this token would exceed max_len, start a continuation line
        if len(current) + len(tok) + 1 > max_len:
            lines.append(current.rstrip())
            current = cont_prefix + tok
        else:
            if current.endswith(' '):
                current += tok
            else:
                current += ' ' + tok

    # append the last line if non-empty
    if current.strip():
        lines.append(current.rstrip())

    return lines


def output_points(
    x_vals: Sequence[Any],
    y_vals: Sequence[Any],
    z_vals: Sequence[Any],
    data_val: Optional[Sequence[Any]] = None,
    outpath: str = "lost"
) -> None:
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


def html_output(mc_object: MCObjectProtocol, fname: FilePath) -> None:
    """produces html output of file """
    # TODO refactor this to work with a template system

    hlines = []
    hlines.append("<!DOCTYPE html><HTML><HEAD>")
    hlines.append("<meta charset=\"utf-8\">")
    hlines.append("<meta name=\"viewport\" content=\"width=device-width\">")
    hlines.append("</HEAD>")

    hlines.append(f"<title>{mc_object.file_name}</title>")

    hlines.append("<body>")
    hlines.append(f"<H1>{mc_object.file_name}</H1>")
    hlines.append(f"Date run: {mc_object.date}")
    hlines.append(f"Time run: {mc_object.start_time}")
    hlines.append(f"Rendevous: {mc_object.num_rendevous}")
    hlines.append(f"Number of warnings: {len(mc_object.warnings)}")

    # add tally specific data
    for tdat in mc_object.tally_data:
        hlines.append(f"<p><H2> Tally Number: {tdat.number}</H2>")
        hlines.append(f"Particle: {tdat.particle}")

        if tdat.eng:
            hlines.append(f"Number Energy Bins: {len(tdat.eng)}")
        if tdat.times:
            hlines.append(f"Number Time Bins: {len(tdat.times)}")

        if tdat.stat_tests:
            hlines.append("Statistical test results")
            stat_rows = [
                ("Mean behaviour", tdat.stat_tests[0]),
                ("Rel err value", tdat.stat_tests[1]),
                ("rel err behavior", tdat.stat_tests[2]),
                ("rel err rate", tdat.stat_tests[3]),
                ("Variance value", tdat.stat_tests[4]),
                ("Variance behavior", tdat.stat_tests[5]),
                ("Variance rate", tdat.stat_tests[6]),
                ("FOM value constant", tdat.stat_tests[7]),
                ("FOM behavior random", tdat.stat_tests[8]),
                ("PDF slope", tdat.stat_tests[9]),
            ]
            stat_lines = ["<table><tr><th>Test</th><th>Result</th></tr>"]
            for name, val in stat_rows:
                stat_lines.append(f"<tr><td>{name}</td><td>{val}</td></tr>")
            stat_lines.append("</table>")
            hlines.append("\n".join(stat_lines))
        else:
            hlines.append("Warning Statistical test data not found")

        # add tally type specific data
        if tdat.tally_type == "4":
            hlines.append(f"Number Cells: {len(tdat.cells)}")
            cell_string = "".join(tdat.cells)
            hlines.append(f"Cells: {cell_string}")
            hlines.append(f"Volumes: {''.join(tdat.vols)}")
            # add result plots
            if tdat.eng and len(tdat.cells) == 1:
                pname = f"tally_{tdat.number}_{tdat.cells[0]}.png"
                # plot_spectra(tdat, pname, title, sp="neutron")
                hlines.append(f"<img src={pname} alt=\"simulated spectrum\">")
            else:
                print("no energy bins or more than one cell")

        hlines.append("</p>")

    hlines.append("</body>")
    hlines.append("</HTML>")

    # output the file
    ut.write_html(fname, hlines)
    ntlogger.info("produced html file: %s", fname)


def html_f4_tab_out(data: Union[TallyProtocol, Sequence[TallyProtocol]], fname: FilePath) -> None:
    """ produces f4 tally data as html table output """
    if not isinstance(data, list):
        data = [data]
    header = "<html><table><tr><th>Tally Number</th><th>CellNumber</th><th>Result</th><th>Relative error</th></tr>"
    rows = []
    for tall in data:
        for cell in tall.cells:
            cell_id = int(cell)
            df = tall.result[cell_id]
            result_val = df["result"].iloc[0]
            rel_err_val = df["rel_err"].iloc[0]
            row_parts = [
                f"<tr><td>{tall.number}</td>",
                f"<td>{cell}</td>",
                f"<td>{result_val}</td>",
                f"<td>{rel_err_val}</td></tr>",
            ]
            rows.append("".join(row_parts))

    strTable = header + "\n" + "\n".join(rows) + "\n</table></html>"

    with open(fname, 'w') as hs:
        hs.write(strTable)
    ntlogger.info("produced html file: %s", fname)


def csv_out(data: Union[TallyProtocol, Sequence[TallyProtocol]], fname: FilePath) -> None:
    """ produces  tally data as csv output   """
    if not isinstance(data, list):
        data = [data]

    lines = []
    for tall in data:
        for cell in tall.cells:
            cell_id = int(cell)
            df = tall.result[cell_id]
            result_val = df["result"].iloc[0]
            rel_err_val = df["rel_err"].iloc[0]
            lines.append(f"{tall.number}, {cell}, {result_val}, {rel_err_val}")

    ut.write_lines(fname, lines)
    ntlogger.info("produced csv file: %s", fname)
