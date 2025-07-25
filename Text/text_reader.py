#setting the code in its own list
def reading_text(file_path):
    try:
        with open(file_path, 'r') as file:
            #reads all the lines in the text file and will return the list
            lines = file.readlines()
            return lines

    #if the file is not correct or not found
    except FileNotFoundError:
        print('File not found')
        return None

    #if anything else happens wrong
    except Exception as e:
        print(f'Error Detected: {e}')
        return None