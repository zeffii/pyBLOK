# PyBLOK

A preliminary attempt at a library for generating BLOK patches. I'm doing this to quickly mash together layouts that may be trickier to connect by hand

## Specs for the components of BLOK ( 2015 edition )

The main kinds of modules are Generate / Modulate / Control / Output. Analyze and Patch are less interesting for scripting access. All X,Y params excluded from the specs.

### CONTROL

#### Envelope (basic)

```
   - TYPE:  "2"
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
   - P0:    Attack      0.0 ... 1.0  // default 0.0
   - P1:    Decay       0.0 ... 1.0  // default 0.2
   - P2:    Sustain     0.0 ... 1.0  // default 0.3
   - P3:    Sustain     0.0 ... 1.0  // default 0.5
```

#### Envelope (custom)

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
#### Envelope (Advanced)

```
   - TYPE:  "55"
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
   - P0:    Attack      0.0 ... 1.0  // default 0.1
   - P1:    Decay       0.0 ... 1.0  // default 0.2
   - P2:    Sustain     0.0 ... 1.0  // default 0.4
   - P3:    Release     0.0 ... 1.0  // default 0.5
   - P4:    Amount      0.0 ... 1.0  // default 1.0
   - P5:    Sust.Decay  0.0 ... 1.0  // default 0.5
   - P6-17  p6 bezier control 1
            p7 bezier control 2
            p8 bezier control 3
            p9 bezier control 4
            < to do -- this is not imperative yet >
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

#### Knob

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

#### Velocity
```
   - TYPE:  "17"
```
#### Keytrack
```
   - TYPE:  "33"
   - P0-127:range      0.0 ... 1.0  // default gradient up
```
#### Random
```
   - TYPE:  "35"
```
#### Aftertouch
```
   - TYPE:  "48"
```
#### ModWheel
```
   - TYPE:  "47"
```
#### Env Trigger
```
   - TYPE:  "51"
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
   - P0:    Pregain     0.0 ... 1.0  // default 1.0
   - P1:    Attack      0.0 ... 1.0  // default 0.5
   - P2:    Release     0.0 ... 1.0  // default 0.5
   - P3:    Trig.level  0.0 ... 1.0  // default 0.5
   - P4:    Rel.level   0.0 ... 1.0  // default 1.0
   - P5:    Mod.Scale   0.0 ... 1.0  // default 1.0
```
#### Dyn Follower
```
   - TYPE:  "54"
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
   - P0:    Pregain     0.0 ... 1.0  // default 1.0
   - P1:    Attack      0.0 ... 1.0  // default 0.5
   - P2:    Release     0.0 ... 1.0  // default 0.5
   - P3:    Thres.level 0.0 ... 1.0  // default 0.5
   - P4:    Thres.Ratio 0.0 ... 1.0  // default 0.2
   - P5:    Mod.Scale   0.0 ... 1.0  // default 1.0
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

