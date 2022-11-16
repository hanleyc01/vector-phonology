from typing import Optional, TypedDict
import numpy as np

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
    
class Place(TypedDict):
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
    atr: float
    
class Sound(TypedDict):
    """
    A `Sound` is a structure composed of a `list[Major]` features,
    `list[Laryngeal]` features, `list[Place]` features, and
    `aux`, which is for any features that do not fit into the other sets
    """
    major: Major
    laryngeal: Laryngeal
    place: Place
    
class SArray:
    """
    Class which encapsulates a `Sound` in the form of a single `np.ndarray`
    """
    arr: np.ndarray
    
    def __init__(self, sound: Sound) -> None:
        major = list(sound['major'].values())
        laryngeal = list(sound['laryngeal'].values())
        place = list(sound['place'].values())
        self.arr = np.array(major + laryngeal + place)
    
    def __str__(self) -> str:
        return str(self.arr)