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
    print("--Starting to compare guesses from training results to input password(s)-- ", file=sys.stderr)
    try:
        fo = open("results/"+CONFIG.PASSWORDS_FILE.rstrip('.txt')+"_guessing_result.txt", "w")
        with open("input/"+CONFIG.PASSWORDS_FILE, 'r') as inputfile:
            if os.stat("input/"+CONFIG.PASSWORDS_FILE).st_size != 0:
                for line in inputfile:
                        start = time.time()
                        line = line.rstrip('\r\n')
                        attempts = guess(line)
                        end = time.time()
                        executionTime = end - start
                        # Write results to file
                        if attempts != -1:
                            fo.write("{}\n".format("Password to guess: " + line + ". Algorithm: Markov chain. " + str(attempts) + " tries and " + str(executionTime) + " seconds."))                    
                        else:
                            fo.write("{}\n".format("Password to guess: " + line + ". Markov chain based algorithm wasn't able to guess the password."))
                fo.flush()
                fo.close()
            else:
                print("Passwords file or training results file is empty! Please add at least one password and make sure you have run the training program, exiting", file=sys.stderr)
                sys.exit(1)                
    except Exception as e:
        sys.stderr.write("\x1b[1;%dm" % (31) + "Error: {}\n".format(e) + "\x1b[0m")
        sys.exit(1)
    print("--Done comparing guesseses to passwords. Results were saved in results folder training_results.txt file-- ", file=sys.stderr)    

# Reads passwords guesses from training result file and checks them against given password
def guess(password):

    try:
        fo = open("results/"+CONFIG.TRAINING_RESULT_FILE, 'r')
        if os.stat("results/"+CONFIG.TRAINING_RESULT_FILE).st_size != 0:
            attempts = 0
            for guess in fo:
                guess = guess.rstrip('\r\n')
                attempts +=1
                if guess == password:
                    return attempts
            return -1
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