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
    
    # Creates a dict of ngrams based on given word
    def build(self, word, n):
        ngrams = dict()
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
        firstLetters = random.choice(list(nGrams.keys()))
        currentNgram = tuple(firstLetters)
        result = list(firstLetters)
        if currentNgram in nGrams:
            possibilities = nGrams[currentNgram]
            next = random.choice(possibilities)
            result.append(next)
            currentNgram = tuple(result[-n:])
        else:
            return ''.join(result)

    # Tries to guess given password based on guesses list
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




  
