'''
At this point, we have written code to generate a random hand and display that
hand to the user. We can also ask the user for a word (Python's input) and
score the word (using your getWordScore). However, at this point we have not
written any code to verify that a word given by a player obeys the rules of the
game. A valid word is in the word list; and it is composed entirely of letters
from the current hand. Implement the isValidWord function.

'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if len(word) < 1:
        return False
    # check if all the characters in word are in the hand dictionary
    temp = getFrequencyDict(word)
    count = 0
    for j in temp.keys():
        if hand.get(j) == None:
            return False
        if temp.get(j) <= hand.get(j):
            count += 1
    if word in wordList and count == len(temp):
        return True
    else:
        return False

