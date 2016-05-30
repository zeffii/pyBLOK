from pyBLOK import Connect, pBlk, pCompile

SubOsc1 = pBlk('Sub.Osc', (130, 140))
SubOsc2 = pBlk('Sub.Osc', (130, 180))
Env1 = pBlk('Env.advanced', (30, 180))
con1 = Connect(Env1, SubOsc2, index=1)
SubOsc1.params[2] = 0.333333
Env1.set_params(attack=0.88, decay=0.45, amount=0.2)


pCompile()

