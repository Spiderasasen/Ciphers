#importing the test cipher section
from ciphers.caesar import *
from ciphers.morse_code import *


def main():
    #testing the mainual code
    # manual('m', True)
    # manual('m', False)

    #testing the ai code
    # ai('a')
    manual_morse_code('m', True)
    manual_morse_code('m', False)
    manual_morse_code('a', True)

if __name__ == "__main__":
    main()