""" """
import matplotlib
# import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import logging as ntlogger

from neutron_tools.utilities import neut_utilities as ut
from neutron_tools.utilities import neut_constants
matplotlib.use('agg')


def normalise(data, norm_val):
    """convert raw data to normalised data"""
    data = np.asarray(data, dtype=float)
    norm_val = float(norm_val)
    norm = data * norm_val
    return norm


def calc_err_abs(results, errors):
    """ calculates absolute errors"""
    # check same length
    if len(results) != len(errors):
        raise ValueError(f"The length of results ({len(results)}) and errors ({len(errors)}) must be the same")

    # calculate absolute error for all results
    abs_err = [res*float(err) for res, err in zip(results, errors)]

    return abs_err


def calc_bin_width(bins):
    """ calculate energy bin widths """
    # calculate bin widths and add 1st bin
    if len(bins) < 2:
        raise ValueError("At least two bin edges are required to calculate bin widths.")

    bw = np.diff(bins, prepend=0)
    return bw


def calc_mid_points(bounds):
    """ calculate the mid points of a list"""
    mids = []
    bounds = np.array(bounds).astype(float)
    i = 0
    while i < len(bounds) - 1:
        val = (bounds[i] + bounds[i + 1]) / 2.0
        mids.append(val)
        i = i + 1
    return mids


