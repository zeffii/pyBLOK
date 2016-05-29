'''
docstring: 


'''

from .blok_units import BLOKS, GLOBAL, DOC


def next_number_generator(start=0):
    '''makes new next number given a start'''
    i = start
    while True:
        yield i
        i += 1

ID_SUPPLY = next_number_generator(3)
POS_SUPPLY = next_number_generator()

def get_id():
    '''id is used for'''
    return next(ID_SUPPLY)

def get_pos():
    '''pos is used for'''
    return next(POS_SUPPLY)

def get_type(name):
    ''' convert name to type with params'''
    return BLOKS[name]


class pBlk:
    '''
    produce an instance of a the BLOK representation.
    this will contain the members declared in __init__.

    '''

    defaults = 'ID TYPE X Y POS'.split(' ')

    def __init__(self, name, xy):
        self.name = name
        self.TYPE = get_type(name)
        self.ID = get_id()
        self.POS = get_pos()
        self.X = xy[0]
        self.Y = xy[1]

    def params(self, parameters):
        '''ta'''
        pass

    def get_index_from_socketname(self, socket):
        '''ta'''
        pass

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
        self.ID = get_id()
        self.FROM = _from.ID
        self.TO = _to.ID
        if index:
            self.INPUTID = index
        elif socket:
            self.INPUTID = self.TO.get_index_from_socketname(socket)
        else:
            print('from {0} to {1}.{2} failed..'.format(self.FROM, self.TO, self.INPUTID))

    def __str__(self):
        const = "<CONNECTION ID=\"{0}\" FROM=\"{1}\" TO=\"{2}\" INPUTID=\"{3}\" />"
        return const.format(self.ID, self.FROM, self.TO, self.INPUTID)
