# password-cracker

In this project I will create a program that enables a user to test the strength of the given password. The program repeatedly generates guesses that aim to match the password the user has given. After completion the program compares solving methods by showing execution times and number of guesses of the different methods. This project uses python 3.

## Dokumentation

[Project definition](docs/project_definition.md)

## Weekly reports

[Week 1](docs/weekly-reports/week-1.md)

[Week 2](docs/weekly-reports/week-2.md)

[Week 3](docs/weekly-reports/week-3.md)

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

Configurations can be found under configs folder. Name of the input file and accepted characters can be configured in config.json file. 

## Input data and results

Input data file (currently configured to passwords.txt) must be in the input folder int .txt format and contain passwords that are written on separate lines. Results file is created automatically after the run.py script has been run.