def _get_df_energy_result(df, eng_hint=None):
    """Extract aligned energy/result arrays from an energy-binned tally DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Tally result DataFrame. Usually contains columns ``energy`` and
        ``result``; ``energy`` may include a final ``"total"`` row.
    eng_hint : sequence, optional
        Optional energy-bin edges from tally metadata, used when no
        ``energy`` column is present.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        ``(energy, result)`` arrays with any non-numeric energy rows removed.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame for tally result data")
    if "result" not in df.columns:
        raise ValueError("Result DataFrame must contain a 'result' column")

    result_vals = pd.to_numeric(df["result"], errors="coerce")

    if "energy" in df.columns:
        energy_vals = pd.to_numeric(df["energy"], errors="coerce")
        valid = energy_vals.notna() & result_vals.notna()
        energy = energy_vals[valid].to_numpy(dtype=float)
        result = result_vals[valid].to_numpy(dtype=float)
    else:
        if eng_hint is None:
            raise ValueError("Energy-binned result requires an 'energy' column or eng_hint")
        energy = np.asarray(eng_hint, dtype=float)
        result = result_vals.dropna().to_numpy(dtype=float)
        if len(energy) != len(result):
            raise ValueError(
                f"Energy/result length mismatch ({len(energy)} != {len(result)})"
            )

    return energy, result


def _first_result_df(result_obj):
    """Return the first DataFrame from common tally ``result`` containers."""
    if isinstance(result_obj, pd.DataFrame):
        return result_obj
    if isinstance(result_obj, dict):
        return next(iter(result_obj.values()))
    raise TypeError("Unsupported tally result container; expected DataFrame or dict")


def _extract_series_rel_err(df, tally, series_key, expected_len):
    """Get per-series relative error array for a plotted line when available."""
    rel_err = None

    if isinstance(df, pd.DataFrame) and "rel_err" in df.columns:
        rel_vals = pd.to_numeric(df["rel_err"], errors="coerce")
        if "energy" in df.columns:
            energy_vals = pd.to_numeric(df["energy"], errors="coerce")
            valid = energy_vals.notna() & rel_vals.notna()
            rel_vals = rel_vals[valid]
        else:
            rel_vals = rel_vals.dropna()
        rel_arr = rel_vals.to_numpy(dtype=float)
        if len(rel_arr) == expected_len:
            rel_err = rel_arr

    if rel_err is not None:
        return rel_err

    if not hasattr(tally, "err") or tally.err is None:
        return None

    if isinstance(tally.err, dict):
        if series_key not in tally.err:
            return None
        err_obj = tally.err[series_key]
        if isinstance(err_obj, pd.DataFrame):
            if "rel_err" in err_obj.columns:
                err_vals = pd.to_numeric(err_obj["rel_err"], errors="coerce").dropna()
                err_arr = err_vals.to_numpy(dtype=float)
            else:
                return None
        else:
            err_arr = np.asarray(err_obj, dtype=float)
    else:
        err_arr = np.asarray(tally.err, dtype=float)

    if len(err_arr) != expected_len:
        return None
    return err_arr


def _plot_energy_series(ax, tally, series_key, df, label=None):
    """Plot a single energy-binned series and return plotting context."""
    energy, result = _get_df_energy_result(df, eng_hint=tally.eng)
    bw = calc_bin_width(energy)
    y_vals = result / bw
    splot = ax.step(energy, y_vals, label=label)

    rel_err = _extract_series_rel_err(df, tally, series_key, len(y_vals))
    return {
        "energy": energy,
        "y_vals": y_vals,
        "line": splot[0],
        "rel_err": rel_err,
    }


def _plot_type1_spectra(ax, tally, legend_override, sp):
    """Handle tally type 1 plotting. Keeps existing type-1 behavior."""
    ax.ylabel("current n/MeV/" + sp)
    series_contexts = []
    ang_bins = tally.ang_bins if tally.ang_bins is not None else []

    if len(tally.surfaces) > 1:
        if len(ang_bins) > 1:
            print("not implemented yet - plotting spectra, angle and multiple surfaces")
            raise NotImplementedError
        for surf, df in tally.result.items():
            series_contexts.append(_plot_energy_series(ax, tally, surf, df, label=surf))
    else:
        if len(ang_bins) > 1:
            for ang_df in tally.result:
                series_contexts.append(_plot_energy_series(ax, tally, None, ang_df))
            legend_override = ang_bins
        else:
            for surf, df in tally.result.items():
                series_contexts.append(_plot_energy_series(ax, tally, surf, df, label=surf))
            ax.legend()

    return series_contexts, legend_override


def _plot_type2_spectra(ax, tally, legend_override):
    """Handle tally type 2 plotting."""
    series_contexts = []
    for surf, df in tally.result.items():
        series_contexts.append(_plot_energy_series(ax, tally, surf, df, label=surf))
    ax.legend()
    return series_contexts, legend_override


def _plot_type4_spectra(ax, tally, legend_override):
    """Handle tally type 4 plotting."""
    series_contexts = []
    for cell, df in tally.result.items():
        series_contexts.append(_plot_energy_series(ax, tally, cell, df, label=cell))
    ax.legend()
    return series_contexts, legend_override


def _plot_type5_spectra(ax, tally, legend_override):
    """Handle tally type 5 plotting."""
    df = tally.result[0]
    series_contexts = [_plot_energy_series(ax, tally, 0, df)]
    return series_contexts, legend_override


def _plot_default_spectra(ax, tally, legend_override):
    """Fallback plotting for other tally types."""
    df = _first_result_df(tally.result)
    series_contexts = [_plot_energy_series(ax, tally, None, df)]
    return series_contexts, legend_override


def _apply_errorbars_for_contexts(ax, series_contexts):
    """Apply per-series error bars using each series' own relative errors."""
    for ctx in series_contexts:
        rel_err = ctx["rel_err"]
        if rel_err is None:
            continue
        y_vals = ctx["y_vals"]
        energy = ctx["energy"]
        if len(energy) < 2:
            continue
        abs_err = calc_err_abs(y_vals, rel_err)
        mids = calc_mid_points(energy)
        ecol = ctx["line"].get_color()
        ax.errorbar(mids, y_vals[1:], yerr=abs_err[:-1], fmt="none",
                    ecolor=ecol, markeredgewidth=1, capsize=2)


def _apply_global_x_limits(ax, all_series_contexts, xlow=None):
    """Set global x-limits based on the widest plotted series."""
    if not all_series_contexts:
        return

    widest_ctx = None
    widest_span = -np.inf
    for ctx in all_series_contexts:
        energy = ctx["energy"]
        if len(energy) == 0:
            continue
        span = float(np.max(energy) - np.min(energy))
        if span > widest_span:
            widest_span = span
            widest_ctx = ctx

    if widest_ctx is None:
        return

    widest_energy = widest_ctx["energy"]
    widest_y = widest_ctx["y_vals"]
    xmax = float(np.max(widest_energy))

    if xlow is None:
        non_zero_loc = ut.find_first_non_zero(widest_y)
        if non_zero_loc is not None:
            xmin = float(widest_energy[non_zero_loc])
            ax.xlim(xmin=xmin, xmax=xmax)
        else:
            ax.xlim(xmax=xmax)
    else:
        ax.xlim(xmin=xlow, xmax=xmax)


