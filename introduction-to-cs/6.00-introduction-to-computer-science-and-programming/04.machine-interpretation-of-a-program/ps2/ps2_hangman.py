# 6.00 Problem Set 3
# 
# Hangman
# Name: Eloi Gil
# Collaborators:
# Time Spent: 2h


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def game (gameWord, guesses):
    print("Welcome to the game, Hangman!")
    availableLetters = list("abcdefghijklmnopqrstuvwxyz")
    word = gameWord
    wordTuple = tuple(word)
    hangList = []
    guessesLeft = guesses

    for letter in wordTuple:
        hangList.append('_')

    #print(wordTuple)

    print("I am thinking of a word that is ", len(word), " letters long.")

    while (guessesLeft > 0 and hangList.count('_') > 0):
        print("-------------------")
        print("You have ", guessesLeft, " guesses left.")
        print("Available letters: ", ''.join(availableLetters))
        print(''.join(hangList))
        print("Please guess a letter:")
        letter = input()
        if wordTuple.count(letter) > 0:
            i = 0
            for char in wordTuple:
                if letter == char:
                    hangList[i] = letter
                i += 1
        else:
            guessesLeft -= 1
        availableLetters.remove(letter)

    if hangList.count('_') == 0:
        print("You won!")
    else:
        print("You loose!")
game (choose_word(wordlist), 8)
