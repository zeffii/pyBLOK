from blok_functions import Connect, pBlk, pCompile

out = pBlk('Mono.Out', (180, 80))

env1 = pBlk('Env.basic', (30, 110))
env1.set_params(attack=0.08, decay=0.45, release=0.6)

oscillators = []
for freq, y in zip([0, 0.5, 1], [120, 150, 180]):
    osc = pBlk('Osc', (130, y))
    osc.set_params(tuning=freq)
    Connect(env1, osc, index=1)
    Connect(osc, out, index=0)
    oscillators.append(osc)

# path must be a valid path, if it's omitted then pCompile prints
# the patch to stdout. If however the path is provided, the silent=1
# will suppress the print and only write the file
pCompile(path=r'C:\Users\zeffi\Desktop\fluxo3.blkx', silent=0)
