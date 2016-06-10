# version 2 - 

'''
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

    TYPE: 

        each BLOK unit has a type parameter used to distinguish one BLOK from another.
        All Amplifier BLOKs have the same TYPE, but an Osc and and Amplifier have 
        different Types. 

    params:

        [Pnum, Pname, default, can_input]
          |
        1 - Pnum -1 means it's an input socket for audio
        2 - Pnum 0..n indicate the corresponding Pnum for the parameter
        3 - a Pnum with parens () means the param state is encoded using a range of P numbers. 
            An example of a param like this is the graphical element of the Waveshaper which 
            is incoded by 128 float values - I like to think of these as a Float Vector type.

        the 'can_input' entry states whether the parameter can be controlled via input from
        another blok unit. For example the waveform shape can be modified on the UI, it has 
        no input socket to allow for knobs or other units to decide the form.
'''


DOC = '''\
<?xml version="1.0" standalone="no" ?>
<storables>{globals}\n{patching}</storables>
'''

# it's one large non-dynamic blok (no socket inputs, only manual sliders)
GLOBAL = '''
    <GLOBAL ID="2" Param_Chorus_Enable="0.000000" Param_Chorus_Phasing="0.400000" Param_Chorus_Speed="0.400000" Param_Chorus_WetDry="0.400000" Param_Delay_Cross="0.000000" Param_Delay_Enable="0.000000" Param_Delay_Feedback="0.000000" Param_Delay_Length="0.400000" Param_Delay_Spacing="0.000000" Param_Delay_TempoSync="0.000000" Param_Delay_Type="0.000000" Param_Delay_WetDry="0.400000" Param_Polyphony="0.500000" Param_Reverb_Damping="0.300000" Param_Reverb_Decay="0.500000" Param_Reverb_Enable="0.000000" Param_Reverb_ModAmount="0.250000" Param_Reverb_ModSpeed="0.250000" Param_Reverb_Roomsize="0.500000" Param_Reverb_WetDry="0.300000" Param_Voice_Bendrange="0.500000" Param_Voice_Portamento="0.000000" Param_Voice_Transpose="0.500000" />'''


