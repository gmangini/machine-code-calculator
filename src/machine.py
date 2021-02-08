from memory import Memory, parse_word
from enum import Enum, auto
from typing import Callable

class State(Enum):
    RUNNING = auto()
    DONE = auto()

class Machine:
    def __init__(self, mem: Memory, reader: Callable[[], str]):
        """
        Takes existing memory and creates a machine ready to be run
        The reader allows for swapping input implementation as needed. This will be helpful when a GUI needs to be introduced
        """
        self.__accumulator: int = 0
        self.__mem = mem
        self.__reader = reader
        self.__instruction_pointer = -1
        self.__instructions_map = {
            '10': self.__read,
            '11': self.__write,
            # '20': self.__load,
            '21': self.__store,
            '30': self.__add,
            # '31': self.__subtract,
            # '32': self.__divide,
            # '33': self.__multiply,
            # '40': self.__branch,
            # '41': self.__branch_neg,
            # '42': self.__branch_zero,
        }

    def run_step(self) -> State:
        """
        Runs the machine step-by-step. Returns the machines current state
        """
        self.__instruction_pointer += 1

        instruction = self.__mem.get_as_instruction(self.__instruction_pointer)
        opcode = instruction[0]
        operand = int(instruction[1])

        if opcode in self.__instructions_map:
            self.__instructions_map[opcode](operand)
        elif opcode == '43':
            # dip out
            return State.DONE
        else:
            # Yeah, we shouldn't get here....
            exit(1)

        return State.RUNNING


    def run(self):
        """
        Runs `run_step` until the machine finishes
        """
        while self.run_step() != State.DONE:
            pass

    def __add(self, loc):
        self.__accumulator += self.__mem.get_as_int(loc)

    def __write(self, loc):
        print(self.__mem.get_as_int(loc))

    def __store(self, loc):
        self.__mem.set_from_int(loc, self.__accumulator)

    def __read(self, loc):
        got = self.__reader()
        word = parse_word(got)
        if word is None:
            print("Expected input to be of form 0000.")
            exit(1)
        else:
            self.__mem.set_from_word(loc, word)
