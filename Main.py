#imports
import sys
from ciphers.caesar import *

#main
def main():
    # differnt vars
    option = '' #boolean, if m its mainal, otherwise its ai
    language = '' #selected cipher
    ciphers = ['Caesar Cipher', 'Morse Code', 'Atbash Cipher', 'ROT13 Cipher', 'Vigenere Cipher'] #list of all the ciphers that will be used
    encryption = True #if false, the user wants to decrypt

    #loop that will be used for selection
    while True:
        #seeing if the user selected the right number
        try:
            #selecting the right option for the user
            print('Which one will you like to do?')
            print('1. Manual Input\n'
                  '2. Ai\n'
                  '3. Exit')

            # var that will select the there option
            choice = int(input())

            #if the user slected 1, then the user can enerpt and decyept there own message
            if choice == 1:
                option = 'm'
                print('manial')
                language = list_options(ciphers)
                
                #asking the user what they want to do 
                while True:
                    #printing out the options
                    print('1. Encrypt\n'
                          '2. Decrypt')
                    choice = int(input('Please chose a valid option\n'))

                    #if they want to encrpt then it will stay true
                    if choice == 1:
                        encryption = True

                        #checking if the language the user selected
                        match language:
                            #if the language is a caeser cipher
                            case 'Caesar Cipher':
                                manual_ceaser(option, encryption)

                    #if the user wants to decrpt then it goes false
                    elif choice == 2:
                        encryption = False

                        #checking what langauge the user selceted
                        match language:
                            #if the language is a caeser cipher
                            case 'Caesar Cipher':
                                manual_ceaser(option, encryption)
                        
                    #just ask to enter a valid number
                    else:
                        print('please enter a valid number')

                    #just leaves the manual section
                    break

            #if user selected 2, its ai
            elif choice == 2:
                option = 'a'
                print('ai')
                language = list_options(ciphers)

                #seeing what langauge that user selected
                match language:
                    #if the user selected caeser cipher
                    case "Caesar Cipher":
                        ai_ceaser(option)

            #closes the program
            elif choice == 3:
                sys.exit(1)

            #else, no option was selcted
            else:
                print('Please select a valid option')

        #if the user selected the something that is not a number
        except ValueError:
            print('please enter a valid number')

        #if something else happend
        except Exception as e:
            print(f'Error occurred: {e}')
            break

#looping through a list and printing the list out
def looping_list(list):
    #to indcate the index
    index = 1

    #looping through the list and printing them
    for item in list:
        print(index, item)
        index += 1

#using the list to return a selected cipher
def list_options(list):
    #max value of the list
    max_value = len(list)

    while True:
        #using the list to be printed
        looping_list(list)

        #seeing the user enters a valid number
        try:
            #asking the user to choose a cipher
            choosen = int(input('Which cipher would you like to use?\n'))

            #if the selected option is a valid option, return the cipher that was chosen
            if 1 <= choosen <= max_value:
                #pretty print - 1 = index value
                return list[choosen - 1]

            #if its not a valid option, ask for a valid option
            else:
                print('Please enter a valid option')

        #if the user enters something that is not a number, asks the user to enter a valid number
        except ValueError:
            print('please enter a valid number')

        #if something else happens
        except Exception as e:
            print(f'Unexpected error: {e}')
            break


#main function call
if __name__ == "__main__":
    main()
