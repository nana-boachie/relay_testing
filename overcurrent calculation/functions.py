# Over current
def long_time_inverse(psm, tms):  # A
    operating_time = tms * (120 / (psm - 1))
    return operating_time


def standard_inverse(psm, tms):  # B
    operating_time = tms * (0.14 / ((psm ** 0.02) - 1))
    return operating_time


def very_inverse(psm, tms):  # C
    operating_time = tms * (13.5 / (psm - 1))
    return operating_time


def extremely_inverse(psm, tms):  # D
    operating_time = tms * (80 / ((psm ** 2) - 1))
    return operating_time
