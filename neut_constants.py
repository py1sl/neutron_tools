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
    return val/100.0


def sv_to_rem(val):
    """ convert Sv to Rem """
    return val * 100.0


def years_to_seconds(val):
    """ convert years to seconds"""
    return val * 365 * 24 * 60 * 60


def years_to_hrs(val):
    """ convert years to hours"""
    return val * 365 * 24


def years_to_days(val):
    """ convert years to days """
    return val * 365


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
