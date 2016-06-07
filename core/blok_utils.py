'''
rate_from_herz:

is a crude approximation of the curve, i didn't yet find the right curve(s) so here is a basic table lookup
with interpolations.
'''

series = [22, 31, 44, 62, 88, 124, 176, 249, 352, 499, 704, 999, 1408, 1999, 2816, 3998, 5632, 7997, 11264, 15994, 22528]

def between(hz, a, b):
    if (hz >= a) and (hz <= b):
        return hz
    else:
        return -1

def remap(old_min, old_max, old_val, new_min, new_max):
    return (((old_val - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

def rate_from_herz(Hz):
    if Hz < 22:
        return 0.0
    if Hz > 22528:
        return 1.0
    tr = {between(Hz, series[i], series[i+1]): [series[i], series[i+1], Hz, i/20, (i+1)/20] for i in range(20)}.get(Hz)
    return remap(*tr)
