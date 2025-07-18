"""
    if the option is false, its maunal
        if encrpytion is true its encption otherwise its decryption
"""
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
            print(valid, "encryption")

        #we are decrpyting
        else:
            print(valid, "decryption")

    #if not manual then it return false
    return False

"""AI Code"""