# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:07:15 2022

@author: Prachi
"""
import sys
import pathlib 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from random import seed
from random import randint


def getfile(filepath):
    #get the file data from txt file
    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as f:
        text = f.read()
    return text

def preprocess(tokenized):
    #preprocessing function
    #lowercase all tokens, check that they are alphabetical, their length
    #greater than 5 and that the token is not a stopword
    tokens = [t.lower() for t in tokenized]
    tokens = [tok for tok in tokens if tok.isalpha() == True and
              len(tok) >5 and
              tok not in stopwords.words('english')]
    
    #lemmatize the processed tokens using list comprehension and get the unique lemmas
    wnl = WordNetLemmatizer()
    lemmatized = [wnl.lemmatize(tok) for tok in tokens]
    uniquelem = set(lemmatized)
    
    #do part of speech tagging on the unique lemmas and print the first 20
    tagged = nltk.pos_tag(uniquelem)
    print("First 20 unique tagged items: " + str(tagged[:20]))
    
    #get only the tagged lemmas that are nouns
    nouns = [val[0] for val in tagged if val[1] == 'NN']
    
    #print number of tokens and number of nouns
    print("\n Number of tokens :" + str(len(tokens)))
    print("\n Number of nouns :" + str(len(nouns)))
    
    #return both the tokens and nouns lists
    return tokens, nouns

if __name__ == '__main__':
    #check that data was entered as system argument, if not enter error message 
    #and stop process, otherwise continue
    if (len(sys.argv) < 2):
        print('Please input a filename as a system arg')
    else:
        #get file path and use filepath to get file
        fp = sys.argv[1]
        file = getfile(fp)
        
        #tokenize the words and get the set of unique tokens
        tokens = word_tokenize(file)
        settok = set(tokens)
        
        #print the Lexical Diversity
        print("Lexical Diversity %.2f" % (len(settok) / len(tokens)))
        
        #preprocess the tokens and get the preprocessed tokens and nouns
        token, nouns = preprocess(tokens)
        
        #create dictionary of the nouns and the number of times a particular
        #noun appears in the tokens list
        dictionary = {}
        for i in range(0,len(nouns)):
            noun = nouns[i]
            dictionary[noun] = token.count(noun)
        
        #create an empty dictionary and get keys in descending order of the sorted dictionary
        sortedDict = {}
        sortedKeys = sorted(dictionary, key=dictionary.get, reverse = True)
        
        #use the empty dictionary called sortedDict to rearrange the sorted keys 
        #to form the sorted Dictionary
        for key in sortedKeys:
            sortedDict[key] = dictionary[key]
        
        #print the top 50 items in the sorted dictionary
        dictItems = sortedDict.items()
        print(list(dictItems)[:50])
        
        #create the list of the top fifty words to use in the guessing game
        words = [val[0] for val in list(dictItems)[:50]]
        
        
        #Start of Guessing game
        #create points counter which starts at five, an input variable which will 
        #keep track of the inputs to make sure to end the game when necessary,
        #and set the seed
        points = 5
        inpt = ""
        seed(123)
        
        #guessing game code
        print("Let's play a word guessing game!")
        
        #check that the user doesn't want to end the game with '!' and that
        #their points aren't in the negatives
        while points >= 0 and inpt != "!":
            #get a random index and use the index to select the corresponding word
            #in the words list
            ind = randint(0,49)
            word = words[ind]
            
            #create boolean variable guessed to check whether word was guessed
            #and create variable guess with _ corresponding to every letter 
            #in the word that needs to be guessed
            guessed = False
            guess = '_ ' * len(word)
            
            #print guess before starting turn and ask user to guess a letter for the input
            print(guess)
            inp = input("Guess a letter:")
            
            #check that the user hasn't guessed the word and make sure input is not "!"
            while guessed == False and inp != "!":
                #if the input is found in the word then change the guess "_" to the 
                #letter inputted where necessary and add 1 point to the total score
                #Display the total points after
                if inp in word:
                    for i in range(0, len(word)):
                        if word[i] == inp:
                            j = i*2
                            guess = guess[0:j] + inp + guess[j+1:]
               
                    points += 1
                    print("Right! Score is " + str(points))
                #if input is not in the words then remove point. If the points are now 
                #in the negative then end game and print fail statement, otherwise
                #ask user to guess again and display current score
                else:
                    points -= 1
                    if points < 0:
                        print("Sorry you failed the game!")
                        break
                    else:
                        print("Sorry, guess again. Score is " + str(points))
                #check that "_" not in guess to check whether the word has been guessed
                #if word has been guessed, print the word, that the user solved it, the
                #current score, and to guess another word. Make the boolean guessed = True
                #so that game will generate another word to guess
                if '_' not in guess:
                    print(guess)
                    print("You solved it!")
                    print("\nCurrent score is " + str(points))
                    print("\nGuess another word")
                    guessed = True
                    break
                #print the guess and ask user for input to guess next letter in word/exit game
                print(guess)
                inp = input("Guess a letter:")
                #make the outside inpt variable = inp, so that game can be exited if user
                #enters "!" as the input
                inpt = inp
            
                
            
        