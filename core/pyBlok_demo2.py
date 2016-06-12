from blok_functions import Connect, pBlk, pCompile

out = pBlk('MonoOut', (320, 110))

env1 = pBlk('EnvBasic', (30, 110))
env1.set_params(attack=0.08, decay=0.45, release=0.6)

oscillators = []
for freq, y in zip([0, 0.5, 1], [120, 200, 280]):
    osc = pBlk('Osc', (170, y))
    osc.set_params(tuning=freq)
    Connect(env1, osc, index=1)
    Connect(osc, out, index=0)
    oscillators.append(osc)

pCompile(path=r'C:\Users\zeffi\Desktop\3fluxo3.blkx', silent=0)
