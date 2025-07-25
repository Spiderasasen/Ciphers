#imports
from Text.text_reader import reading_text
from ciphers.checking_if_manual import is_manual

#Dictionary to convert charcters to morse code
MORSE_CODE_DICT = {
    #Letters
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    #numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    #space
    ' ': '/',
    #other special characters
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-',  '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
}

#Dictionary to convery Morse code back to characters (inverse)
MORSE_CODE_DECODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

"""
This is the manual section of the code
"""

def manual_morse_code(valid, encryptions):
    #if the option is valid then start checking for encryptions
    if is_manual(valid):
        #checking if the user wants to encrypt something
        if encryptions:
            #message area to hold the answer
            message = ''

            #asking the user what to put
            user_input = input('What is your message?\n')

            message = encryption(user_input)

            print(message)

        #the user wants to decrpyt
        else:
            #asking the user what they want to decrypt
            user_input = input('What message do you want decrypt?\n')

            print(morse_decode(user_input))

    #if not return false
    return False

def encryption(message: str) -> str:
    """
    Encodes a plaintext message into Morse Code

    Args:
        message (str): the plaintext message to encode

    returns:
        str: the encoded Morse code String, with the spaces between characters and '/' for spaces
    """
    encoded_parts = []

    #process the message word by word to handel spaces correctly
    words = message.split(' ') #split by single spaces to get individual words

    for word in words:
        char_codes = []
        for char in word:
            #convert character to uppercase to match dictionary keys
            char_upper = char.upper()
            if char_upper in MORSE_CODE_DICT:
                char_codes.append(MORSE_CODE_DICT[char_upper])
            else:
                #handle char not in the directory
                pass

        #join characters within a word with single space
        encoded_parts.append(" ".join(char_codes))

    #join words with the standard morse code word separator (triple space or "/")
    return "/".join(encoded_parts) #use "/" as a separator

def morse_decode(morse_message: str) -> str:
    """
    Decodes a morse code message back to plaintext.

    args:
        morse_message (str): the morse code string to decode
                             assumes spaces between charcters and '/' for word breaks

    returns:
        str: the decoded plaintext message
    """
    decoded_words = []

    #split the entire morse message by the word seperator('/')
    morse_words = morse_message.strip().split(' / ') #.strip() to remove leading/trailings whitespace

    for morse_word in morse_words:
        decoded_chars = []

        #split each morse word by single spaces to get individual char codes
        morse_chars = morse_word.split(' ')
        for morse_char in morse_chars:
            if morse_char in MORSE_CODE_DECODE_DICT:
                decoded_chars.append(MORSE_CODE_DECODE_DICT[morse_char])
            elif morse_char == '': #handle multiple spaces between codes that results in a empty string
                continue
            else:
                #unkowen morse sequence
                decoded_chars.append('?') #place holder for unknown code
        decoded_words.append(" ".join(decoded_chars)) #joins the characters to form a word

    #joins words with a single space
    return " ".join(decoded_words)

#ai sections
def ai_morse_code(valid):
    #checking if the section is ai
    if not is_manual(valid):
        #importing the list of code that will be encrypted
        ciphers = reading_text('Text/text.txt')
        ciphers2 = reading_text('Text/morse_code_text.txt')

        #combining the 2 list
        combined_list = ciphers + ciphers2

        #new cipher that will be used to alter the orginal text
        clean_cipher = []

        #loop to remove the /n
        for text in combined_list:
            clean_cipher.append(text.strip())


        #returning the alter text to the newsit cipher
        ciphers = clean_cipher

        #list to hold the encrypted message
        encrypted_list = []

        #loop that will encrypt the message
        for message in ciphers:
            encrypted_list.append(encryption(message))

        #printing the encrpted message
        print(encrypted_list, '\nDo you know what each message says?')
        enter = input()

        #looping the decryptions
        for code in encrypted_list:
            #decodes the message
            print(morse_decode(code))
            #just used so the user can see the message
            enter = input()

    #else it will return false
    else:
        return False