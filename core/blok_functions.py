'''
docstring: 


'''
import os
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
        self.all_params = BLOKS[self.name]
        self.params = self.make_params()
        self.remaps = {}
        self.map_paramindex_from_parameters()  # fills remaps dict
        storables.append(self)

    def make_params(self):
        '''
        restructures simple BLOK dict
        '''

        def get_innerdict(outer_dict):
            '''gets first key/value of the inner dict '''
            return [i for i in outer_dict.values()][0]

        parameter_dict = {}
        for p in self.all_params.keys():

            if p == 'TYPE':
                continue

            if '-' in p:
                start, finish = p.split('-')
                p_start, p_finish = int(start[1:]), int(finish[1:])
                param_list = get_innerdict(self.all_params.get(p))

                for i in range(p_finish-p_start+1):
                    idx = i + p_start
                    my_val = param_list[i]
                    parameter_dict[idx] = my_val
            else:
                idx = int(p[1:])
                parameter_dict[idx] = get_innerdict(self.all_params.get(p))
        return parameter_dict


    def map_paramindex_from_parameters(self):
        ''' things '''

        def get_innerdict_key(outer_dict):
            '''gets first key/value of the inner dict '''
            return [i for i in outer_dict.keys()][0]

        for m in self.all_params.keys():
            if m == 'TYPE':
                continue
            if '-' in m:
                continue
            name = get_innerdict_key(self.all_params[m])    
            self.remaps[name] = int(m[1:])


    def set_params(self, **parameters):
        '''to be used when setting non defaults'''
        for name, value in parameters.items():
            idx = self.remaps[name]
            self.params[idx] = value

    def get_index_from_socketname(self, socketname):
        '''ta -- not implemented yet'''
        if socketname == 'audio_in':
            return 0
        elif socketname in self.params:
            return 1

    def __str__(self):
        ret_str = ["<BLOK"]
      
        for d in self.standard:
            ret_str.append("{0}=\"{1}\"".format(d, getattr(self, d)))

        for idx, p in enumerate(self.params):
            my_val = self.params.get(p)
            ret_str.append("P{0}=\"{1:6f}\"".format(str(idx), my_val))
      
        ret_str.append('/>')

        return ' '.join(ret_str)


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
        if index:
            self.INPUTID = index
        elif socket:
            self.INPUTID = self.TO.get_index_from_socketname(socket)
        else:
            print('from {0} to {1}.{2} failed..'.format(self.FROM, self.TO, self.INPUTID))
        storables.append(self)


    def __str__(self):
        const = "<CONNECTION ID=\"{0}\" FROM=\"{1}\" TO=\"{2}\" INPUTID=\"{3}\" />"
        return const.format(self.ID, self.FROM, self.TO, self.INPUTID)


# SubOsc1 = pBlk('Sub.Osc', (130, 140))
# SubOsc2 = pBlk('Sub.Osc', (130, 180))
# Env1 = pBlk('Env.advanced', (30, 180))
# con1 = Connect(Env1, SubOsc2, index=1)
# SubOsc1.params[2] = 0.333333
# Env1.set_params(attack=0.88, decay=0.45, amount=0.2)


# pCompile()
