"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """

    # iterative version1
    new_list = []

    for word in list1:
        if word not in new_list:
            new_list.append(word)

    return new_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    # iterative version1
    new_list = []

    for word in list1:
        if word in list2:
            new_list.append(word)

    return new_list

# Functions to perform merge sort

def merge(list1, list2):
   """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    merged_list = []

    counter1 = 0
    counter2 = 0

    # traverse over both the list and insert the shorter element first
    while counter1 < len(list1) and counter2 < len(list2):
        if list1[counter1] < list2[counter2]:
            merged_list.append(list1[counter1])
            counter1 += 1
        elif list1[counter1] > list2[counter2]:
            merged_list.append(list2[counter2])
            counter2 += 1
        else:
            merged_list.append(list1[counter1])
            counter1 += 1

    # account for premature termination of above loop
    for counter in range(counter1, len(list1)):
        merged_list.append(list1[counter])

    for counter in range(counter2, len(list2)):
        merged_list.append(list2[counter])

    return merged_list

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    # return if list is empty or contains only one element
    if len(list1) < 2:
        return list1

    mid = len(list1)/2

    # split into two halves
    list_left = list1[:mid]
    list_right = list1[mid:]

    # merge individual lists
    list_left = merge_sort(list_left)
    list_right = merge_sort(list_right)

    return merge(list_left, list_right)


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return []

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()



