import sys

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
