# making boolean options
option = False #if false its mainal
language = ''

#loop that will be used for selection
while True:
    #selecting the right option for the user
    print('Which one will you like to do?')
    print('1. User\n'
          '2. Ai')

    # var that will select the there option
    choice = int(input())

    #if the user slected 1, then the user can enerpt and decyept there own message
    if choice == 1:
        option = False
        print('manial')
        break

    #if user selected 2, its ai
    elif choice == 2:
        option == True
        print('ai')
        break

    #else, no option was selcted
    else:
        print('Please select a valid option')
