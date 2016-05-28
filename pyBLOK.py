'''
 Analyze and Patch are less interesting for scripting access. All X,Y params excluded from the specs. And Pos / ID

   - POS:   ( 0...n , DAG position, or Z position? )     
   - ID:    given at creation time
'''

### CONTROL

#### Envelope (basic)

'''
   - TYPE:  "2"
   - P0:    Attack      0.0 ... 1.0  // default 0.0
   - P1:    Decay       0.0 ... 1.0  // default 0.2
   - P2:    Sustain     0.0 ... 1.0  // default 0.3
   - P3:    Sustain     0.0 ... 1.0  // default 0.5
'''

#### Envelope (custom)

'''
   - TYPE:  "23"
   - P0:    Speed       0.0 ... 1.0  // default 0.6
   - P1:    Loop        0.2 ... 1.0  // default 0.2 (bool)
   - P2:    Sustain     0.3 ... 1.0  // default 0.3 (bool)
   - P3:    Loop Pos    0.0 ... 1.0  // default 0.5
   - P4-195:Envelope    0.0 ... 1.0  // default 0.5
'''
#### Envelope (Advanced)

'''
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
'''

#### LFO

'''
   - TYPE:  "3"
   - P0:    frequency   0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
'''

#### Knob

# Internal

'''
   - TYPE:  "8"
   - P0:    range       0.0 ... 1.0  // default 0.5
'''
# External

'''
   - TYPE:  "13..16" -> "28..31"
   - P0:    range       0.0 ... 1.0  // default 0.5
'''

#### Velocity
'''
   - TYPE:  "17"
'''
#### Keytrack
'''
   - TYPE:  "33"
   - P0-127:range      0.0 ... 1.0  // default gradient up
'''
#### Random
'''
   - TYPE:  "35"
'''
#### Aftertouch
'''
   - TYPE:  "48"
'''
#### ModWheel
'''
   - TYPE:  "47"
'''
#### Env Trigger
'''
   - TYPE:  "51"
   - P0:    Pregain     0.0 ... 1.0  // default 1.0
   - P1:    Attack      0.0 ... 1.0  // default 0.5
   - P2:    Release     0.0 ... 1.0  // default 0.5
   - P3:    Trig.level  0.0 ... 1.0  // default 0.5
   - P4:    Rel.level   0.0 ... 1.0  // default 1.0
   - P5:    Mod.Scale   0.0 ... 1.0  // default 1.0
'''
#### Dyn Follower
'''
   - TYPE:  "54"
   - P0:    Pregain     0.0 ... 1.0  // default 1.0
   - P1:    Attack      0.0 ... 1.0  // default 0.5
   - P2:    Release     0.0 ... 1.0  // default 0.5
   - P3:    Thres.level 0.0 ... 1.0  // default 0.5
   - P4:    Thres.Ratio 0.0 ... 1.0  // default 0.2
   - P5:    Mod.Scale   0.0 ... 1.0  // default 1.0
'''


### GENERATE 

#### Oscillator
'''
   - TYPE:  "4"
   - P0:    tuning      0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
'''

#### Sub Oscillator
'''
   - TYPE:  "18"
   - P0:    tuning      0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.5 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
'''

#### Fixed Oscillator
'''
   - TYPE:  "10"
   - P0:    tuning      0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
   - P2:    shape                    // default 0.0 (enum)
            - Sine      "0.000000"
            - Tri       "0.333333"
            - Saw       "0.500000"
            - Square    "1.000000"
'''

#### Hyper Oscillator
'''
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
'''

#### Noise Oscillator
'''
   - TYPE:  "7"
   - P0:    amp         0.0 ... 1.0  // default 0.5
'''

#### Impulse
'''
   - TYPE:  "39"
   - P0:    amp         0.0 ... 1.0  // default 1.0
'''

#### Sync Oscillator
'''
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
'''
#### PWM Oscillator
'''
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
'''
#### Sampler (basic)
'''
   - TYPE:  "58"
   - P0:    tuning      0.0 ... 1.0  // default 0.5
   - P1:    amp         0.0 ... 1.0  // default 0.5
'''

### Modifiers

