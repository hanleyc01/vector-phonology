from typing import Optional, TypedDict
from ipaparser import IPA, IPASymbol # type: ignore

class Major(TypedDict):
    """
    Major class features are represented by a balanced ternary, some
    number, paradigmatically a whole number, within the inclusive range
    [-1,1]; where -1 := the *lack* of any feature value for that segment,
    0 := the negative value for that feature of that segment, and
    1 := the positive value for that feature of that segment
    """
    syll: float
    cons: float
    son: float
    contin: float
    del_rel: float
    lat: float
    nas: float
    stri: float
    
class Laryngeal(TypedDict):
    """
    Laryngeal class features are represented by a balanced ternary, some
    number, paradigmatically a whole number, within the inclusive range
    [-1,1]; where -1 := the *lack* of any feature value for that segment,
    0 := the negative value for that feature of that segment, and
    1 := the positive value for that feature of that segment
    """
    voice: float
    spr_gl: float
    cons_gl: float
    
class Place:
    """
    Place class features are represented by a balanced ternary, some
    number, paradigmatically a whole number, within the inclusive range
    [-1,1]; where -1 := the *lack* of any feature value for that segment,
    0 := the negative value for that feature of that segment, and
    1 := the positive value for that feature of that segment
    """
    ant: float
    cor: float
    dist: float
    high: float
    low: float
    back: float
    round: float
    lab: float

class Sound(TypedDict):
    """
    A `Sound` is a structure composed of a `list[Major]` features,
    `list[Laryngeal]` features, `list[Place]` features, and
    `aux`, which is for any features that do not fit into the other sets
    """
    major_class: list[Major]
    laryngeal: list[Laryngeal]
    place: list[Place]
    aux: None
    
if __name__ == '__main__':
    i: Major = {
        'syll': 1,
        'cons': -0,
        'son': 1,
        'contin': 1,
        'del_rel': -1,
        'lat': -1,
        'nas': 0,
        'stri': -1
        }
    print(list(i.values()))
