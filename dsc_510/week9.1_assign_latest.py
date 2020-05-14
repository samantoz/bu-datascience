# course: DSC510
# assignment: 9.1
# date: 05/10/2020
# name: Arindam Samanta

'''
# description: This program will perform various functions to read file and count words and their occurances
# and writing back the output to a file
'''


# Importing library
import string
import os

# This function process_line will process each line and split out the words
# Input: a line and a dictionary.
# calls the add_word() function for each word
# No Return value


def process_line(line, word_count_dict):
    # stripping the line of the end of line characters and white spaces
    line = line.strip()

    # splitting the words from the line
    word_list = line.split()
    # print(word_list)

    # verifying each word from the line for inconsistency and punctuations
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            # Call the add_word function in order to add each word to the dictionary
            add_word(word, word_count_dict)

#
# This function add_word will add each word to the dictionary or increase the count
# Input: a word and a dictionary
# No Return value


def add_word(words, word_count_dict):
    if words not in word_count_dict:
        word_count_dict[words] = 1
    else:
        word_count_dict[words] += 1

# This function will open a file
# write the contents in the file
# close the file


def process_file(out_filename, word_count_dict):
    if os.path.isfile(out_filename):  # check if file exists
        # print('File Exists so writing to the same file.', out_filename)
        with open(out_filename, 'a') as fh:  # open file for append/ writing
            fh.write('{:15s}{:15s}'.format("Word", "Count") + '\n')
            fh.write('-'*30 + '\n')
            value_key_list= []
            for key, val in word_count_dict.items():
                value_key_list.append((val, key))
            value_key_list.sort(reverse=True)
            for val, key in value_key_list:
                fh.write('{:15s} {:<3d}'.format(key,val) + '\n')
        fh.close()
    else:
        print('File Does Not Exists!', out_filename)

# This is the main function.
# This will open the file and call Process_line.
# When finished it will call Pretty_print to print the dictionary


def main():
    # Initializing and empty word count dictionary
    word_count_dict = {}
    read_filename = "Gettysburg.txt"
    try:
        # Check if the file exists and open it to assign the file pointer to a file handler
        rf = open(read_filename, 'r')
    except FileNotFoundError as fe:
        print(fe)
    except Exception as e: # This is to catch other exceptions
        print(e)
    else:
        # Get the filename from the user input in order to write the output
        # Then read each line from the read file
        for line in rf:
            # Calling function to process each line
            process_line(line, word_count_dict)

        out_filename = input("Please enter a file name to write the report: ")
        if os.path.isfile(out_filename):  # Check if file exists
            print("File Already Exists. Use another name.", out_filename)
        else:
            l = str(len(word_count_dict))  # Reading the total word count from the dictionary
            with open(out_filename, 'w') as fhand:  # Open the new file to write the word count
                fhand.write("length of the dictionary :" + " " + l + "\n")
                fhand.write("="*30 + "\n")

            # Call function process_file to write the details
            process_file(out_filename, word_count_dict)

# Checking to see if the main function exists before calling


if __name__ == "__main__":
    main()