#### Filter
'''
   - TYPE:  "1"
   - P0:    Cutoff      0.0 ... 1.0  // default 0.5
   - P1:    Resonance   0.0 ... 1.0  // default 0.0
   - P2:    kind                     // (enum)
            - Low Pass   "0.000000"
            - HighPass   "0.333333"
            - BandPass   "0.555555"
            - BandReject "1.0"

'''

#### Amplifier
'''
   - TYPE:  "6"
   - P0:    Factor      0.0 ... 1.0  // default 0.5

'''

#### Waveshaper
'''
   - TYPE:  "24"
   - P0:    Scale       0.0 ... 1.0  // default 0.5
   - P1:    Offset      0.0 ... 1.0  // default 0.5
   - P2-129 Gradient    [0.0 .. 1.0, ..]

'''

#### Delay
'''
   - TYPE:  "19"
   - P0:    Time        0.0 ... 1.0  // default 0.5    (249ms)
   - P1:    Feedback    0.0 ... 1.0  // default 0.0
'''

#### Keytracked Delay
'''
   - TYPE:  "20"
   - P0:    Time        0.0 ... 1.0  // default 0.5
   - P1:    Feedback    0.0 ... 1.0  // default 0.0
'''

#### Filter Delay (keytracked)
'''
   - TYPE:  "21"
   - P0:    Time        0.0 ... 1.0  // default 0.5
   - P1:    Feedback    0.0 ... 1.0  // default 0.0
   - P2:    Cutoff      0.0 ... 1.0  // default 0.5

'''

#### Invert
'''
   - TYPE:  "27"

'''

#### Rescale
'''
   - TYPE:  "26"
   - P0:    Factor      0.0 ... 1.0  // default 1.0
   - P1:    Offset      0.0 ... 1.0  // default 0.5
'''

#### Bit Crusher
'''
   - TYPE:  "34"
   - P0:    Bits        0.0 ... 1.0  // default 0.0  20-0
'''
#### Clipper
'''
   - TYPE:  "40"
   - P0     Upper.Lim   0.0 ... 1.0  // default 1.0
   - P1     Lower.Lim   0.0 ... 1.0  // default 0.0

'''
#### VU Tracker
'''
   - TYPE:  "41"
   - P0     Decay       0.0 ... 1.0  // default 0.5 (445ms)
   - P1     peak        0.0 ... 1.0  // default 1.0 (bool)   
'''

#### Crossfade
'''
   - TYPE:  "46"
   - P0     amp1          0.0 ... 1.0  // default 0.5
   - P1     amp2          0.0 ... 1.0  // default 0.5
   - P2     mix           0.0 ... 1.0  // default 0.5
   - P3     Audio (AR,CR) 0.0 ... 1.0  // default 1.0
'''

#### Env Trigger
'''
   - TYPE:  "51"
   - P0     pregain      0.0 ... 1.0  // default 1.0 (6.02dB)
   - P1     attack       0.0 ... 1.0  // default 0.5 (445ms)
   - P2     release      0.0 ... 1.0  // default 0.5 (445ms)
   - P3     Trig Level   0.0 ... 1.0  // default 0.5 (-12dB)
   - P4     Rel Level    0.0 ... 1.0  // default 1.0
   - P5     Mod Scale    0.0 ... 1.0  // default 1.0
'''

#### Dyn Follower
'''
   - TYPE:  "54"
   - P0     pregain      0.0 ... 1.0  // default 1.0 (6.02dB)
   - P1     attack       0.0 ... 1.0  // default 0.5 (445ms)
   - P2     release      0.0 ... 1.0  // default 0.5 (445ms)
   - P3     Thres.Level  0.0 ... 1.0  // default 0.5 (-12dB)
   - P4     Thres.Ratio  0.0 ... 1.0  // default 0.2
   - P5     Mod Scale    0.0 ... 1.0  // default 1.0
'''

#### Filter 2
'''
   - TYPE:  "56"
   - P0     Cutoff       0.0 ... 1.0  // default 0.5 (704Hz)
   - P1     Resonance    0.0 ... 1.0  // default 0.0
   - P2     kind                      // (enum)
            - Low Pass   "0.000000"
            - HighPass   "0.333333"
            - BandPass   "0.500000"
            - BandReject "1.0"
   - P3     keytrack     0.0 ... 1.0  // default 0.0 (bool)
'''

