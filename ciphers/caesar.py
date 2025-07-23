"""
    if the option is false, its maunal
        if encrpytion is true its encption otherwise its decryption
"""
import sys
import math

#approximate english letter frequencies
ENGLISH_FREQ_PERCENTAGES = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, # A - G
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, # H - N
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, # O - U
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074 # V - Z
]

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
            user_input = input('What is the encrypted message?\n')
            decryptions(user_input)

    #if not manual then it return false
    return False

#returns the message when encrpted depending on the number of shifts
def encryptions(message: str, num_shifts: int) -> str:
    encrypted_message = ''

    #ensureing the shift is within a valid range (1 - 25)
    actual_shift = num_shifts % 26

    for char in message:
        #calculating the new postion
        if 'a' <= char <= 'z':
            #lower case char
            new_char_code = ((ord(char) - ord('a') + actual_shift) % 26) + ord('a')
            encrypted_message += chr(new_char_code)
        elif 'A' <= char <= 'z':
            #upper case char
            new_char_code = ((ord(char) - ord('A') + actual_shift) % 26) + ord('A')
            encrypted_message += chr(new_char_code)
        else:
            #nothing to add, because its not an alphabet char
            encrypted_message += char

    return encrypted_message

def get_observed_frequencies(text: str) -> tuple[list[int], int]:
    """
    Calculates the observed counts of each letter in a given text

    args:
        text (str): the text to analyze

    returns:
        tuple[list[list],int]: a tuple containing:
            - a list of 26 integers, where each element is the count of a letter
            - the total number of alphabetic characters found in the text
    """
    observed_counts = [0] * 26 #initialize counts for a-z
    total_letters = 0
    for char in text:
        char_upper = char.upper() #convert to uppercase for consistent counting
        if 'A' <= char_upper <= 'Z':
            index = ord(char_upper) - ord('A') #get 0-based index
            observed_counts[index] += 1
            total_letters += 1
    return observed_counts, total_letters

def calculate_chi_squared(observed_counts: list[int], total_letters: int) -> float:
    """
    calculates the chi-squared score comparing ovserved letter frequencies
    to expected english letter frequencies. lower scores indicare a better match.

    args:
        observed_counts (list[int]): A list of 26 letter counts from the text.
        total_letters (int): the total number of alaphabetic characters in the text

    return:
        float: the chi-squared score. returns float('inf') if total_letters is 0
            to indicate an impossible match
    """
    if total_letters == 0:
        return float('inf') #cannot calculate chi-squared for empty text of no letters

    chi_squared = 0.0
    for i in range(26): #iterate through each letter of alphabet
        expected_count = ENGLISH_FREQ_PERCENTAGES[i] * total_letters
        observed_count = observed_counts[i]

        #avoiding division by 0,
        #if expected_count is 0 or smaller than zero
        if expected_count > 0:
            chi_squared += ((observed_count - expected_count) ** 2) / expected_count
        elif observed_count > 0:
            #if a letter is observed but not expexted at all, its a strong mismatch
            chi_squared += (observed_count ** 2) / 0.0000001 #using a tiny divisor for a large penalty

    return chi_squared

def decryptions(message : str, num_top_results: int = 5):
    #used to hold the message
    message_holder = ''
    #attempts to decypt s Caeser cipher without knowing the shift.
    #it tires all 26 possibal shifts and prints the result for each
    print(f'Ciphertext: {message}\n')

    best_shift = -1
    min_chi_squared = float('inf') #initialize with positive infinity to find the minimum
    best_decrypted_text = ''

    decryption_candidates = [] #stores tuples

    for shift_attempt in range(26): #shifts from 0 to 26
        #to decrypt with a positive shift_attempt, we apply a negative shift
        decypted_text = encryptions(message, -shift_attempt)

        #calculate the letter frequencies of the decrypted candidate text
        observed_counts, total_letters = get_observed_frequencies(decypted_text)

        #calulate the letter frequencies of the decrypted candidate text
        chi_squared_score = calculate_chi_squared(observed_counts, total_letters)

        decryption_candidates.append((chi_squared_score, shift_attempt, decypted_text))

    #sort the candidates by their chi-squared (lowest score is best)
    decryption_candidates.sort(key=lambda x: x[0])

    #print the top N results
    print(f'Top {num_top_results} most likely decryptions:')
    print("-" * 50)
    if not decryption_candidates:
        print('No candidates to analyze')
    else:
        for i, (score, shift, text) in enumerate(decryption_candidates[:num_top_results]):
            #check if the score is not infinity (meaninf there were letters to analyze)
            if score == float('inf'):
                print(f"{i + 1}. Shift: N/A | Chi-Sq: N/A | Message '{text}' (No alphabetic characters for analysis)")
            else:
                print(f"{i + 1}. Shift: {shift:2d} | Chi-Sq: {score:.2f} | Message '{text}'")
    print("-" * 50)

    #adding a note if the message is short
    if len(message) < 20 and decryption_candidates[0][0] != float('inf'):
        print('\nNote: For every short message, frequency analysis may not always')
        print('predict the correct shift as the top result. Check other top candidates.')

"""AI Code"""