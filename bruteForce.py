#!/usr/bin/env python3

''' This script loads the passwords from input folders passwords.txt file and tries to guess the password using brute force algorithm.'''

# imports
import os
import time
import sys
from bforce.brute_force import bruteForce
from markov.markov import markov
from configs.configure import Configure

# loads password file from input folder and runs brute force based guesser
def runBruteForce():

    bruteforce = bruteForce({
        "name": CONFIG.NAME,
        "alphabet": CONFIG.ALPHABET
    })

    print("--Starting to generate guesses and check them against given password(s)-- ", file=sys.stderr)
    try:
        fo = open("results/"+CONFIG.PASSWORDS_FILE.rstrip('.txt')+"_guessing_result.txt", "w")
        with open("input/"+CONFIG.PASSWORDS_FILE, 'r') as inputfile:
            if os.stat("input/"+CONFIG.PASSWORDS_FILE).st_size != 0:
                for line in inputfile:
                        start = time.time()
                        line = line.rstrip('\r\n')
                        tries = bruteforce.guess(line) # returns the number of guesses it took to guess the password
                        end = time.time()
                        executionTime = end - start  
                        # Write results to file
                        fo.write("{}\n".format("Password to guess: " + line + ". Algorithm: Brute force. " + str(tries) + " tries and " + str(executionTime) + " seconds."))
                        fo.flush()
                fo.close()
            else:
                print("Passwords file is empty! Please add at least one password, exiting", file=sys.stderr)
                sys.exit(1)
    except Exception as e:
        sys.stderr.write("\x1b[1;%dm" % (31) + "Error: {}\n".format(e) + "\x1b[0m")
        sys.exit(1)
    print("--Done comparing guesses to passwords. Results were saved in results folder passwords_guessing_result.txt file-- ", file=sys.stderr)     

def main():
    try:
        global CONFIG
        CONFIG = Configure({"name":"My Config"})
        runBruteForce()
    except Exception as e:
        sys.stderr.write("\x1b[1;%dm" % (31) + "Error: {}\n".format(e) + "\x1b[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()