# password-cracker

In this project I will create a program that enables a user to test the strength of the given password or multiple passwords. The program repeatedly generates guesses that aim to match the password(s) the user has given in a .txt file. After completion the program writes execution times and number of guesses it took to guess the given password(s). This project uses python 3.

## Documentation

- [Project definition](docs/project_definition.md)

- [Testing](docs/testing.md)

- [Project specifications](docs/specifications.md)

- [User guide](docs/user_guide.md)

## Installation

Requires Python 3

Create a virtual environment

`$ python3 -m venv venv`

Activate the virtual environment

`source venv/bin/activate`

Clone the repo

`git clone https://github.com/Aleksipa/password-cracker.git`


## Configurations

Configurations can be found under configs folder. Name of the input file, lenght of ngrams (currently set to 3), accepted characters and number of guesses the program generates from the input file can be configured in config.json file. 

## Input data and results

Input data files (currently configured to passwords.txt and training.txt) must be in the input folder in .txt format and must contain passwords that are written on separate lines. Training results and password guessing result files are created automatically after the scripts has been executed.

Required input files:

 `input/passwords.txt`

 `input/training.txt`


## Available Scripts

This program consists of three separeate program modules: `train`, `markovChain` and `bruteForce`. `train` generates training result file, that consists of password guesses. Guesses are based on n-gram probabilities of user given training file. Based on the result file `markovChain` tries each generated guess against user given password(s). `bruteForce` generates every possible guess and tries the guesses against user given password(s).

In order to guess the password(s) using brute force algorithm run the following:

`python3 bruteForce.py`

To create passwords based on markov's chain run the following:

`python3 train.py`

In order to test whether the password guesses generated by markov chain match the password(s) in the input folder, run the following:

`python3 markovChain`
