import sys
import random
import time
from collections import OrderedDict

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

    def generate(self, nGrams, n, password):
        startTime = time.time()
        attempts = 0
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
        guess = ''.join(result)
        attempts += 1
        if guess == password:
            end = time.time()
            executionTime = end - startTime        
            return (attempts, executionTime)
  
