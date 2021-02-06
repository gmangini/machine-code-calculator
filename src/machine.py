from memory import Memory

class Machine:
    def __init__(self, mem: Memory):
        """
        Takes existing memory and creates a machine ready to be run
        """
        self.__accumulator: int = 0
        self.__mem = mem
        self.__instruction_pointer = -1
        self.__instructions_map = {
            # '10': self.__read,
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

    def run(self):
        while True:
            self.__instruction_pointer += 1

            instruction = self.__mem.get_as_instruction(self.__instruction_pointer)
            opcode = instruction[0]
            operand = int(instruction[1])

            if opcode in self.__instructions_map:
                self.__instructions_map[opcode](operand)
            elif opcode == '43': # dip out
                break
            else:
                # Yeah, we shouldn't get here....
                exit(1)

    def __add(self, loc):
        self.__accumulator += self.__mem.get_as_int(loc)

    def __write(self, loc):
        print(self.__mem.get_as_int(loc))

    def __store(self, loc):
        self.__mem.set_from_int(loc, self.__accumulator)
