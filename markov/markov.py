import sys
import random
import time
from collections import OrderedDict

# Markov class. Tries to guess the given password with markov chain based ngrams.
class markov:

    def __init__(self, dict):
        self.name=dict['name']
        self.ngram_size = dict['ngram_size']
        self.number_of_guesses = dict['number_of_guesses']
        self.alphabet = dict['alphabet']

    
    # Creates a dict of ngrams based on given word list
    def build(self, wordList):
        ngrams = dict()
        for j in range(len(wordList)):
            word = wordList[j]
            if len(word) < self.ngram_size:
                return ngrams
            for i in range(len(word)-self.ngram_size):
                ngram = tuple(word[i:i+self.ngram_size])
                next_char = word[i+self.ngram_size]
                if ngram in ngrams:
                    ngrams[ngram].append(next_char)
                else:
                    ngrams[ngram] = [next_char]
            last_ngram = tuple(word[len(word)-self.ngram_size:])
            if last_ngram in ngrams:
                ngrams[last_ngram].append(None)
            else:
                ngrams[last_ngram] = [None]
        return ngrams

    # Generates a list of guesses based on given ngram dict
    def generate(self, nGrams):
        guesses = list()
        for j in range(self.number_of_guesses):
            beginning = random.choice(list(nGrams.keys()))
            currentNgram = tuple(beginning)
            guess = list(beginning)
            for i in range(10):
                if currentNgram in nGrams:
                    possibilities = nGrams[currentNgram]
                    next = random.choice(possibilities)
                    if next is None: break
                    guess.append(next)
                    currentNgram = tuple(guess[-self.ngram_size:])
                else: 
                    break
            if ''.join(guess) not in guesses:
                guesses.append(''.join(guess))
        return guesses
   

    # Tries to guess given password based on list of guesses
    def guess(self, password, guesses):
        start = time.time()
        attempts = 0
        for i in range(len(guesses)):
            attempts +=1
            if guesses[i] == password:
                end = time.time()
                executionTime = end - start
                return (attempts, executionTime)
        return (attempts, 0)




  
