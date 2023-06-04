# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : data__dict.py
# - author : yc0325lee
# - created : 2022-10-16 12:26:04 by lee2103
# - modified : 2022-10-16 12:26:04 by lee2103
# - description : 
#
# - tuple
# ; immutable & hashable
# - construction
# (1) using a pair of parentheses to denote the empty tuple: ()
# (2) using a trailing comma for a singleton tuple: a, or (a,)
# (3) separating items with commas: a, b, c or (a, b, c)
# (4) using the tuple() built-in: tuple() or tuple(iterable)
#
# - an object is hashable
#   (1) if it has a hash value which never changes during its lifetime
#       (it needs a __hash__() method)
#   (2) be compared to other objects (it needs an __eq__() method)
#   (3) hashable objects which compare equal must have the same hash value.
#       'if a == b' -> hash(a) == hash(b)
# ; the atomic immutable types (str, bytes, numeric types) are all hashable. a
#   frozen set is always hashable, because its elements must be hashable by
#   definition.
# ; a tuple is hashable only if all its items are hashable.
# ----------------------------------------------------------------------------


### -----------------------------------
### DICTIONARIES ###
## properties: unordered, iterable, mutable, can contain multiple data types
## made of key-value pairs
## keys must be unique, and can be strings, numbers, or tuples
## values can be any type

# create an empty dictionary (two ways)
if True:
    empty_dict = {}
    empty_dict = dict()
    #print(isinstance(empty_dict, abc.Mapping))

if False:
    # creating a dictionary (1)
    family = {
        'dad'  : 'homer',
        'mom'  : 'marge',
        'size' : 6
    }
    
    # creating a dictionary (2)
    family = dict(
        dad  = 'homer',
        mom  = 'marge',
        size = 6
    )

    # creating a dictionary (3)
    list_of_tuples = [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
    family = dict(list_of_tuples) # convert a list of tuples into a dictionary
                                  # https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    # creating a dictionary (4)
    list_of_tuples = zip(['dad', 'mom', 'size'], [1, 2, 3])
    family = dict(list_of_tuples)
    
    # examine a dictionary
    family['dad']       # returns 'homer'
    len(family)         # returns 3
    'mom' in family     # returns True
    'marge' in family   # returns False (only checks keys)
    
    # returns a list (Python 2) or an iterable view (Python 3)
    # Python 2 -> list
    # Python 3 -> dict_keys, dict_values, dict_items (iterable)
    family.keys()       # keys: ['dad', 'mom', 'size']
    family.values()     # values: ['homer', 'marge', 6]
    family.items()      # key-value pairs: [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
    
    # modify a dictionary (does not return the dictionary)
    family['cat'] = 'snowball'              # add a new entry
    family['cat'] = 'snowball ii'           # edit an existing entry
    del family['cat']                       # delete an entry
    family['kids'] = ['bart', 'lisa']       # dictionary value can be a list
    family.pop('dad')                       # remove an entry and return the value ('homer')
    family.update({'baby':'maggie', 'grandpa':'abe'})   # add multiple entries
    
    # access values more safely with 'get'
    family['mom']                       # returns 'marge', error upon non-existing key
    family.get('mom')                   # equivalent, None upon non-existing key
    family['grandma']                   # throws an error since the key does not exist
    family.get('grandma')               # returns 'None' instead
    family.get('grandma', 'not found')  # returns 'not found' (the default)
    
    # access a list element within a dictionary
    family['kids'][0]                   # returns 'bart'
    family['kids'].remove('lisa')       # removes 'lisa'
    
    # string substitution using a dictionary
    'youngest child is %(baby)s' % family   # returns 'youngest child is maggie'
    
    # operation and looping
    if "mom" in family:
        print("mon's name is {}".format(family['mom']))
    
    for key in family.keys():
        print(family[key])
    
    for value in family.values():
        print(family[key])
    
    for key, value in family.items():
        print("key= {}, value= {}".format(key, valiue))
    
    # reset a dict
    family.clear()

if False:
    # dict comprehension
    pass

if False:
    # -------------------------------------
    # - update([other])
    # ; update the dictionary with the key/value pairs from other,
    #   overwriting existing keys. return none.
    pass
