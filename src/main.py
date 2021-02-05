from memory import Memory
from machine import Machine
import re
import sys

four_nums = re.compile("^[0-9]{4}$")

# print(sys.stdin.isatty())
def input_with_echo(prompt: str) -> str:
    """
    Since the input function doesn't echo for pipes, I force that here (which makes for easier testing)
    """
    if sys.stdin.isatty():
        # it's not piped, proceed normally
        return input(prompt)
    else:
        got = input(prompt)
        print(got)
        return got

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
        match = four_nums.match(input_str)

        # is the input an instruction?
        if match is not None:
            match.string[0:2]
            mem.set_next((match.string[0:2], match.string[2:]))
        elif input_str == 'q':
            print('Input end.')
            break

    machine = Machine(mem)
    machine.run()


if __name__ == '__main__':
    main()

