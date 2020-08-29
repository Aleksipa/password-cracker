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

The program input consists of two user given list. One which contains the passwords that user want's to evaluate and the other that is used to train the markov model. The output is the execution times and number of guesses it takes for a brute force password guesser and trainded Markov model-based password guesser to guess the given password.

## Expected Time Complexities

| Algorithm                | Big-O (Worst-case performance) | Description                                                                                        |
| ------------------------ | ------------------------------ | -------------------------------------------------------------------------------------------------- |
| Brute-force search       | **L(log N/log 2)**             | Every possible password will be explored in the worst case.                                        |


where:
**|N|** is the number of possible symbols
**|L|** is the number of symbols in the password



https://en.wikipedia.org/wiki/Password_strength