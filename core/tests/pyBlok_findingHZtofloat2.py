import math
from blok_functions import pBlk, pCompile

items_wide = 8
xoffset = 100
yoffset = 100
padding_x = 50
padding_y = 50

def get_location(i):
    x = padding_x + xoffset * (i % items_wide)
    y = padding_y + yoffset * math.floor(i / items_wide)
    return x, y

num_items = 100
for idx, i in enumerate([i/num_items for i in range(num_items+1)]):

    f = pBlk('Filter', get_location(idx))
    f.set_params(cutoff=i)


pCompile(path=r'C:\Users\zeffi\Desktop\rrfluxo7.blkx', silent=0)

