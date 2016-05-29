import blok_units

from blok_units import blok_dict


def next_number_generator(start=0):
    i = start
    while True:
        yield i
        i += 1



def get_ID():
    ...

class pBlk:

    defaults = ['ID TYPE X Y POS'].split(' ')

    def __init__(self, name, xy):
        self.name = name
        self.TYPE = get_type(name)
        self.ID = get_ID()
        self.POS = get_POS()
        self.X = xy[0]
        self.Y = xy[1]

    def params(self, parameters):
        ...

    def __str__(self):
        ret_str = ["<BLOK"]
      
        for d in self.defaults:
            ret_str.append("{0}=\"{1}\"".format(d, getattr(self, d)))

        for idx, p in enumerate(self.params):
            ret_str.append("P{0}=\"{1}\"".format(str(idx), p))
      
        ret_str.append('/>')

        return ' '.join(ret_str)


class Connect:

    '''
    - ID        :is a token
    - FROM..TO  :uses the POS token
    - INPUTID   :specifies which input socket on the destination
    '''

    def __init__(self, _from, _to, socket=None, index=None):
        self.ID = get_ID()
        self.FROM = _from.ID
        self.TO = _to.ID
        if index:
            self.INPUTID = index
        elif socket:
            self.INPUTID = get_index_from_socketname(socket)
        else:
            print('from {0} to {1}.{2} failed..'.format(self.FROM, self.TO, self.INPUTID))

    def __str__(self):
        const ="<CONNECTION ID=\"{0}\" FROM=\"{1}\" TO=\"{2}\" INPUTID=\"{3}\" />"
        return const.format(self.ID, self.FROM, self.TO, self.INPUTID)





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