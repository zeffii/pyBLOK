'''
rate_from_herz:

is a crude approximation of the curve, i didn't yet find the right curve(s) so here is a basic table lookup
with interpolations.
'''

series = [
    22, 23, 25, 27, 29, 31, 33, 35,
    38, 41, 44, 47, 50, 54, 58, 62,
    67, 71, 76, 82, 88, 94, 101, 108,
    116, 124, 134, 143, 153, 164, 174, 188,
    202, 216, 232, 249, 268, 287, 307, 329,
    352, 377, 404, 433, 465, 499, 536, 574,
    615, 658, 704, 754, 808, 867, 931, 999,
    1072, 1149, 1231, 1317, 1408, 1508, 1617, 1735,
    1863, 1999, 2144, 2298, 2462, 2634, 2816, 3016,
    3235, 3471, 3726, 3998, 4289, 4597, 4924, 5269,
    5632, 6033, 6470, 6943, 7452, 7997, 8578, 9195,
    9849, 10538, 11264, 12066, 12940, 13886, 14904,
    15994, 17157, 18391, 19698, 21077, 22528]

def between(hz, a, b):
    if (hz >= a) and (hz <= b):
        return hz
    else:
        return -1

def remap(old_min, old_max, old_val, new_min, new_max):
    return (((old_val - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

def rate_from_herz(Hz):
    ni = len(series)-1
    if Hz < 22:
        return 0.0
    if Hz > 22528:
        return 1.0
    tr = {between(Hz, series[i], series[i+1]): [series[i], series[i+1], Hz, i/ni, (i+1)/ni] for i in range(ni)}.get(Hz)
    return remap(*tr)
