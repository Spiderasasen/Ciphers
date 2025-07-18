"""
    if the option is false, its maunal
        if encrpytion is true its encption otherwise its decryption
"""
import sys


#checking if the option is manual or not
def is_manual(option):
    #if option is true, then we enter manual
    if option == 'm':
        return True
    #otherwise its ai
    return False


"""Manual code"""
def manual(valid, encryption):
    #checking if the option is manual first
    if is_manual(valid):
        #checking if the code is encrpytion or not
        if encryption:
            #user puts there message
            user_input = input('Please enter your message...\n')

            #asking the number of shifts the user wants
            while True:
                #checking the user enter a valid number
                try:
                    shifts = int(input('\nHow many shifts would you want? \n1 - 25\n'))

                    #if the number the user inputs is in between 1 - 25
                    if 1 <= shifts <= 25:
                        print(f'message: {user_input}, shifting: {shifts}')
                        new_message = encryptions(user_input, shifts)
                        print(new_message)
                        break

                    #if the user got a number outside of 1 - 25
                    else:
                        print('Please enter a valid number')

                #if the error is just a normal fat finger
                except ValueError:
                    print('Please enter a valid number')

                #anything else happens
                except Exception as e:
                    print(f'Error occurred: {e}')
                    sys.exit(1)

        #we are decrpyting
        else:
            print(valid, "decryption")

    #if not manual then it return false
    return False

#returns the message when encrpted depending on the number of shifts
def encryptions(message: str, num_shifts: int):
    encrypted_message = ''

    #ensureing the shift is within a valid range (1 - 25)
    actual_shift = num_shifts % 26

    for char in message:
        #calculating the new postion
        if 'a' <= char <= 'z':
            #lower case char
            new_char_code = ((ord(char)) - ord('a') + actual_shift % 26) + ord('a')
            encrypted_message += chr(new_char_code)
        elif 'A' <= char <= 'z':
            #upper case char
            new_char_code = ((ord(char)) - ord('A') + actual_shift % 26) + ord('A')
            encrypted_message += chr(new_char_code)
        else:
            #nothing to add, because its not an alphabet char
            encrypted_message += char

    return encrypted_message

"""AI Code"""