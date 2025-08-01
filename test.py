#importing the test cipher section
from ciphers.caesar import *
from ciphers.morse_code import *
from ciphers.atbash import *
from ciphers.ROT13 import *

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
    # ai_atbash('a')

    """ROT13"""
    # word = rot13_encrypt('Hello World')
    # print(word)
    # rot13_manual('m', True)
    # rot13_manual('a', True)
    # rot13_manual('a', False)
    # rot13_manual('m', False)
    # ai_rot13('m')
    # ai_rot13('a')

if __name__ == "__main__":
    main()