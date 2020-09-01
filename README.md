# password-cracker

In this project I will create a program that enables a user to test the strength of the given password or multiple passwords. The program repeatedly generates guesses that aim to match the password(s) the user has given in a .txt file. After completion the program writes execution times and number of guesses it took to guess the given password(s). This project uses python 3.

## Dokumentation

[Project definition](docs/project_definition.md)

## Weekly reports

[Week 1](docs/weekly-reports/week-1.md)

[Week 2](docs/weekly-reports/week-2.md)

[Week 3](docs/weekly-reports/week-3.md)

[Week 4](docs/weekly-reports/week-4.md)

[Week 5](docs/weekly-reports/week-5.md)

[Week 6](docs/weekly-reports/week-6.md)

## Test coverage

[Coverage report](docs/coverage-report.png)

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

Input data files (currently configured to passwords.txt and training.txt) must be in the input folder in .txt format and must contain passwords that are written on separate lines. Training results and password guessing result files are created automatically after the scripts has been executed. Please note that execution times grow exponentially as password lengths increase.

## User guide

This program consists of three separeate program modules: `train`, `markovChain` and `bruteForce`. `train` generates training result file, that consists of password guesses. Guesses are based on n-gram probabilities of user given training file. Based on the result file `markovChain` tries each generated guess against user given password(s). `bruteForce` generates every possible guess and tries the guesses against user given password(s).