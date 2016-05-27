# PyBLOK

A preliminary attempt at a library for generating BLOK patches. I'm doing this to quickly mash together layouts that may be trickier to connect by hand

## Specs for the components of BLOK ( 2015 edition )

The main kinds of modules are Generate / Modulate / Control / Output. Analyze and Patch are less interesting for scripting access. All X,Y params excluded from the specs.

### CONTROL

#### ENVELOPE (basic)

```
   - TYPE:  "2"
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
   - P0:    Attack      0.0 ... 1.0  // default 0.0
   - P1:    Decay       0.0 ... 1.0  // default 0.2
   - P2:    Sustain     0.0 ... 1.0  // default 0.3
   - P3:    Sustain     0.0 ... 1.0  // default 0.5
```

#### ENVELOPE (advanced)

```
   - TYPE:  "23"
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
   - P0:    Speed       0.0 ... 1.0  // default 0.6
   - P1:    Loop        0.2 ... 1.0  // default 0.2 (bool)
   - P2:    Sustain     0.3 ... 1.0  // default 0.3 (bool)
   - P3:    Loop Pos    0.0 ... 1.0  // default 0.5
   - P4-195:Envelope    0.0 ... 1.0  // default 0.5
```

#### LFO

```
   - TYPE:  "3"
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
   - P0:    frequency   0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
```

#### KNOB

Internal

```
   - TYPE:  "8"
   - P0:    range       0.0 ... 1.0  // default 0.5
```
External

```
   - TYPE:  "13..16" -> "28..31"
   - P0:    range       0.0 ... 1.0  // default 0.5
```

### GENERATE 

#### OSC
```
   - TYPE:  "4"
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
   - P0:    semitone    0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
```

