from blok_functions import pBlk, pCompile
from blok_utils import rate_from_herz

# http://computermusicresource.com/Simple.bell.tutorial.html
overtones = [0.56, .92, 1.19, 1.71, 2.0, 2.74, 3, 3.76, 4.07]

out = pBlk('Mono.Out', (520, 110))

env1 = pBlk('Env.basic', (20, 110))
env1.set_params(attack=0.11, decay=0.65, release=0.8)

noise = pBlk('Noise.Osc', (180, 110))
env1 > noise.index(0)

fundamental = 200
ypositions = [(120 + 80*i) for i, _ in enumerate(overtones)]

for freq, y in zip(overtones, ypositions):
    fz = rate_from_herz(fundamental*freq)
    _filter = pBlk('Filter', (380, y))
    _filter.set_params(cutoff=fz, resonance=0.98)
    noise > _filter.index(0)
    _filter > out.index(0)


pCompile(path=r'C:\Users\zeffi\Desktop\fluxo_bell.blkx', silent=0)
