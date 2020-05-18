# course: DSC510
# assignment: 10.1
# date: 05/17/2020
# name: Arindam Samanta
'''
# description: this program uses an open API to obtain data for the end user
This program uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
The program receives a JSON response which includes various pieces of data. You should parse the JSON data to obtain the “value” key.
The data associated with the value key should be displayed for the user (i.e., the joke).
Your program should allow the user to request a Chuck Norris joke as many times as they would like.
You should make sure that your program does error checking at this point.
    If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user.
    There are other ways to handle this. Think about included string functions you might be able to call.
Your program must include a header as in previous weeks.
Your program must include a welcome message for the user.
Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”
'''

import requests
import json
import textwrap


def pretty_print(in_string):
    string_len = 80
    my_wrapper = textwrap.TextWrapper(drop_whitespace=True, width=string_len)
    lines = my_wrapper.wrap(text=in_string)
    print('=' * string_len)
    for line in lines:
        print(line)
    print('=' * string_len)


def main():
    print("Welcome to the Joke for smile program!")

    usr_response = input("Do you wish to read a Chuck Norris Joke? (answer: y/Y to read or any other key to quit) \n")
    while usr_response == 'y' or usr_response == 'Y':
        url_to_call = "https://api.chucknorris.io/jokes/random"
        url_response = requests.request("GET", url_to_call)
        if url_response.status_code == 200:
            output_json = json.loads(url_response.text)
            unformatted_string = output_json['value']
            print("Connection to server is successful! \n\n")
            print("Here is your joke.\n")
            pretty_print(unformatted_string)
        else:
            print("Connection Unsuccessful. Please try again after sometime.")
        usr_response = input(
            "Do you wish to read another Chuck Norris Joke? (answer: y/Y to read or any other key to quit) \n")


if __name__ == '__main__':
    main()
