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
    def build(self, words, n):
        ngrams = dict()
        if len(words) < n:
            return ngrams
        for i in range(len(words)-n):
            ngram = tuple(words[i:i+n])
            next_word = words[i+n]
            if ngram in ngrams:
                ngrams[ngram].append(next_word)
            else:
                ngrams[ngram] = [next_word]
        last_ngram = tuple(words[len(words)-n:])
        if last_ngram in ngrams:
            ngrams[last_ngram].append(None)
        else:
            ngrams[last_ngram] = [None]
        return ngrams

    # Generates a string guess based on given ngram dict
    def generate(self, nGrams, n):
        start = random.choice(list(nGrams.keys()))
        currentNgram = tuple(start)
        result = list(start)
        for i in range(10):
            if currentNgram in nGrams:
                possibilities = nGrams[currentNgram]
                next = random.choice(possibilities)
                if next is None: break
                result.append(next)
                currentNgram = tuple(result[-n:])
            else:
                break
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




  
