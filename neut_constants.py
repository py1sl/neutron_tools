"""Set of constants for use by neutron tools """


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
    """convert rem to Sv """
    return val/100.0


def Sv_to_rem(val):
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
