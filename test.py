#importing the test cipher section
from ciphers.caesar import *


def main():
    #testing the mainual code
    manual('m', True)
    manual('a', True)
    manual('m', False)
    manual('a', False)

if __name__ == "__main__":
    main()