# imports
from Text.text_reader import reading_text
from ciphers.checking_if_manual import is_manual

"""
THIS IS THE MANAUL SECTION OF THE CODE
"""
def manual_atbash(option, encryption):
    #checking if the code is manual
    if is_manual(option):
        #checking if the user wants to encrypt something
        if encryption:
            #asking the user what they want to encrypt
            user_input = input('What will you like to encrypt?\n')

            #starts to encrypting the message and printing it out
            print(atbash_encrypt(user_input))

        #if not, start decrypting a message
        else:
            #asking the user what they want to decrypt
            user_input = input('What will you like to decrypt?\n')

            #printing the message
            print(atbash_decrypt(user_input))


    #if not, return false
    else:
        return False

def atbash_encrypt(message: str) -> str:
    """
    Encrypts a plaintext message using the atbash cipher
    (encrption and decryption are the same for atbash)

    Args:
        message (str): the plaintext message to encrypt

    returns:
        str: the atbash-encrypted ciphertext
    """
    processed_message = ""

    for char in message:
        if 'a' <= char <= 'z':
            #calculates the 0 based index for lowercase
            original_index = ord(char) - ord('a')
            #calculate reversed index: 25 - orginal index
            new_char_code = ord('a') + (25 - original_index)
            processed_message += chr(new_char_code)
        elif 'A' <= char <= 'Z':
            #calculates the 0 based index for uppercase
            original_index = ord(char) - ord('A')
            #calculate reversed index: 25 - orginal index
            new_char_code = ord('A') + (25 - original_index)
            processed_message += chr(new_char_code)
        else:
            #nothing will happen, so let it be
            processed_message += char

    return processed_message

def atbash_decrypt(message:str) -> str:
    """
    Decrypts the message that is given
    (both encryption and decryption are the same)

    Args:
         message (str): the message we are given to decrypt

    Returns:
        str: the orgainal message that is now decrypted
    """
    return atbash_encrypt(message) #just call the encryption function

"""
THIS IS THE AI SECTION OF THE CODE
"""
def ai_atbash(valid):
    #checking if the user really ment to choose ai
    if not is_manual(valid):
        #making a list of ciphers
        ciphers = reading_text('Text/text.txt')

        #cleaning up the ciphers
        clean_chipher = []

        for cipher in ciphers:
            clean_chipher.append(cipher.strip())

        #adding the clean cipher to the orginal cipher list
        ciphers = clean_chipher

        #encrypting the ciphers
        encrypted_cipher = []

        for message in ciphers:
            encrypted_cipher.append(atbash_encrypt(message))

        #showing the user all the ciphers
        print(encrypted_cipher, '\nDo you know the original message from the cipher?')
        enter = input()

        #decode the cipher
        for message in encrypted_cipher:
            #prints out the decrypted message
            print(atbash_decrypt(message))
            #waits for the user to press enter
            enter = input()

    #otherwise return false
    return False
