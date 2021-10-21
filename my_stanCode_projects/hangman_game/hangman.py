"""
File: hangman.py
Name: Daniel Lu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 10


def main():
    """
    call the hangman function
    """
    hangman()


def hangman():
    """
    step 1: initialization, show the dashed
    step 2: while loop to
    """
    ans = random_word()                 # random word initialization
    left = N_TURNS                      # guesses left initialization
    recorder = ""                       # recorder initialization
    dashed = dasher(recorder, ans)      # dash the random word

    print("The word looks like " + dashed)      # required print out

    while True:
        input_ch = str(input("You have " + str(left) + " guesses left.\nYour guess: "))     # first get char
        while not input_ch.isalpha() or len(input_ch) != 1:             # keep get char until get legal format
            input_ch = str(input("illegal format.\nYour guess: "))

        if input_ch.upper() not in ans:                                 # wrong guess
            left -= 1                                                   # guesses left minus one
            print("There is no " + input_ch.upper() + "'s in the word.")    # required print out
        else:                                                           # correct guess
            recorder += input_ch.upper()                                # record it
            print("You are correct!")                                   # required print out

        dashed = dasher(recorder, ans)                                  # dashed updated
        if '-' not in dashed:                                           # which means word has been figured out
            print("You win!!\nThe word was " + ans)                     # required print out
            break                                                       # loop terminated
        elif left == 0:                                                 # no guess left
            print("You are completely hung : (\nThe word was: " + ans)  # required print out
            break                                                       # loop terminated
        else:
            print("The word looks like " + dashed)                      # loop continue, required print out


def dasher(ch, string):
    """
    This function will dash characters which user yet figure out.
    By comparing random word to every single character in string ch.
    """
    result = ""                     # initialize the string result
    for i in range(len(string)):    # compare character in random word from the first to the last one
        j = ch.find(string[i])      # method find will return the location if exist
        if j != -1:                 # string[i] is in the string ch which means user had already guessed
            result += ch[j]         # make it visible in result
        else:                       # j == -1 means it's not yet been found
            result += '-'           # keep it dashed in result
    return result                   # return the string result


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
