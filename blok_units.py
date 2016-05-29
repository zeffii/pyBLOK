
# Shapes
Sine = 0.000000
Tri = 0.333333
Saw = 0.500000
Square = 1.000000

# filter types
LowPass = 0.000000
HighPass = 0.333333
BandPass = 0.500000 
BandReject = 1.000000

# filter shapes
Off = 0.000000
peak = 0.333333
low = 0.500000
high = 1.000000


blok_dict = {
    'Env.basic': {
        'TYPE': 2,
        'P0': {'attack': 0.0},
        'P1': {'decay': 0.2},
        'P2': {'sustain': 0.3},
        'P3': {'release': 0.5}
    },
    'Env.custom': {
        'TYPE': 23,
        'P0': {'speed': 0.6},
        'P1': {'loop': 0.2}, # (bool, off)
        'P2': {'sustain': 0.3}, # (bool, off)
        'P3': {'loop.pos': 0.5},
        'P4-P195': {'envelope': [0.5 for i in range(191)]}
    },
    'Env.advanced': {
        'TYPE': 55,
        'P0': {'attack': 0.1},
        'P1': {'decay': 0.2},
        'P2': {'sustain': 0.4},
        'P3': {'release': 0.5},
        'P4': {'amount': 1.0},
        'P5': {'sust.decay': 0.5},
        'P6-P17': {'envelope': [0.5 for i in range(12)]}  # maybe hard-code these instead?
    },
    'LFO': {
        'TYPE': 3,
        'P0': {'frequency': 0.5},
        'P1': {'amp': 0.5},
        'P2': {'shape': 0.5} # (enum [Sine, Tri, Saw, Square])
    },
    'Knob.int': {
        'TYPE': 8,
        'P0': {'range': 0.5}
    },
    'Knob.ext': {
        'TYPE': [13,14,15,16,28,29,30,31],  # only one of each may exist.
        'P0': {'range': 0.5}
    },
    'Velocity': {
        'TYPE': 17
    },
    'Keytrack': {
        'TYPE': 33,
        'P0-P127': {'range': [i/128 for i in range(128)]}  #  maybe hardcode instead?
    },
    'Random': {'TYPE': 35},
    'Aftertouch': {'TYPE': 48},
    'Mod.wheel': {'TYPE': 47},
    'Osc': {
        'TYPE': 4,
        'P0': {'tuning': 0.5},
        'P1': {'amp': 0.5},
        'P2': {'shape':  0.5} # (enum [Sine, Tri, Saw, Square])
    },
    'SubOsc': {
        'TYPE': 18,
        'P0': {'tuning': 0.5},
        'P1': {'amp': 0.5},
        'P2': {'shape': 0.5}  # (enum [Sine, Tri, Saw, Square])
   },
    'Fixed.Osc': {
        'TYPE':  10,
        'P0': {'tuning': 0.5},
        'P1': {'amp': 0.5},
        'P2': {'shape': 0.0}  # (enum [Sine, Tri, Saw, Square])
    },
    'Hyper.Osc': {
        'TYPE': 32,
        'P0': {'amp': 0.5},
        'P1': {'tuning': 0.5},
        'P2': {'diffuse': 0.5},
        'P3': {'spread': 0.5},
        'P4': {'shape': 0.5}  # (enum [Sine, Tri, Saw, Square])
    },
    'Noise.Osc': {
        'TYPE': 7, 
        'P0': {'amp': 0.5}
    }, 
    'Impulse': {
        'TYPE': 39, 
        'P0': {'amp': 1.0}
    },
    'Sync.Osc': {
        'TYPE': 43,
        'P0': {'amp': 0.5},
        'P1': {'tuning': 0.5},
        'P2': {'amount': 0.5},
        'P3': {'sharpness': 0.5},
        'P4': {'phase.reset' 0.0},
        'P5': {'shape': 0.5}  # (enum [Sine, Tri, Saw, Square])
    },
    'PWM.Osc': {
        'TYPE': 42,
        'P0': {'amp': 0.5},
        'P1': {'tuning': 0.5},
        'P2': {'pulsewidth': 0.5},
        'P3': {'phase.reset': 0.0},
        'P4': {'shape': 0.5}  # (enum [Sine, Tri, Saw, Square])
    },
    'Sampler': {
        'TYPE': 58,
        'P0': {'tuning': 0.5},
        'P1': {'amp': 0.5}
    },
    'Filter': {
        'TYPE': 1,
        'P0': {'cutoff': 0.5},
        'P1': {'resonance': 0.0},
        'P2': {'kind': 0.0}  # (enum [LowPass, HighPass, BandPass, BandReject])
    },
    'Amplifier': {
        'TYPE': 6,
        'P0': {'factor': 0.5}
    },
    'Waveshaper': {
        'TYPE': 24,
        'P0': {'scale': 0.5},
        'P1': {'offset': 0.5},
        'P2-P129': {'gradient': [i/127 for i in range(127)]}  # hardcode? import? offer presets?
    },
    'Delay': {
        'TYPE': 19,
        'P0': {'time': 0.5}, # (249ms)
        'P1': {'feedback': 0.0}
    },
    'Keytrk.Delay': {
        'TYPE': 20,
        'P0': {'time': 0.5},
        'P1': {'feedback': 0.0}
    },
    'Filter.Delay': {
        'TYPE': 21,
        'P0': {'time': 0.5},
        'P1': {'feedback': 0.0},
        'P2': {'cutoff': 0.5}
    },
    'Invert': {
        'TYPE': 27
    },
    'Rescale': {
        'TYPE': 26,
        'P0': {'factor': 1.0},
        'P1': {'offset': 0.5}
    },
    'Bit.Crusher': {
        'TYPE': 34,
        'P0': {'bits': 0.0} #  20-0
    },
    'Clipper': {
        'TYPE': 40,
        'P0': {'upper.Lim': 1.0},
        'P1': {'lower.Lim': 0.0}
    },
    'VU.Tracker': {
        'TYPE': 41,
        'P0': {'decay': 0.5}, # (445ms)
        'P1': {'peak': 1.0} # (bool)   
    },
    'Xfade': {
        'TYPE': 46,
        'P0': {'amp1': 0.5},
        'P1': {'amp2': 0.5},
        'P2': {'mix': 0.5},
        'P3': {'audio': 1.0}
    },
    'Env.Trigger': {
        'TYPE': 51,
        'P0': {'pregain': 1.0}, #  (6.02dB)
        'P1': {'attack': 0.5}, #  (445ms)
        'P2': {'release': 0.5}, #  (445ms)
        'P3': {'trig.Level': 0.5}, #  (-12dB)
        'P4': {'rel.Level': 1.0},  
        'P5': {'mod.Scale': 1.0}  
    },    
    'Dyn.Follower': {
        'TYPE': 54,
        'P0': {'pregain': 1.0}, #  (6.02dB)
        'P1': {'attack': 0.5}, #  (445ms)
        'P2': {'release': 0.5}, #  (445ms)
        'P3': {'thres.level': 0.5}, #  (-12dB)
        'P4': {'thres.ratio': 0.2},
        'P5': {'mod.scale': 1.0}
    },    
    'Filter2': {
        'TYPE': 56,
        'P0': {'cutoff': 0.5}, #  (704Hz)
        'P1': {'resonance': 0.0},
        'P2': {'kind': 0.0}, # (enum [LowPass, HighPass, BandPass, BandReject])
        'P3': {'keytrack': 0.0}, #  (bool)
    },    
    'bandEQ': {
        'TYPE': 57
        'P0': {'kind': 0.0}, # (enum [Off, peak, low, high]),
        'P1': {'freq': 0.5}, #  (704Hz)
        'P2': {'width': 0.5}, # 
        'P3': {'amp': 0.0}, # 
        'P4': {'kind': 0.0}, # (enum [Off, peak, low, high]),
        'P5': {'freq': 0.5}, #  (704Hz)
        'P6': {'width': 0.5}, # 
        'P7': {'amp': 0.0}, # 
        'P8': {'kind': 0.0}, # (enum [Off, peak, low, high]),
        'P9': {'freq': 0.5}, #  (704Hz)
        'P10': {'width': 0.5}, # 
        'P11': {'amp': 0.0} #    
    }
    'Mono.Out': {
        'TYPE': 0,
        'P0': {'volume': 0.5}
    },
    'Stereo.Out': {
        'TYPE': 25,
        'P0': {'pan': 0.5},
        'P1': {'volume': 0.5}
    },
    'Arp': {
        'TYPE': 44,
        'P0': {'speed': 1.0},
        'P1': {'ticks': 1.0},
        'P2': {'octaves': 0.5}
         #  this might be off by one, the progress indicator may be p3..
         # p3,6,9...49  down   0.0 ... 1.0  // default 0.0 (bool)
         # p4,7,10..50  note   0.0 ... 1.0  // default 0.5
         # p5,8,11..51  up     0.0 ... 1.0  // default 0.0 (bool)
    }
}
