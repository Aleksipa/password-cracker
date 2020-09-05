
#!/usr/bin/env python3

import time
from collections import OrderedDict
from bforce.cartesian_product import cProduct

# Brute force class. Tries to guess the given password with brute force.
class bruteForce:

    def __init__(self, dict):
        self.name=dict['name']
        self.alphabet = dict['alphabet']

    def guess(self,password):
        attempts = 0
        for i in range(1, 9):
            for letter in cProduct(self.alphabet, repeat=i):
                attempts += 1
                letter = ''.join(letter)
                if letter == password:
                    return (attempts)