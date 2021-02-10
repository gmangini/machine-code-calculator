import re
from typing import Optional, Tuple, List
from enum import Enum, auto

signed_four_nums = re.compile("^[-+]?[0-9]{4}$")


class Sign(Enum):
    NEGATIVE = '-'
    POSITIVE = '+'


Word = Tuple[Sign, str, str]


class Memory:
    """
    Memory space for the machine
    """
    def __init__(self) -> None:
        """
        Initialize new memory space
        """
        self.__vals: List[Word] = []

    def get_size(self) -> int:
        return len(self.__vals)

    def set_next(self, tup: Word) -> None:
        """
        Add a new tuple to memory
        """
        self.__vals.append(tup)

    def get_as_int(self, location: int) -> int:
        """
        Gets a memory location as an int
        """
        tup = self.__vals[location]

        return int(tup[0].value + tup[1] + tup[2])

    def get_as_instruction(self, location: int) -> Word:
        """
        Gets the raw instruction tuple
        """
        return self.__vals[location]

    def set_from_int(self, loc: int, num: int) -> None:
        as_str = f'{abs(num):04}'
        sign = Sign.NEGATIVE if num < 0 else Sign.POSITIVE
        self.__vals[loc] = (sign, as_str[0:2], as_str[2:])

    def set_from_word(self, loc: int, word: Word) -> None:
        self.__vals[loc] = word


def parse_word(word: str) -> Optional[Word]:
    match = signed_four_nums.match(word)
    if match is None:
        return None
    if len(match.string) == 4:
        return (Sign.POSITIVE, match.string[0:2], match.string[2:])
    elif len(match.string) == 5:
        if match.string[0] == '-':
            return (Sign.NEGATIVE, match.string[0:2], match.string[2:])
        else:
            return (Sign.POSITIVE, match.string[0:2], match.string[2:])
    else:
        # This should not be possible
        exit(1)
    return (match.string[0:2], match.string[2:])
