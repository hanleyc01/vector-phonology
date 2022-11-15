from distfeat import Sound, Major, Laryngeal, Place, SArray
from pprint import pprint
import random
import numpy as np

###            ###
###    NOTES   ###
###            ###
# Simple test case to try and work out how to deal with Nengo SPA;
# TODO:
# [x] Generate a list of random "words", which are a collection of sounds.
# [ ] Create some kind of "memory" system, represented by a matrix
# [ ] Figure out how these interact (like a probe)

# Number of elements in the Major class
_MAJOR_LEN = 8
# Number of elements in the laryngeal class
_LAR_LEN = 3
# Number of elements in the Place class
_PL_LEN = 8

def get_major() -> Major:
    l = []
    for _ in range(_MAJOR_LEN):
        l.append(random.uniform(-1.0,1.0))
    m: Major = {
            'syll': l[0],
            'cons': l[1],
            'son': l[2],
            'contin': l[3],
            'del_rel': l[4],
            'lat': l[5],
            'nas': l[6],
            'stri': l[7],
            }
    return m

def get_laryngeal() -> Laryngeal:
    l = []
    for _ in range(_LAR_LEN):
        l.append(random.uniform(-1.0,1.0))
    m: Laryngeal = {
            'voice': l[0],
            'spr_gl': l[1],
            'cons_gl': l[2]
            }
    return m
    
    
def get_place() -> Place:
    l = []
    for _ in range(_PL_LEN):
        l.append(random.uniform(-1.0,1.0))
    m: Place = {
            'ant': l[0],
            'cor': l[1],
            'dist': l[2],
            'high': l[3],
            'low': l[4],
            'back': l[5],
            'round': l[6],
            'lab': l[7]
            }
    return m

def get_sound() -> Sound:
    """
    Generates a random `Sound`
    """
    major_class_features = get_major()
    laryngeal_class_features = get_laryngeal()
    place_class_features = get_place()
    sound: Sound = {
            'major': major_class_features,
            'laryngeal': laryngeal_class_features,
            'place': place_class_features}
    return sound

def get_word(length=None) -> list[Sound]:
    if not length:
        length = random.randint(1,10)
    word = []
    for j in range(length):
        s = get_sound()
        word.append(s)
    return word

def get_words(length=None) -> list[list[Sound]]:
    """
    Generates a `list[list[Sound]]`
    """
    if not length:
        length = random.randint(1,3)
    words = []
    for i in range(length):
        words.append(get_word())
    return words
    
s_word = lambda y: list(map(lambda x: SArray(x), y)) # type: ignore
s_words = lambda x: list(map(lambda y: s_word(y), x))

if __name__ == '__main__':
    words = get_words()
    s_ws = s_words(words)
    print(s_ws)
