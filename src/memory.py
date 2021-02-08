import re
from typing import Optional

four_nums = re.compile("^[0-9]{4}$")

class Memory:
    """
    Memory space for the machine
    """

    def __init__(self):
        """
        Initialize new memory space
        """
        self.__vals: List[Tuple[str, str]] = []
    
    def get_size(self) -> int:
        return len(self.__vals)

    def set_next(self, tup: tuple[str, str]):
        """
        Add a new tuple to memory
        """
        self.__vals.append(tup)

    def get_as_int(self, location: int):
        """
        Gets a memory location as an int
        """
        tup = self.__vals[location]
        return int(tup[0] + tup[1])

    def get_as_instruction(self, location):
        """
        Gets the raw instruction tuple
        """
        return self.__vals[location]

    def set_from_int(self, loc, num: int):
        as_str = str(num)
        self.__vals[loc] = (as_str[0:2], as_str[2:])

    def set_from_word(self, loc, word: tuple[str, str]):
        self.__vals[loc] = word

def parse_word(word: str) -> Optional[tuple[str, str]]:
    match = four_nums.match(word)
    if match is None:
        return None
    return (match.string[0:2], match.string[2:])
