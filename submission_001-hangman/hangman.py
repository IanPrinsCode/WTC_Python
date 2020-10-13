#TIP: use random.randint to get a random word from the list
import random
from random import choice


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    list_object = open(file_name)
    words = list_object.readlines()
    return words


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    random_word = words[random.randint(0, len(words)-1)]
    random_index = random.randint(0, len(random_word)-1)
    hidden_word = random_word.replace(random_word[random_index] , "_", 1)
    print("Guess the word: " + hidden_word)
    return [random_word]



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """ 
    return input("Guess the missing letter: ")


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)[0]
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

