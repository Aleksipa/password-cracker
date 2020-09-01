import itertools
import time
from collections import OrderedDict
from bforce.cartesian_product import cProduct

# Brute force class. Tries to guess the given password with brute force.
class bruteForce:

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

    def guess(self,password):
        attempts = 0
        for i in range(1, 9):
            for letter in cProduct(self.alphabet_list, repeat=i):
                attempts += 1
                letter = ''.join(letter)
                if letter == password:
                    return (attempts)



