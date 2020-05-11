# course: DSC510
# assignment: 8.1
# date: 05/03/2020
# name: Arindam Samanta
# description: This program will perform various functions to read file and count words and their occurances

# Importing library
import string


#
# This function add_word will add each word to the dictionary or increase the count
# Input: a word and a dictionary
# No Return value


def add_word(words, word_count_dict):
    if words not in word_count_dict:
        word_count_dict[words] = 1
    else:
        word_count_dict[words] += 1


#
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


# This function Pretty_print will format each line before printing
# Input: the dictionary
# No Return value


def pretty_print(word_count_dict):
    value_key_list= []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    print('{:15s}{:15s}'.format("Word", "Count"))
    print('-'*30)
    for val, key in value_key_list:
        print('{:15s} {:<3d}'.format(key,val))


# This is the main function.
# This will open the file and call Process_line.
# When finished it will call Pretty_print to print the dictionary
def main():
    # Intializing and empty word count dictionary
    word_count_dict = {}
    fname = "Gettysburg.txt"
    try:
        fhand = open(fname, 'r')
    except FileNotFoundError as fe:
        print(fe)
    # Read each line from the file into a variable
    for line in fhand:
        # Calling function to process each line
        process_line(line, word_count_dict)

    print("length of the dictionary :", len(word_count_dict))
    pretty_print(word_count_dict)

# Checking to see if the main function exists before calling

if __name__ == "__main__":
    main()
