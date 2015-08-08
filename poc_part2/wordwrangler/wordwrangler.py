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

    #new_list = []

    #for word in list1:
    #    if word not in new_list:
    #        new_list.append(word)

    #return new_list

    # iterative version2
    # better version

    list2 = list(list1)
    new_counter = 0
    for old_counter in range(1, len(list2)):
        if list2[new_counter] != list2[old_counter]:
            list2[new_counter + 1] = list2[old_counter]
            new_counter += 1

    return list2[:new_counter+1]



def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """

    # iterative version1
    #new_list = []

    #for word in list1:
    #    if word in list2:
    #        new_list.append(word)

    #return new_list


    # iterative version2
    # more efficient
    new_list = []
    counter1 = 0
    counter2 = 0

    while counter1 < len(list1) and counter2 < len(list2):
        if list1[counter1] < list2[counter2]:
            counter1 += 1
        elif list1[counter1] > list2[counter2]:
            counter2 += 1
        else:
            new_list.append(list1[counter1])
            counter1 += 1

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
    if len(list1) < 2:
        return list1

    mid = len(list1)/2

    list_left = list1[:mid]
    list_right = list1[mid:]

    list_left = merge_sort(list_left)
    list_right = merge_sort(list_right)

    return merge(list_left, list_right)

# Function to generate all strings for the word wrangler game

def insert_x(my_string):
    """
    inserts x after every letter in my_string
    has got nothing to do with this program!
    """
    if len(my_string) < 2:
        return my_string
    else:
        return my_string[0] + 'x' + insert_x(my_string[1:])

def add_first_word(words, word_to_add):
    """
    returns all the combination of words in the given list of words
    after adding word_to_add at all possible places
    """
    result = []
    print 'words- ', words
    print 'word_to_add- ', word_to_add

    for word in words:

        for count in range(len(word) + 1):
            result.append(word[:count] + word_to_add + word[count:])

    return result

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    total_words = []

    if len(word) < 1:
        return [""]


    first_word = word[0]
    # words without first_word
    total_words += gen_all_strings(word[1:])

    # words with first_word
    total_words += add_first_word(total_words, first_word)

    return total_words

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """

    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)

    data = []
    #print data
    #print type(data)

    for line in netfile.readlines():
        data.append(line[:-1])

    #print data
    return data

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    print words
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

def test():
    """
    basic testing
    """

    #print remove_duplicates(['anurag', 'narayan', 'narayan', 'rahul', 'zebra', 'zebra'])
    #print intersect([1, 2, 3, 4, 5],[3, 4, 5, 6, 7])

    #print merge_sort(['l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])
    #print merge_sort(['z', 'a'])
    #print merge(['b', 'd', 'f', 'k', 'l'],['a', 'c'])
    #print
    #print add_first_word(['abcdef', 'ddddd', 'eeee'], 'x')
    print gen_all_strings('abc')
    print
    print gen_all_strings('a')
    print
    print gen_all_strings('')
# Uncomment when you are ready to try the game
#run()

#test()



