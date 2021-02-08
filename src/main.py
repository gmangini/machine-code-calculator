from memory import Memory
from machine import Machine, parse_word
from utils import input_with_echo
import re

def main() -> None:
    '''Main'''
    mem = Memory()

    print('Starting...')
    print()
    print('Please input your program:')
    print()

    # This is the main read loop for getting instructions
    while True:
        input_str = input_with_echo(f'[{mem.get_size():04}] ')
        word = parse_word(input_str)

        # is the input an instruction?
        if word is not None:
            mem.set_next(word)
        elif input_str.startswith('q'):
            print('Input end.')
            print('Running machine')
            print()
            break

    machine = Machine(mem, lambda: input_with_echo(" > "))
    machine.run()


if __name__ == '__main__':
    main()

