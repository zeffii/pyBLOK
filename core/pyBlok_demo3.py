from blok_functions import Connect, pBlk, pCompile

out = pBlk('Mono.Out', (320, 110))

env1 = pBlk('Env.basic', (30, 110))
env1.set_params(attack=0.08, decay=0.45, release=0.6)

oscillators = []
for freq, y in zip([0, 0.5, 1], [120, 200, 280]):
    osc = pBlk('Osc', (170, y))
    osc.set_params(tuning=freq)
    env1 > (osc, 1)
    osc > (out, 0)
    oscillators.append(osc)

pCompile(path=r'C:\Users\zeffi\Desktop\fluxo4.blkx', silent=0)