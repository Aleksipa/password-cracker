# Project definition

The aim of this project is to implement a program that enables a user to test the strength of the given passwords. The program repeatedly generates guesses that aim to match the passwords the user has given. After completion the program presents the execution times and number of guesses it took for the chosen algorithm to guess the password.

## Algorithms and data structrures

The program generates guesses using two different approaches. On of which is based on brute force algorithm and the other on Markov model-based method implemented with trie data structure.

## Input and output

The input consists of two parts. First one is a list of passwords (each password in its own line) or individual password, a user wants to evaluate. The second is a user given training file that needs to contain a list of real passwords (each password in its own line). Dictionaries won't work because passwords that occur often needs to be multiple times in the training file in order for markov chain to work properly. There are numerous leaked password files freely available on the internet. 

The output of the training is a .txt file containing a user defined number of password guesses (number of guesses can be configured at the config file). Guesses are based on the user given training file. Output of `bruteForce` and `markovChain` is the execution time and number of guesses it took for a chosen guessing algorithm to guess the given password(s). Please note that execution times grow exponentially as length of the password increases.

## Sources

* https://en.wikipedia.org/wiki/Password_cracking

* https://en.wikipedia.org/wiki/Markov_chain

* https://en.wikipedia.org/wiki/Trie