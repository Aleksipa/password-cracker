# User guide

This password guessing program consists of three separeate program modules: `train`, `markovChain` and `bruteForce`. `train` generates training result file, that consists of password guesses. Guesses are based on n-gram probabilities of user given training file. Based on the result file `markovChain` tries each generated guess against user given password(s). `bruteForce` generates every possible guess and tries the guesses against user given password(s).

## How to install the program

Requires Python 3

Create a virtual environment

`$ python3 -m venv venv`

Activate the virtual environment

`source venv/bin/activate`

Clone the repo

`git clone https://github.com/Aleksipa/password-cracker.git`

## How to execute the program

There are of two different approaches to guess passwords with this program: brute force and markov chain based methods. After the program has been installed, passwords that a user want's to evalueate needs to be placed into input folders passwords.txt file (each password must be in it's own line). After that brute force guessing can be executed by running:

`python bruteForce.py`

This creates a password_guessing_result.txt file to results folder, which contains number of guesses and time it took to guess for every password that was found on the input folders passwords.txt file.

In order to use markov chain based method the model must be trained first. Training file needs to be placed into input folder and it needs to be a .txt file containing real passwords (each passoword must be in it's own line). Currently the name of the training file is set to training.txt but this can be renamed in the configs. After the training file contains passwords the training can be executed by runnning:

`python train.py`

This creates a training_results.txt file into result folder. After this file has been generated, it is possible to check the results of the markov chain based generator against the input folders password.txt file. This can be done by executing:

`python markovChain.py`

This creates a password_guessing_result.txt file to results folder, which contains number of guesses and time it took to guess for every password that was found on the input folders passwords.txt file. In case the password wasn't found on generated guesses the program prints a statement about that.