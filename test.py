#importing the test cipher section
from ciphers.caesar import *
from ciphers.morse_code import *
from ciphers.atbash import *


def main():
    """Caeser code"""
    #testing the mainual code
    # manual('m', True)
    # manual('m', False)
    #testing the ai code
    # ai('a')

    """Morse Code"""
    # manual_morse_code('m', True)
    # manual_morse_code('m', False)
    # manual_morse_code('a', True)
    # ai_morse_code('a')

    """Atbash code"""
    # manual_atbash('m', True)
    # manual_atbash('m', False)
    ai_atbash('a')


if __name__ == "__main__":
    main()