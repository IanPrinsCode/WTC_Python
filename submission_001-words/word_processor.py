import string
from functools import reduce


def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


"""
This function receives a string of text as paramater.  The function splits up the string into
a list of words and returns that list.
"""
def convert_to_word_list(text):
    return list(filter(lambda word: word != "" , split([",", " ", "?", ";", "."], text.lower())))


"""
This function receives a string of text and an integer value as paramaters.  The function 
splits up the string into a list of words and returns only the words that are longer than the 
length parameter.
"""
def words_longer_than(length, text):
    return list(filter(lambda word: word != "" and len(word) > length , split([",", " ", "?", ";", "."], text.lower())))


"""
This function receives a string of text as paramater.  A list of words containing all the words
in the text is then mapped into a list containing only the values of the length of the words.
The function then iterates through this list, passing each unique value into the key of a new
dictionary, while also counting the number of occurences of each word size, and passing the sum
total into the corresponding dictionary value.
"""
def words_lengths_map(text):
    word_lengths = list(map(lambda x: len(x), convert_to_word_list(text)))
    return dict((x, word_lengths.count(x)) for x in set(word_lengths))


"""
This function returns a list containing all characters in the alphabet. 
"""
def get_alphabet_characters():
    return list(string.ascii_lowercase)


"""
This function receives a string of text as paramater.  It then iterates through the list of alphabetic
characters, returned by the get_alphabet_characters() function, and passes each letter into the key of
a new dictionary.  The function simultaneously checks in the text string for the amount of occurences
of each letter and passes the sum total into the corresponding value of the dictionary.
"""
def letters_count_map(text):
    return dict((char, text.lower().count(char)) for char in get_alphabet_characters())


"""
This function receives a string of text as paramater.  The reduce method is being used to iterate
through the dictionary, returned by the letters_count_map() funtion, and compares all values in this
dictionary to finally return the key of the letter with the highest amount of occurence. For empty text
this function will return 'None'.
"""
def most_used_character(text):
    if text == "":
        return None
    answer = reduce((lambda x, y: x if letters_count_map(text).get(x) > letters_count_map(text).get(y) else y), letters_count_map(text))
    return answer


if __name__ == "__main__":
    # text = 'These are indeed interesting, an obvious understatement, times. What say you?'
    text = "Adam said to Eve, cover yourself with leafs"


    print(convert_to_word_list(text))
    print(words_longer_than(5, text))
    print(words_lengths_map(text))
    print(letters_count_map(text))
    print(most_used_character(text))

