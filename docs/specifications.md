# Data Structures and Algorithms Used

The goal is to implement and compare the execution of markov chain based trained algorithm to brute force algorithm in password guessing.

## Data Structures

- Lists
- Dicts
- Tuples

## Algorithms

- Brute-force search
- Markov chain

## Program Input

The program input consists of two user given list. One which contains the passwords that user want's to evaluate and the other that is used to train the markov model. The output of the training is a .txt file containing a user defined number of password guesses. Guesses are based on the user given training file. Output of `bruteForce` and `markovChain` is the execution time and number of guesses it took for a chosen guessing algorithm to guess the given password(s). This data is saved in to a .txt file. Please note that execution times grow exponentially as length of the password increases.

## Expected Time Complexities

| Algorithm                | Big-O (Worst-case performance) | Description                                                                                        |
| ------------------------ | ------------------------------ | -------------------------------------------------------------------------------------------------- |
| Brute-force search       | **L(log N/log 2)**             | Every possible password will be explored in the worst case.                                        |


where:
**|N|** is the number of possible symbols
**|L|** is the number of symbols in the password

## Sources

- https://en.wikipedia.org/wiki/Password_strength