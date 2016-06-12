'''
docstring: 
pylinting : 
   "disable": [
       "C0103", "C0413", "R0903", "I0011", "E0401", "C0111",
       "C0301", "W0104", "W0106", "W0105", "W0612"
    ],

'''

from blok_units import BLOKS, GLOBAL, DOC


class ID_producer:
    '''
    when a blok gets an ID it should increase the ID by two, 
    when a connection gets an ID it should increase it by only one
    '''
    idx = 0
    def __init__(self, start=0):
        self.idx = start

    def new_id(self, origin):
        temp_idx = self.idx
        self.idx += {'BLOK': 2, 'CONNECTION':1}.get(origin)
        return temp_idx



def next_number_generator(start=0):
    '''makes new next number given a start'''
    i = start
    while True:
        yield i
        i += 1


POS_SUPPLY = next_number_generator()
ID_gen = ID_producer(3)


def get_id(kind):
    '''id is used for'''
    return ID_gen.new_id(kind)

def get_pos():
    '''pos is used for'''
    return next(POS_SUPPLY)

def get_type(name):
    ''' convert name to type with params'''
    return BLOKS[name]['TYPE']



storables = []

def pCompile(path=None, silent=1):
    '''produce a .blkx'''
    patches = ''.join([('    ' + str(stored) + '\n') for stored in storables])
    doc = DOC.format(globals=GLOBAL, patching=patches)

    if path:
        with open(path, 'w') as blkx:
            blkx.write(doc)
        if not silent:
            print(doc)
    else:
        print(doc)




class pBlk:
    '''
    produce an instance of a the BLOK representation.
    this will contain the members declared in __init__.

    '''
    # pylint: disable=too-many-instance-attributes

    standard = 'ID TYPE X Y POS'.split(' ')


    def __init__(self, name, xy):
        self.name = name
        self.TYPE = get_type(name)
        self.ID = get_id('BLOK')
        self.POS = get_pos()
        self.X = xy[0]
        self.Y = xy[1]
        
        self.all_params = BLOKS[self.name]['params']
        self.params = {}
        self.remaps = {}
        self.make_params()
        # self.add_properties()
        
        storables.append(self)

    # def add_properties(self):
    #     '''
    #     adding dynamic properties setter / getter
    #     learn http://www.python-course.eu/python3_properties.php

    #     '''
    #     def stump(blok, param_idx, val=None):
    #         if isinstance(val, (float, tuple)):
    #             blok.params[param_idx] = val
    #         return blok.params[param_idx]

    #     for k, v, in self.remaps.items():
    #         param_name = k
    #         param_idx = v
    #         if isinstance(v, tuple):
    #             continue

    #         setter_func = lambda self, val: stump(self, param_idx, val)
    #         setattr(self, param_name, setter_func)

    def make_params(self):
        '''
        restructures simple BLOK dict
        - This is run only once, in the init portion.
        '''

        parameter_dict = {}
        for idx, name, value, can_connect in self.all_params:

            if isinstance(idx, int) and idx >= 0:
                self.params[idx] = value

            elif isinstance(idx, tuple):
                # only other option is a tuple
                p_start, p_finish = idx
                for i, v in enumerate(value):
                    j = i + p_start
                    self.params[j] = v

            if isinstance(idx, tuple) or idx >= 0:
                self.remaps[name] = idx

    def set_params(self, **parameters):
        '''to be used when setting non defaults'''
        for name, value in parameters.items():
            idx = self.remaps[name]
            if isinstance(idx, tuple):
                '''this disects those parameters that are Float Vectors'''
                start, end = idx
                for j, i in enumerate(range(start, end+1)):
                    self.params[i] = value[j]
            else:
                '''single value Float based parameters'''
                self.params[idx] = value

    def set_pvector(self, parameters):
        '''
        Env.custom : P4-P195 "envelope" [range(4, 196)]  # 192
        Env.advanced : P6-P17 "envelope" [range(6, 18)]  # 12
        keytrack : P0-P127 "range" [range(128)]          # 128
        Waveshaper : P2-P129 "gradient" [range(2, 130)]  # 128
        '''
        indices = {
            'EnvCustom': list(range(4, 196)),
            'EnvAdvanced' : list(range(6, 18)),
            'keytrack' : list(range(128)),         
            'Waveshaper' : list(range(2, 130))
        }.get(self.name)

        if not len(indices) == len(parameters):
            msg1 = 'setting pvector encountered length mismatch '
            msg2 = 'got {0}, expected {1}'
            print(msg1 + msg2.format(len(parameters, len(indices))))
            return

        for i, idx in enumerate(indices):
            self.params[idx] = parameters[i]

    def get_index_from_socketname(self, socketname):
        '''ta -- not implemented yet'''
        if socketname == 'audio_in':
            return 0
        elif socketname in self.params:
            return 1

    def index(self, idx):
        return (self, idx)

    def __str__(self):
        ret_str = ["<BLOCK"]
      
        for d in self.standard:
            ret_str.append("{0}=\"{1}\"".format(d, getattr(self, d)))
        
        for idx, (key, val) in enumerate(sorted(self.params.items())):
            ret_str.append("P{0}=\"{1:6f}\"".format(str(idx), val))

        ret_str.append('/>')

        return ' '.join(ret_str)

    def __gt__(self, other):
        if isinstance(other, tuple):
            Connect(self, other[0], index=other[1])


class Connect:

    '''
    - ID        :is a token
    - FROM..TO  :uses the POS token
    - INPUTID   :specifies which input socket on the destination
    '''

    def __init__(self, _from, _to, socket=None, index=None):
        self.ID = get_id('CONNECTION')
        self.FROM = _from.POS
        self.TO = _to.POS
        if isinstance(index, int):
            self.INPUTID = index
        elif socket:
            self.INPUTID = self.TO.get_index_from_socketname(socket)
        else:
            print('from {0} to {1}.{2} failed..'.format(self.FROM, self.TO, self.INPUTID))
        storables.append(self)


    def __str__(self):
        const = "<CONNECTION ID=\"{0}\" FROM=\"{1}\" TO=\"{2}\" INPUTID=\"{3}\" />"
        return const.format(self.ID, self.FROM, self.TO, self.INPUTID)


# SubOsc1 = pBlk('SubOsc', (130, 140))
# SubOsc2 = pBlk('SubOsc', (130, 180))
# Env1 = pBlk('EnvAdvanced', (30, 180))
# con1 = Connect(Env1, SubOsc2, index=1)
# SubOsc1.params[2] = 0.333333
# Env1.set_params(attack=0.88, decay=0.45, amount=0.2)


# pCompile()
