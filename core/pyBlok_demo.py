from blok_functions import Connect, pBlk, pCompile

SubOsc1 = pBlk('Sub.Osc', (130, 140))
SubOsc2 = pBlk('Sub.Osc', (130, 180))
Env1 = pBlk('Env.advanced', (30, 180))
con1 = Connect(Env1, SubOsc2, index=1)
SubOsc1.params[2] = 0.333333
Env1.set_params(attack=0.88, decay=0.45, amount=0.2)

# path must be a valid path, if it's omitted then pCompile prints
# the patch to stdout. If however the path is provided, the silent=1
# will suppress the print and only write the file
pCompile(path=r'C:\Users\zeffi\Desktop\fluxo.blkx', silent=1)