BLOKS = {
    'EnvBasic': {
        'TYPE': 2,
        'params': [
            [0, 'attack', 0.0, False],
            [1, 'decay', 0.2, False],
            [2, 'sustain', 0.3, False],
            [3, 'release', 0.5, False]
        ]
    },
    'EnvCustom': {
        'TYPE': 23,
        'params': [
            [0, 'speed', 0.6, True],
            [1, 'loop', 0.2, False],
            [2, 'sustain', 0.3, False],
            [3, 'pos', 0.5, False],
            [(4, 195), 'envelope', [0.5 for i in range(191)], False]
        ]
    },
    'EnvAdvanced': {
        'TYPE': 55,
        'params': [
            [0, 'attack', 0.1, True],
            [1, 'decay', 0.2, True],
            [2, 'sustain', 0.4, True],
            [3, 'release', 0.5, True],
            [4, 'amount', 1.0, True],
            [5, 'sustain_decay', 0.5, False],
            [(6, 17), 'envelope', [0.5 for i in range(12)], False]
        ]
    },
    'LFO': {
        'TYPE': 3,
        'params': [
            [0, 'frequency', 0.5, True],
            [1, 'amp', 0.5, True],
            [2, 'shape', 0.5, False] # (enum [Sine, Tri, Saw, Square])
        ]
    },
    'KnobInt': {
        'TYPE': 8,
        'params': [
            [0, 'range', 0.5, False]
        ]
    },
    'KnobExt': {
        'TYPE': [13, 14, 15, 16, 28, 29, 30, 31], #  only one of each may exist.
        'params': [
            [0, 'range', 0.5, False]
        ]
    },
    'Velocity': {'TYPE': 17, 'params': []},
    'Keytrack': {
        'TYPE': 33,
        'params': [
            [(0, 127), 'range', [i/128 for i in range(128)], False]  #  maybe hardcode instead?
        ]
    },
    'Random': {'TYPE': 35, 'params': []},
    'Aftertouch': {'TYPE': 48, 'params': []},
    'Modwheel': {'TYPE': 47, 'params': []},
    'Osc': {
        'TYPE': 4,
        'params': [
            [0, 'tuning', 0.5, True],
            [1, 'amp', 0.5, True],
            [2, 'shape', 0.5, False] # (enum [Sine, Tri, Saw, Square])
        ]
    },
    'SubOsc': {
        'TYPE': 18,
        'params': [
            [0, 'tuning', 0.5, True],
            [1, 'amp', 0.5, True],
            [2, 'shape', 0.5, False] # (enum [Sine, Tri, Saw, Square])
        ]
    },
    'FixedOsc': {
        'TYPE':  10,
        'params': [
            [0, 'tuning', 0.5, True],
            [1, 'amp', 0.5, True],
            [2, 'shape', 0.0, False] # (enum [Sine, Tri, Saw, Square])
        ]
    },
    'HyperOsc': {
        'TYPE': 32,
        'params': [
            [0, 'amp', 0.5, True],
            [1, 'tuning', 0.5, False],
            [2, 'diffuse', 0.5, False],
            [3, 'spread', 0.5, False],
            [4, 'shape', 0.5, False]  # (enum [Sine, Tri, Saw, Square])
        ]
    },
    'NoiseOsc': {
        'TYPE': 7, 
        'params': [
            [0, 'amp', 0.5, False]
        ]
    }, 
    'Impulse': {
        'TYPE': 39, 
        'params': [
            [0, 'amp', 1.0, True]
        ]
    },
    'SyncOsc': {
        'TYPE': 43,
        'params': [
            [0, 'amp', 0.5, True],
            [1, 'tuning', 0.5, True],
            [2, 'amount', 0.5, True],
            [3, 'sharpness', 0.5, False],
            [4, 'phase_reset', 0.0, False],
            [5, 'shape', 0.5, False]  # (enum [Sine, Tri, Saw, Square])
        ]
    },
    'PWMOsc': {
        'TYPE': 42,
        'params': [
            [0, 'amp', 0.5, True],
            [1, 'tuning', 0.5, True],
            [2, 'pulsewidth', 0.5, True],
            [3, 'phase_reset', 0.0, False],
            [4, 'shape', 0.5, False]  # (enum [Sine, Tri, Saw, Square])
        ]
    },
    'Sampler': {
        'TYPE': 58,
        'params': [
            [0, 'tuning', 0.5, True],
            [1, 'amp', 0.5, True]
        ]
    },
    'Filter': {
        'TYPE': 1,
        'params': [
            [-1, 'input', -1, True],
            [0, 'cutoff', 0.5, True],
            [1, 'resonance', 0.0, True],
            [2, 'kind', 0.0, False]  # (enum [LowPass, HighPass, BandPass, BandReject])
        ]
    },
    'Amplifier': {
        'TYPE': 6,
        'params': [
            [-1, 'input', -1, True],
            [0, 'factor', 0.5, True]
        ]
    },
    'Waveshaper': {
        'TYPE': 24,
        'params': [
            [-1, 'input', -1, True],
            [0, 'scale', 0.5, True],
            [1, 'offset', 0.5, True],
            [(2, 129), 'gradient', [i/128 for i in range(128)], False]  # hardcode? import? offer presets?
        ]
    },
    'Delay': {
        'TYPE': 19,
        'params': [
            [-1, 'input', -1, True],
            [0, 'time', 0.5, True], # (249ms)
            [1, 'feedback', 0.0, True]
        ]
    },
    'KeytrkDelay': {
        'TYPE': 20,
        'params': [
            [-1, 'input', -1, True],
            [0, 'time', True],
            [1, 'feedback', True]
        ]
    },
    'FilterDelay': {
        'TYPE': 21,
        'params': [
            [-1, 'input', -1, True],
            [0, 'time', 0.5, True],
            [1, 'feedback', 0.0, True],
            [2, 'cutoff', 0.5, False]
        ]
    },
    'Invert': {
        'TYPE': 27, 
        'params': [[-1, 'input', -1, True]]
    },
    'Rescale': {
        'TYPE': 26,
        'params': [
            [-1, 'input', -1, True],
            [0, 'factor', 1.0, True],
            [1, 'offset', 0.5, True]
        ]
    },
    'BitCrusher': {
        'TYPE': 34,
        'params': [
            [-1, 'input', -1, True],
            [0, 'bits', 0.0, True] #  20-0
        ]
    },
    'Clipper': {
        'TYPE': 40,
        'params': [
            [-1, 'input', -1, True],
            [0, 'upperLim', 1.0, True],
            [1, 'lowerLim', 0.0, True]
    },
    'VUTracker': {
        'TYPE': 41,
        'params': [
            [-1, 'input', -1, True],
            [0, 'decay', 0.5, False], # (445ms)
            [1, 'peak', 1.0, False] # (bool)   
        ]
    },
    'Xfade': {
        'TYPE': 46,
        'params': [
            [0, 'amp1', 0.5, True],
            [1, 'amp2', 0.5, True],
            [2, 'mix', 0.5, True],
            [3, 'audio', 1.0, False]
        ]
    },
    'EnvTrigger': {
        'TYPE': 51,
        'params': [
            [-1, 'input', -1, True],        
            [0, 'pregain', 1.0, False], #  (6.02dB)
            [1, 'attack', 0.5, False], #  (445ms)
            [2, 'release', 0.5, False], #  (445ms)
            [3, 'trigLevel', 0.5, False], #  (-12dB)
            [4, 'relLevel', 1.0, False],  
            [5, 'modScale', 1.0, False]
        ]
    },    
    'DynFollower': {
        'TYPE': 54,
        'P0': {'pregain': 1.0}, #  (6.02dB)
        'P1': {'attack': 0.5}, #  (445ms)
        'P2': {'release': 0.5}, #  (445ms)
        'P3': {'thresLevel': 0.5}, #  (-12dB)
        'P4': {'thresRatio': 0.2},
        'P5': {'modScale': 1.0}
    },    
    'Filter2': {
        'TYPE': 56,
        'P0': {'cutoff': 0.5}, #  (704Hz)
        'P1': {'resonance': 0.0},
        'P2': {'kind': 0.0}, # (enum [LowPass, HighPass, BandPass, BandReject])
        'P3': {'keytrack': 0.0}, #  (bool)
    },    
    'bandEQ': {
        'TYPE': 57,
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
    },
    'MonoOut': {
        'TYPE': 0,
        'P0': {'volume': 0.5}
    },
    'StereoOut': {
        'TYPE': 25,
        'P0': {'pan': 0.5},
        'P1': {'volume': 0.5}
    },
    'Arp': {
        'TYPE': 44,
        'P0': {'speed': 1.0},
        'P1': {'ticks': 1.0},
        'P2': {'octaves': 0.5}
    }
}