#### 3 band EQ
'''
   - TYPE:  "57"
   - P0     kind                      // (enum) 
            - Off        "0.000000"
            - peak       "0.333333"
            - low        "0.500000"
            - high       "1.000000"
   - P1     Freq         0.0 ... 1.0  // default 0.5 (704Hz)
   - P2     width        0.0 ... 1.0  // default 0.5
   - P3     Amp          0.0 ... 1.0  // default 0.0
   - P4     kind                      // (enum) 
            - Off        "0.000000"
            - peak       "0.333333"
            - low        "0.500000"
            - high       "1.000000"
   - P5     Freq         0.0 ... 1.0  // default 0.5 (704Hz)
   - P6     width        0.0 ... 1.0  // default 0.5
   - P7     Amp          0.0 ... 1.0  // default 0.0
   - P8     kind                      // (enum) 
            - Off        "0.000000"
            - peak       "0.333333"
            - low        "0.500000"
            - high       "1.000000"
   - P9     Freq         0.0 ... 1.0  // default 0.5 (704Hz)
   - P10    width        0.0 ... 1.0  // default 0.5
   - P11    Amp          0.0 ... 1.0  // default 0.0   
'''

### Output

#### Mono Out

'''
  type 0  
  p0  Volume 0.5
'''
#### Stereo Out
'''
  type 25  
  p0  Pan 0.5
  p1  Volume 0.5
'''
#### Arp
'''
  // todo... but backburner
  type 44
  p0   speed
  p1   ticks
  p2   octaves
  // this might be off by one, the progress indicator may be p3..
  p3,6,9...49  down   0.0 ... 1.0  // default 0.0 (bool)
  p4,7,10..50  note   0.0 ... 1.0  // default 0.5
  p5,8,11..51  up     0.0 ... 1.0  // default 0.0 (bool)
'''
### Connections
'''
These seem to be declared so

``` 
    <CONNECTION ID="127" FROM="3" TO="1" INPUTID="0" />

    - ID        :is a token
    - FROM..TO  :uses the POS token
    - INPUTID   :specifies which input socket on the destination

'''
### Globals

'''
it's one large non-dynamic blok (no socket inputs, only manual sliders)


 <GLOBAL 
   ID="118"   // some number
   Param_Chorus_Enable="0.000000" 
   Param_Chorus_Phasing="0.400000" 
   Param_Chorus_Speed="0.400000" 
   Param_Chorus_WetDry="0.400000" 
   Param_Delay_Cross="0.000000" 
   Param_Delay_Enable="0.000000" 
   Param_Delay_Feedback="0.000000" 
   Param_Delay_Length="0.400000" 
   Param_Delay_Spacing="0.000000" 
   Param_Delay_TempoSync="0.000000" 
   Param_Delay_Type="0.000000" 
   Param_Delay_WetDry="0.400000" 
   Param_Polyphony="0.500000" 
   Param_Reverb_Damping="0.300000" 
   Param_Reverb_Decay="0.500000" 
   Param_Reverb_Enable="0.000000" 
   Param_Reverb_ModAmount="0.250000" 
   Param_Reverb_ModSpeed="0.250000" 
   Param_Reverb_Roomsize="0.500000" 
   Param_Reverb_WetDry="0.300000" 
   Param_Voice_Bendrange="0.500000" 
   Param_Voice_Portamento="0.000000"
   Param_Voice_Transpose="0.500000" />
'''

 ### .blkx spec



'''svg
<?xml version="1.0" standalone="no" ?>
<storables>
    <GLOBAL ID="118" ...... />
    ...
    <BLOCK ID="119" TYPE="0" X="621" Y="361" POS="0" P0="0.500000" />
    ...
    ...
    <CONNECTION ID="127" FROM="3" TO="1" INPUTID="0" />
    ...
</storables>

where BLOK and CONNECTION are seemingly written in order of creation time. (ie POS allocation time? ..) -- this I have not looked at yet.
'''

# E O L 