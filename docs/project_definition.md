# Project definition

The aim of this project is to implement a program that enables a user to test the strength of the given passwords. The program repeatedly generates guesses that aim to match the passwords the user has given. After completion the program compares solving methods by showing execution times and number of guesses of the different methods.

## Algorithms and data structrures

The program generates guesses using two different approaches. On of which is based on brute force algorithm and the other on Markov model-based method implemented with trie data structure.

## Input and output

The input consists of two parts. First one is a list of passwords (each password in its own line) or individual password, a user wants to evaluate. The second is a user given training file that needs to contain a list of real passwords (each password in its own line). Dictionaries won't work because passwords that occur often needs to be multiple times in the training file in order for markov chain to work properly. There are numerous leaked password files freely available on the internet. 

The output is the execution times and number of guesses it takes for a brute force password guesser and trainded Markov model-based password guesser to guess the given password. Please note that execution times grow exponentially as length of the password increases.

## Sources

* https://en.wikipedia.org/wiki/Password_cracking

* https://en.wikipedia.org/wiki/Markov_chain

* https://en.wikipedia.org/wiki/Trie