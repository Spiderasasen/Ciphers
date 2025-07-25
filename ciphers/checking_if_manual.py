def is_manual(valid):
    """
    Checking if its really manual section by the user
    """
    # if option says m, its manual
    if valid == 'm':
        return True
    #otherwise its ai
    return False