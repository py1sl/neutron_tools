"""Set of constants and conversions for use by neutron tools """


def get_e():
    """charge on electron in coulombs"""
    return 1.60217662e-19


def get_p_mass():
    """mass of proton in g"""
    return 1.672623e-24


def get_n_mass():
    """mass of neutron in g"""
    return 1.674929e-24


def get_e_mass():
    """ mass of electron in g"""
    return 9.10938e-28


def rem_to_Sv(val):
    """convert Rem to Sv """
    return val / 100.0


def sv_to_rem(val):
    """ convert Sv to Rem """
    return val * 100.0


def years_to_seconds(val):
    """ convert years to seconds"""
    return val * 365.25 * 24 * 60 * 60


def years_to_hrs(val):
    """ convert years to hours"""
    return val * 365.25 * 24


def years_to_days(val):
    """ convert years to days """
    return val * 365.25


def bq_to_curie(val):
    """converts bq to curies """
    return val * 2.703e11


def curie_to_bq(val):
    """ convert val to bq """
    return val * 3.7e-12


def eV_to_joule(val):
    """ convert electron volts to joules """
    return val * 1.602e-19


def eV_to_wavelength_photon(val):
    """ converts eV to wavelength in m """
    return 1.24e-6 / val


def wavelength_to_meV_neutron(val):
    """convert neutron wavelength in A to energy in meV """
    return 81.81 / (val * val)


def joule_to_ev(val):
    """ converts energy in joules to electron volts """
    return val / (1.602e-19)


def second_to_hour(val):
    """ converts time in seconds to hours """
    return val / 3600


def second_to_day(val):
    """ converts time in seconds to days """
    return val / 86400


def second_to_year(val):
    """ converts time in seconds to years """
    return val / 3.1536e07


def hour_to_second(val):
    """ converts time in hours to seconds """
    return val * 3600


def day_to_second(val):
    """ converts time in days to seconds """
    return val * 86400


def shake_to_second(val):
    """ converts time in shakes to seconds """
    return val * 1e-8


def second_to_shake(val):
    """ converts time in seconds to shakes """
    return val * 1e8


def shake_to_ms(val):
    """ converts time in shake to millisecond """
    return val / 100


def barn_to_cm2(val):
    """ converts barns to cm2 """
    return val/ 1e24


def cm2_to_barn(val):
    """ converts cm2 to barns """
    return val * 1e24


def Z_dict():
    zdict = {
        "H": 1,
        "He": 2,
        "Li": 3,
        "Be": 4,
        "B": 5,
        "C": 6,
        "N": 7,
        "O": 8,
        "F": 9,
        "Ne": 10,
        "Na": 11,
        "Mg": 12,
        "Al": 13,
        "Si": 14,
        "P": 15,
        "S": 16,
        "Cl": 17,
        "Ar": 18,
        "K": 19,
        "Ca": 20,
        "Sc": 21,
        "Ti": 22,
        "V": 23,
        "Cr": 24,
        "Mn": 25,
        "Fe": 26,
        "Co": 27,
        "Ni": 28,
        "Cu": 29,
        "Zn": 30,
        "Ga": 31,
        "Ge": 32,
        "As": 33,
        "Se": 34,
        "Br": 35,
        "Kr": 36,
        "Rb": 37,
        "Sr": 38,
        "Y": 39,
        "Zr": 40,
        "Nb": 41,
        "Mo": 42,
        "Tc": 43,
        "Ru": 44,
        "Rh": 45,
        "Pd": 46,
        "Ag": 47,
        "Cd": 48,
        "In": 49,
        "Sn": 50,
        "Sb": 51,
        "Te": 52,
        "I": 53,
        "Xe": 54,
        "Cs": 55,
        "Ba": 56,
        "La": 57,
        "Ce": 58,
        "Pr": 59,
        "Nd": 60,
        "Pm": 61,
        "Sm": 62,
        "Eu": 63,
        "Gd": 64,
        "Tb": 65,
        "Dy": 66,
        "Ho": 67,
        "Er": 68,
        "Tm": 69,
        "Yb": 70,
        "Lu": 71,
        "Hf": 72,
        "Ta": 73,
        "W": 74,
        "Re": 75,
        "Os": 76,
        "Ir": 77,
        "Pt": 78,
        "Au": 79,
        "Hg": 80,
        "Tl": 81,
        "Pb": 82,
        "Bi": 83,
        "Po": 84,
        "At": 85,
        "Rn": 86,
        "Fr": 87,
        "Ra": 88,
        "Ac": 89,
        "Th": 90,
        "Pa": 91,
        "U": 92,
        "Np": 93,
        "Pu": 94,
        "Am": 95,
        "Cm": 96,
        "Bk": 97,
        "Cf": 98,
        "Es": 99,
        "Fm": 100,
        "Md": 101,
        "No": 102,
        "Lr": 103,
        "Rf": 104,
        "Db": 105,
        "Sg": 106,
        "Bh": 107,
        "Hs": 108,
        "Mt": 109,
        "Ds": 110,
        "Rg": 111,
        "Cn": 112,
        "Nh": 113,
        "Fl": 114,
        "Mc": 115,
        "Lv": 116,
        "Ts": 117,
        "Og": 118,
    }
    return zdict
