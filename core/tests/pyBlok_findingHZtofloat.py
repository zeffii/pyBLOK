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

for idx, i in enumerate([
    0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5,
    0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]):

    f = pBlk('Filter', get_location(idx))
    f.set_params(cutoff=i)


pCompile(path=r'C:\Users\zeffi\Desktop\fluxo7.blkx', silent=0)

'''
22: 0.0
31: 0.05
44: 0.10
62: 0.15
88: 0.20
124: 0.25
176: 0.30
249: 0.35
352: 0.40
499: 0.45
704: 0.50
999: 0.55
1408: 0.60
1999: 0.65
2816: 0.70
3998: 0.75
5632: 0.80
7997: 0.85
11264: 0.90
15994: 0.95
22528: 1.00

22, 31, 44, 62, 88, 124, 176, 249, 352, 499, 704, 999, 1408, 1999, 2816, 3998, 5632, 7997, 11264, 15994, 22528

22: 0.0
          9
31: 0.05
          13
44: 0.10
          18
62: 0.15
          26
88: 0.20
          36
124: 0.25
          52 
176: 0.30
          73
249: 0.35
          103
352: 0.40
          147
499: 0.45
          205
704: 0.50
          295
999: 0.55
          409
1408: 0.60
          591
1999: 0.65
          817
2816: 0.70
          1182
3998: 0.75
          1634
5632: 0.80 
          2365
7997: 0.85
          3267
11264: 0.90
          4730
15994: 0.95
          6534
22528: 1.00

'''