def _unpack_et_df(et_input):
    """Extract (energy_arr, time_arr, value_matrix) from an E×T DataFrame.

    Parameters
    ----------
    et_input : pd.DataFrame
        The ``value_df`` returned by :func:`process_e_t_userbin`, with energy
        as row index and time bin boundaries as column names.

    Returns
    -------
    tuple[np.ndarray, np.ndarray, np.ndarray]
        ``(energy_arr, time_arr, value_matrix)``
    """
    if isinstance(et_input, pd.DataFrame):
        energy_arr = et_input.index.to_numpy(dtype=float)
        time_arr = et_input.columns.to_numpy(dtype=float)
        value_matrix = et_input.values
    else:
        raise TypeError(
            "et_input must be a pd.DataFrame with energy as index and time as columns"
        )
    return energy_arr, time_arr, value_matrix


def find_peak_time(target_energy, ET_results):
    """Find the time at which maximum flux occurs for a given energy.

    Parameters
    ----------
    target_energy : float
        The target energy value to find the peak for.
    ET_results : pd.DataFrame
        E×T DataFrame returned by :func:`process_e_t_userbin`, with energy
        as row index and time bin boundaries as column names.

    Returns
    -------
    float
        Time value at which peak flux occurs.
    """
    energy_arr, time_arr, value_matrix = _unpack_et_df(ET_results)

    # Find index of closest energy
    erg_index = np.argmin(np.abs(energy_arr - target_energy))

    # Get flux slice for this energy
    flux_slice = value_matrix[erg_index, :]

    # Find peak within valid time array bounds
    valid_flux = flux_slice[:len(time_arr)]
    peak_index = np.argmax(valid_flux)
    peak_time = time_arr[peak_index]

    return peak_time


