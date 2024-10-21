
## Defining constants in Pyhton - various ways 

"""
#1
class Constants:
    @property
    def PI(self):
        return 3.14159

    @property
    def MAX_USERS(self):
        return 1000

constants = Constants()

# constants.PI = 3.14 # This raises AttributeError:



#2 Final is just a hint. it does not enforce this constraint
from typing import Final

PI: Final = 3.14159
MAX_USERS: Final = 1000

PI = 3.14 

print(PI)
"""


#3
from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
    PI: float = 3.14159
    MAX_USERS: int = 1000

constants = Constants()

#constants.PI = 3.14 #This raises dataclasses.FrozenInstanceError: cannot assign to field 'PI'
