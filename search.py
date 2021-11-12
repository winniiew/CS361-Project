# CS361 Assignment 5: MVP Microservices
# Author: Elaine Zamora
# Date: 10/27/2021


import sys
import argparse
import json
import requests
import wikipedia

url = "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search="

# ------------------------
def join_words(words):
    """ This takes list of words entered by the user and reformats it 
        separated by "_" where wordX is a word entered and X is the Xith
        word in the list: word1_word2_word3
    """
    search_q = "_".join(words)
    return search_q


def display_info(words):
    """
        Takes as input a query and writes result to a text file named search_result.txt
        Uses Wikipedia to search and return a summary of text related to search query
        """
    # join query words separated by underscore to append to url
    query_name = join_words(words)

    # search wikipedia, parse data, and write summary to search_result.txt
    summary = wikipedia.summary(query_name)
    #print(summary)
    r_dict = {'name':query_name, 'summary':summary}

    with open("search_result.txt", "w") as outfile:
        json.dump(r_dict, outfile)


if __name__ == "__main__":
    # Note: The following can be utilized via CLI with search terms 
    # immediately after the filename separated by spaces
    arg = sys.argv
    display_info(arg[1:])
    
    # Note: You can use the following to simply call the function with search terms as args
    #     : user query must be entered with spaces between terms
    # user_query = 'Nelson Mandela'
    # display_info(user_query)
