import sys
import random
import time
import numpy as np

# Markov class. Tries to guess the given password with markov chain based ngrams.
class markov:

    def __init__(self, dict):
        self.name=dict['name']
        self.ngram_size = dict['ngram_size']
        self.max_number_of_guesses = dict['max_number_of_guesses']
        self.alphabet = dict['alphabet']

    # Creates a dict of ngrams based on given word list
    def buildNgrams(self, wordList):
        ip_counter = 0
        ngrams = {}
        for j in range(len(wordList)):
            word = wordList[j]
            if len(word) >= self.ngram_size:
                for i in range(len(word) - self.ngram_size+1):
                    ngram = word[i:i+self.ngram_size]
                    if ngram not in ngrams:
                        ngrams[ngram] = {
                            'ip_count':0,
                            'cp_counter':0,
                            'next_letter':{},
                        }
                    if i == 0:
                        ngrams[ngram]['ip_count'] += 1
                        ip_counter += 1
                    if i != len(word) - (self.ngram_size):
                        end_char = word[i+self.ngram_size]
                        if end_char not in ngrams[ngram]['next_letter']:
                            ngrams[ngram]['next_letter'][end_char] = 1
                            ngrams[ngram]['cp_counter'] += 1    
                        else:
                            ngrams[ngram]['next_letter'][end_char] += 1
                            ngrams[ngram]['cp_counter'] += 1
                    else:
                        if None not in ngrams[ngram]['next_letter']:
                            ngrams[ngram]['next_letter'][None] = 1
                            ngrams[ngram]['cp_counter'] += 1
                        else:
                            ngrams[ngram]['next_letter'][None] += 1
                            ngrams[ngram]['cp_counter'] += 1
        return ngrams

    # Generates a list of guesses based on given ngram dict
    def generateGuesses(self, nGrams):
        guesses = list()
        beginnings = []
        beginning_prob = []
        for k in nGrams:
            ip_counts = nGrams[k]['ip_count']    
            if ip_counts > 0:
                beginnings.append(k)
                beginning_prob.append(ip_counts)
        numOccurancesIp = sum(beginning_prob)        
        beginning_probs = probs = [y / numOccurancesIp for y in beginning_prob]
        for j in range(self.max_number_of_guesses):    
            beginning = np.random.choice(beginnings, p=beginning_probs)
            currentNgram = beginning
            guess = list(beginning)
            for i in range(10):
                if currentNgram in nGrams.keys():
                    initValues = list(nGrams[currentNgram]['next_letter'].values())
                    numOccurances = sum(initValues)
                    probs = [x / numOccurances for x in initValues]
                    characters = list(nGrams[currentNgram]['next_letter'].keys())    
                    next = np.random.choice(characters, p=probs)
                    if next is None: break
                    guess.append(next)
                    currentNgram = (''.join(guess)[-self.ngram_size:])
                else: 
                    break
            if ''.join(guess) not in guesses:
                guesses.append(''.join(guess))
        return guesses   

  
