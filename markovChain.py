#!/usr/bin/env python3

'''This script loads the passwords from input folders passwords.txt files and then checks if password from training results 
matches the input folders password.'''

# imports
import time
import os
import sys
from bforce.brute_force import bruteForce
from markov.markov import markov
from configs.configure import Configure

# loads input files and tests if training results match the passwords in input folder.
def runMarkov():

    # Checks if password from training results matches the input folders password.
    try:
        fo = open("results/"+CONFIG.PASSWORDS_FILE.rstrip('.txt')+"_guessing_result.txt", "w")
        with open("input/"+CONFIG.PASSWORDS_FILE, 'r') as inputfile, open("results/"+CONFIG.TRAINING_RESULT_FILE, 'r') as guessesfile:
            if os.stat("input/"+CONFIG.PASSWORDS_FILE).st_size != 0 | os.stat("results/"+CONFIG.TRAINING_RESULT_FILE).st_size != 0:
                for line in inputfile:
                    attempts = 0
                    line = line.rstrip('\r\n')
                    for guess in guessesfile:
                        start = time.time()
                        attempts += 1
                        guess = guess.rstrip('\r\n')
                        if guess == line:
                            end = time.time()
                            executionTime = end - start
                            # Write results to file
                            fo.write("{}\n".format("Password to guess: " + line + ". Algorithm: Markov chain. " + str(attempts) + " tries and " + str(executionTime) + " seconds."))
                    fo.write("{}\n".format("Markov chain based algorithm wasn't able to guess the password."))
                    fo.flush()
                fo.close()
            else:
                print("Passwords file or training results file is empty! Please add at least one password and make sure you have run the training program, exiting", file=sys.stderr)
                sys.exit(1)                
    except Exception as e:
        sys.stderr.write("\x1b[1;%dm" % (31) + "Error: {}\n".format(e) + "\x1b[0m")
        sys.exit(1)

def main():
    try:
        global CONFIG
        CONFIG = Configure({"name":"My Config"})
        runMarkov()
    except Exception as e:
        sys.stderr.write("\x1b[1;%dm" % (31) + "Error: {}\n".format(e) + "\x1b[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()