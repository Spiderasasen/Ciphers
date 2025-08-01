#imports
from ciphers import caesar
from ciphers import checking_if_manual
from ciphers.checking_if_manual import is_manual
from Text.text_reader import reading_text

#calling the manual option
def rot13_manual(valid, encyprtion):
    #checking if its manual
    if is_manual(valid):
        #if the user wanted to encypt something
        if encyprtion:
            #asking the user what they want to encrypt
            user_input = input('What do you want to encrypt?\n')

            #takes the message and prints it out
            print(rot13_encrypt(user_input))

        #if the user does not want to encypt anything but wants to decypt
        else:
            #asking the user what they want to decrypt
            user_input = input('What do you want to decrypt?\n')

            #takes the message and runs it in the ceaser decyption
            print(caesar.decryptions_ceaser(user_input))

    #if not, return false
    else:
        return False

#Wapper function
def rot13_encrypt(message: str) -> str:
    #encrypts a message using the caesar cipher encyption
    return caesar.encryptions(message, 13)

"""AI Code"""
#ai section of the code
def ai_rot13(valid):
    #checking if its really ai
    if not is_manual(valid):
        #importing the list of words that will be incrpted
        ciphers = reading_text('Text/text.txt')

        #new list that will be used to alter the orginal text
        clean_cipher = []

        #removing the \n in the line
        for text in ciphers:
            clean_cipher.append(text.strip())

        #mergin both cipher and clean_cipher
        ciphers = clean_cipher

        #var that will be used to get a syntax for the ciphers encrpytion
        shifts = 13

        #list that will hold the new encypted messages
        encrypt_message = []

        #loop that will encrypt all the ciphers
        for cipher in ciphers:
            #holding the encypted message
            encrypt_message.append(caesar.encryptions(cipher, shifts))

        #printing out all the chipers so the player can see
        print(encrypt_message, '\n Can you guess the messages?')
        enter = input()

        #looping through all the ciphers and showing the player all the decryted ciphers
        for message in encrypt_message:
            #this function just deciphers the message
            caesar.decryptions_ceaser(message)
            #just there for the user can see the deciphered message
            enter = input()

    #its actually manual not ai, so return false
    return False