def plot_raw_spectra(data, fname, title, sp="proton"):
    """ plots spectra from MCNP tally data object per bin no normalisation """
    plt.clf()
    plt.title("Neutron energy spectra full model " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/" + sp + "/bin")
    plt.xscale('log')
    plt.yscale('log')
    if not isinstance(data, list):
        data = [data]

    for d in data:
        if not hasattr(d, 'eng'):
            raise ValueError("Invalid MCNP tally does not have energy bins.")

        for obj_id, df in d.result.items():
            energy, result = _get_df_energy_result(df, eng_hint=d.eng)
            splot = plt.step(energy, result, label=obj_id)
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def plot_spectra(data, fname, title, sp="proton", err=False,
                 xlow=None, legend=None):
    """ plots spectra from MCNP tally data object, dividing by bin width """
    if not isinstance(data, list):
        data = [data]

    plt.clf()
    plt.title(" " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("flux n/cm2/MeV/" + sp)
    plt.xscale('log')
    plt.yscale('log')

    handlers = {
        '1': lambda ax, d, leg: _plot_type1_spectra(ax, d, leg, sp),
        '2': _plot_type2_spectra,
        '4': _plot_type4_spectra,
        '5': _plot_type5_spectra,
    }

    all_series_contexts = []

    for d in data:
        handler = handlers.get(d.tally_type, _plot_default_spectra)
        series_contexts, legend = handler(plt, d, legend)
        all_series_contexts.extend(series_contexts)

        if err is True:
            _apply_errorbars_for_contexts(plt, series_contexts)

    _apply_global_x_limits(plt, all_series_contexts, xlow=xlow)

    if legend is not None:
        plt.legend(legend)

    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def plot_spectra_ratio(data1, data2, fname, title):
    """  plots the ratio of two energy spectra """
    plt.clf()
    plt.title("Comparison of " + title)
    plt.xlabel("Energy (MeV)")
    plt.ylabel("ratio")
    plt.xscale('log')

    df1 = _first_result_df(data1.result)
    df2 = _first_result_df(data2.result)

    e1, r1 = _get_df_energy_result(df1, eng_hint=data1.eng)
    e2, r2 = _get_df_energy_result(df2, eng_hint=data2.eng)

    s1 = pd.Series(r1, index=e1)
    s2 = pd.Series(r2, index=e2)
    common_energies = s1.index.intersection(s2.index)
    if len(common_energies) == 0:
        raise ValueError("No overlapping energy bins found for ratio plot")

    ratio = (s1.loc[common_energies] / s2.loc[common_energies]).to_numpy(dtype=float)
    plt.plot(common_energies.to_numpy(dtype=float), ratio)
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def plot_run_comp(data, err, fname, title, xlab="Run #",
                  ylab="Dose Rate microSv/h"):
    """ plot single value tally results with error """
    plt.clf()

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    x = np.arange(1, len(data) + 1)
    plt.xlim(xmin=0, xmax=len(x) + 1)
    plt.errorbar(x, data, yerr=err, fmt='o')
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def plot_ET_heatmap(ET_results, fname, normalise_factor=1):
    """ plot an energy time heat map from a tally with energy and time bins.

    Parameters
    ----------
    ET_results : pd.DataFrame
        E×T DataFrame returned by :func:`process_e_t_userbin`, with energy
        as row index and time bin boundaries as column names.
    fname : str
        Filename to save the plot.
    normalise_factor : float, optional
        Normalisation factor applied to the flux values.
    """
    energy_arr, time_arr, ET_matrix = _unpack_et_df(ET_results)

    # set up to do log ignoring 0 bins
    ET_safe = np.where(ET_matrix > 0, ET_matrix, np.nan)
    ET_safe = normalise(ET_safe, normalise_factor)
    log_values = np.log10(ET_safe)

    # convert shakes to microS
    time_arr = neut_constants.shake_to_ms(time_arr)

    # Plot heatmap
    plt.figure(figsize=(12, 6))
    pcm = plt.pcolormesh(time_arr, energy_arr, log_values[:-1, :-2], shading='auto', cmap='viridis')
    plt.colorbar(pcm, label='log10(flux)')

    # Add shaded region for 2-10Å energy range
    # Convert wavelengths to energy: E(MeV) = (81.81 / λ²(Å²)) / 1e9
    energy_10A = (81.81 / (10.0 ** 2)) / 1e9  # Lower energy bound (longer wavelength)
    energy_2A = (81.81 / (2.0 ** 2)) / 1e9    # Upper energy bound (shorter wavelength)
    plt.axhspan(energy_10A, energy_2A, alpha=0.15, color='red', label='2-10Å')

    plt.xscale('linear')
    plt.yscale('log')
    plt.xlabel(r'Time ($\mu$S)')
    plt.ylabel('Energy (MeV)')
    plt.title('Energy Over Time')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def time_slice(target_time, ET_results, fname, normalise_factor=1):
    """ Extract and plot an energy spectrum at a given time from a
        tally with energy and time bins.

    Parameters
    ----------
    target_time : float
        Target time (shakes) for which to extract the energy spectrum.
    ET_results : pd.DataFrame
        E×T DataFrame returned by :func:`process_e_t_userbin`, with energy
        as row index and time bin boundaries as column names.
    fname : str
        Filename to save the plot.
    normalise_factor : float, optional
        Normalisation factor applied to the flux values.
    """
    energy_arr, time_arr, ET_matrix = _unpack_et_df(ET_results)

    # Find index of closest time
    time_index = np.argmin(np.abs(time_arr - target_time))
    flux_slice = ET_matrix[:, time_index]
    flux_slice = normalise(flux_slice, normalise_factor)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(energy_arr, flux_slice, marker='o')
    plt.xscale('log')
    plt.xlabel('Energy (MeV)')
    plt.ylabel('Flux ')
    plt.title(f'Flux vs Energy at time = {time_arr[time_index]:.2e}')
    plt.tight_layout()
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


def energy_slice(target_energy, ET_results, fname, min_time=None, max_time=None, wl=True, window=50, normalise_factor=1, plot_total=True, xscale='log'):
    """ Extract and plot time distributions for a given energy or multiple energies from a
        tally with energy and time bins.

        Parameters
        ----------
        target_energy : float, list, or array-like
            The target energy value(s) to extract. Can be a single energy (float) or
            multiple energies (list or array).
        ET_results : pd.DataFrame
            E×T DataFrame returned by :func:`process_e_t_userbin`, with energy
            as row index and time bin boundaries as column names.
        fname : str
            Filename to save the plot
        min_time : float, optional
            Minimum time for x-axis. If None, calculated from peak.
        max_time : float, optional
            Maximum time for x-axis. If None, calculated from peak.
        wl : bool, optional
            If True, display wavelength in title instead of energy. Default is True.
        window : int, optional
            Window size around peak for auto-scaling time axis. Default is 50.
        normalise_factor : float, optional
            Normalization factor for flux values. Default is 1.
        plot_total : bool, optional
            If True, plot total flux (summed over all energies) as a line. Default is True.
        xscale : str, optional
            X-axis scale type: 'log' for logarithmic, 'linear' for linear. Default is 'log'.
    """
    energy_arr, time_arr, ET_matrix = _unpack_et_df(ET_results)

    # Convert target_energy to array if it's a scalar
    target_energies = np.atleast_1d(target_energy)

    # Find indices of closest energies and convert time array once
    erg_indices = []
    for te in target_energies:
        erg_index = np.argmin(np.abs(energy_arr - te))
        erg_indices.append(erg_index)
        print(f"Energy: {te}, index: {erg_index}")

    # Convert shakes to microS
    time_arr_converted = neut_constants.shake_to_ms(time_arr)

    # Calculate total flux (sum across all energies)
    total_flux = np.sum(ET_matrix, axis=0)
    total_flux = normalise(total_flux, normalise_factor)

    # Plot
    plt.figure(figsize=(8, 5))

    # Collect all peaks to determine overall time limits if not specified
    all_peaks = []
    all_peak_times = []
    all_peak_values = []

    for erg_index, te in zip(erg_indices, target_energies):
        flux_slice = ET_matrix[erg_index, :]
        flux_slice = normalise(flux_slice, normalise_factor)

        # focus on the peak - ensure peak is within time array bounds
        # Limit search to the range that matches time_arr_converted length
        valid_flux = flux_slice[:len(time_arr_converted)]
        peak_index = np.argmax(valid_flux)
        peak_value = valid_flux[peak_index]

        all_peaks.append(peak_index)
        all_peak_values.append(peak_value)

        # Store the actual peak time value
        peak_time = time_arr_converted[peak_index]
        all_peak_times.append(peak_time)

        # Create label with either wavelength or energy
        if wl:
            wave_length = np.sqrt(81.81 / (energy_arr[erg_index])/1e9)
            label = f'λ = {round(wave_length, 2)} Å'
        else:
            label = f'E = {energy_arr[erg_index]:.2e} MeV'

        plt.plot(time_arr_converted, flux_slice, marker='o', label=label)

    # Plot total flux if requested
    if plot_total:
        plt.plot(time_arr_converted, total_flux, marker='s', linewidth=2,
                 label='Total flux', color='black', alpha=0.7)

    plt.xscale(xscale)
    plt.xlabel(r'Time ($\mu$S)')
    plt.ylabel('Flux')

    # Determine time limits (centered on peak with window around it)
    if min_time is None or max_time is None:
        if len(all_peaks) > 0:
            # Use median of peak indices to handle multiple energies
            median_peak_idx = int(np.median(all_peaks))
            median_peak_idx = np.clip(median_peak_idx, 0, len(time_arr_converted) - 1)

            # Define window in terms of indices, not time
            min_idx = max(0, median_peak_idx - window)
            max_idx = min(len(time_arr_converted) - 1, median_peak_idx + window)

            if min_time is None:
                min_time = time_arr_converted[min_idx]
            if max_time is None:
                max_time = time_arr_converted[max_idx]

    plt.xlim(min_time, max_time)

    # Set y-axis limits based on peak values
    if plot_total:
        # Use total flux at the median peak location
        median_peak_idx = int(np.median(all_peaks))
        median_peak_idx = np.clip(median_peak_idx, 0, len(total_flux) - 1)
        y_max = total_flux[median_peak_idx] * 1.05
    else:
        # Use maximum of individual energy peaks
        y_max = max(all_peak_values) * 1.05

    plt.ylim(0, y_max)

    if len(erg_indices) > 1:
        plt.title('Flux vs time at multiple energies')
        plt.legend()
    else:
        erg_index = erg_indices[0]
        if wl:
            wave_length = np.sqrt(81.81 / (energy_arr[erg_index])/1e9)
            plt.title(f'Flux vs time at wavelength = {round(wave_length, 2)} Å')
        else:
            plt.title(f'Flux vs time at energy = {energy_arr[erg_index]:.2e} MeV')
        if plot_total:
            plt.legend()

    plt.tight_layout()
    plt.savefig(fname)
    ntlogger.info("produced figure: %s", fname)


