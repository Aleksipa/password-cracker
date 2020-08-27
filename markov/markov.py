import sys
import random
import time
from collections import OrderedDict

# Markov class. Tries to guess the given password with markov chain based ngrams.
class markov:

    def __init__(self, dict):
        self.name=dict['name']
        self.alphabet = dict['alphabet']
        self.alphabet_len = len(self.alphabet)
        self.alphabet_dict = OrderedDict.fromkeys(self.alphabet)
        i = 0
        for char in self.alphabet_dict:
            self.alphabet_dict[char] = i
            i += 1
        self.alphabet_list = list(self.alphabet)
        self._index = 0
    
    # Creates a dict of ngrams based on given word list
    def build(self, wordList, n):
        ngrams = dict()
        for j in range(len(wordList)):
            word = wordList[j]
            if len(word) < n:
                return ngrams
            for i in range(len(word)-n):
                ngram = tuple(word[i:i+n])
                next_char = word[i+n]
                if ngram in ngrams:
                    ngrams[ngram].append(next_char)
                else:
                    ngrams[ngram] = [next_char]
            last_ngram = tuple(word[len(word)-n:])
            if last_ngram in ngrams:
                ngrams[last_ngram].append(None)
            else:
                ngrams[last_ngram] = [None]
        return ngrams

    # Generates a string guess based on given ngram dict
    def generate(self, nGrams, n):
        guesses = list()
        for j in range(10):
            beginning = random.choice(list(nGrams.keys()))
            currentNgram = tuple(beginning)
            guess = list(beginning)
            for i in range(10):
                if currentNgram in nGrams:
                    possibilities = nGrams[currentNgram]
                    next = random.choice(possibilities)
                    if next is None: break
                    guess.append(next)
                    currentNgram = tuple(guess[-n:])
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




  
