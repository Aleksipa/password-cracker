import itertools
import time

# Brute force function
def bruteForce(password):
    allowedChars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    start = time.time()
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(allowedChars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            if letter == password:
                end = time.time()
                executionTime = end - start
                return (attempts, executionTime)


