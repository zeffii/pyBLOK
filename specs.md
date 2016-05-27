# PyBLOK

A preliminary attempt at a library for generating BLOK patches. I'm doing this to quickly mash together layouts that may be trickier to connect by hand

## Specs for the components of BLOK ( 2015 edition )

The main kinds of modules are:  

```
 -[x] Generate  
 -[x] Control  
 -[ ] Modify  
 -[ ] Output  
```

 Analyze and Patch are less interesting for scripting access. All X,Y params excluded from the specs. And Pos / ID

```
   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
```

### CONTROL

#### Envelope (basic)

```
   - TYPE:  "2"
   - P0:    Attack      0.0 ... 1.0  // default 0.0
   - P1:    Decay       0.0 ... 1.0  // default 0.2
   - P2:    Sustain     0.0 ... 1.0  // default 0.3
   - P3:    Sustain     0.0 ... 1.0  // default 0.5
```

#### Envelope (custom)

```
   - TYPE:  "23"
   - P0:    Speed       0.0 ... 1.0  // default 0.6
   - P1:    Loop        0.2 ... 1.0  // default 0.2 (bool)
   - P2:    Sustain     0.3 ... 1.0  // default 0.3 (bool)
   - P3:    Loop Pos    0.0 ... 1.0  // default 0.5
   - P4-195:Envelope    0.0 ... 1.0  // default 0.5
```
#### Envelope (Advanced)

```
   - TYPE:  "55"
   - P0:    Attack      0.0 ... 1.0  // default 0.1
   - P1:    Decay       0.0 ... 1.0  // default 0.2
   - P2:    Sustain     0.0 ... 1.0  // default 0.4
   - P3:    Release     0.0 ... 1.0  // default 0.5
   - P4:    Amount      0.0 ... 1.0  // default 1.0
   - P5:    Sust.Decay  0.0 ... 1.0  // default 0.5
   - P6-17  p6  bezier ctrl 1 x
            p7  bezier ctrl 1 y
            p8  bezier ctrl 2 x
            p9  bezier ctrl 2 y
            p10 bezier ctrl 3 x
            p11 bezier ctrl 3 y
            p12 bezier ctrl 4 x
            p13 bezier ctrl 4 y
            p14 bezier ctrl 5 x
            p15 bezier ctrl 5 y
            p16 bezier ctrl 6 x
            p17 bezier ctrl 6 y
```

#### LFO

```
   - TYPE:  "3"
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
   - P0:    Pregain     0.0 ... 1.0  // default 1.0
   - P1:    Attack      0.0 ... 1.0  // default 0.5
   - P2:    Release     0.0 ... 1.0  // default 0.5
   - P3:    Thres.level 0.0 ... 1.0  // default 0.5
   - P4:    Thres.Ratio 0.0 ... 1.0  // default 0.2
   - P5:    Mod.Scale   0.0 ... 1.0  // default 1.0
```


### GENERATE 

#### Oscillator
```
   - TYPE:  "4"
   - P0:    tuning      0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
```

#### Sub Oscillator
```
   - TYPE:  "18"
   - P0:    tuning      0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
```

#### Fixed Oscillator
```
   - TYPE:  "10"
   - P0:    tuning      0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.0 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
```

#### Hyper Oscillator
```
   - TYPE:  "32"
   - P0:    amp         0.0 ... 1.0  // default 0.5
   - P1:    tuning      0.0 ... 1.0  // default 0.5
   - P2:    diffuse     0.0 ... 1.0  // default 0.5
   - P3:    spread      0.0 ... 1.0  // default 0.5
   - P4:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
```

#### Noise Oscillator
```
   - TYPE:  "7"
   - P0:    amp         0.0 ... 1.0  // default 0.5
```

#### Impulse
```
   - TYPE:  "39"
   - P0:    amp         0.0 ... 1.0  // default 1.0
```

#### Sync Oscillator
```
   - TYPE:  "43"
   - P0:    amp         0.0 ... 1.0  // default 0.5
   - P1:    tuning      0.0 ... 1.0  // default 0.5
   - P2:    amount      0.0 ... 1.0  // default 0.5
   - P3:    sharpness   0.0 ... 1.0  // default 0.5
   - P4:    phase.reset 0.0 ... 1.0  // default 0.0
   - P5:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
```
#### PWM Oscillator
```
   - TYPE:  "42"
   - P0:    amp         0.0 ... 1.0  // default 0.5
   - P1:    tuning      0.0 ... 1.0  // default 0.5
   - P2:    pulsewidth  0.0 ... 1.0  // default 0.5
   - P3:    phase.reset 0.0 ... 1.0  // default 0.0
   - P4:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
```
#### Sampler (basic)
```
   - TYPE:  "58"
   - P0:    tuning      0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
```

### Modifiers

#### Filter
```
   - TYPE:  "1"
   - P0:    Cutoff      0.0 ... 1.0  // default 0.5
   - P1:    Resonance   0.0 ... 1.0  // default 0.0
   - P2:    kind                     // (enum)
            - Low Pass   "0.000000"
            - HighPass   "0.333333"
            - BandPass   "0.555555"
            - BandReject "1.0"

```
#### Amplifier
```
   - TYPE:  "6"
   - P0:    Factor      0.0 ... 1.0  // default 0.5

```
#### Waveshaper
```
   - TYPE:  "24"
   - P0:    Scale       0.0 ... 1.0  // default 0.5
   - P1:    Offset      0.0 ... 1.0  // default 0.5
   - P2-129 Gradient    [0.0 .. 1.0]

```
#### Delay
```
   - TYPE:  "19"
   - ...

```
#### Keytracked Delay
```
   - TYPE:  "20"
   - ...

```
#### Filter Delay
```
   - TYPE:  "21"
   - ...
   - ...

```
#### Invert
```
   - TYPE:  "27"

```
#### Rescale
```
   - TYPE:  "26"

```
#### Bit Crusher
```
   - TYPE:  "34"

```
#### Clipper
```
   - TYPE:  "40"
   0
   1

```
#### VU Tracker
```
   - TYPE:  "41"
   0  float
   1  bool

```
#### Crossfade
```
   - TYPE:  "46"
   P0  amp1
   P1  amp2
   P2  mix
   P3  signal type (AR,CR)

```

#### Env Trigger
```
   - TYPE:  "51"
   0  pregain      1.0
   1  attack       0.5
   2  release      0.5
   3  Trig Level   0.5
   4  Rel Level    1.0
   5  Mod Scale    0.5

```

#### Dyn Follower
```
   - TYPE:  "54"
   0  pregain      1.0
   1  attack       0.5
   2  release      0.5
   3  Thres.Level  0.5
   4  Thres.Ratio  0.2
   5  Mod Scale    1.0

```

#### Filter 2
```
   - TYPE:  "56"
   - 0 Cutoff
   - 1 Resonance
   - 2 kind     (enum) LP HP BP BR
   - 3 keytrack (bool) 0.0

```
#### 3 band EQ
```
   - TYPE:  "57"
   - 0 kind    (enum) Off, peak, low, high
   - 1 Cutoff
   - 2 width
   - 3 Amp
   - 4 kind    (enum) Off, peak, low, high
   - 5 Cutoff
   - 6 width
   - 7 Amp
   - 8 kind    (enum) Off, peak, low, high
   - 9 Cutoff
   - 10 width
   - 11 Amp
```