from blok_functions import pBlk, pCompile

out = pBlk('MonoOut', (320, 110))

env1 = pBlk('EnvBasic', (30, 110))
env1.set_params(attack=0.085, decay=0.45, release=0.6)

oscillators = []
for freq, y in zip([0, 0.5, 1], [120, 200, 280]):
    osc = pBlk('Osc', (170, y))
    osc.set_params(tuning=freq)
    env1 > osc._amp
    osc > out._input
    oscillators.append(osc)


env1.attack(0.7)
env1.decay(0.22)

pCompile(path=r'C:\Users\zeffi\Desktop\demux1.blkx', silent=0)


