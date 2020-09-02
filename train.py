#!/usr/bin/env python3

''' This script loads the passwords from the input folders training file (currently named training.txt) 
and ouputs a .txt file to results folder containing password guesses based on markov chains'''

# imports
import sys
from bforce.brute_force import bruteForce
from markov.markov import markov
from configs.configure import Configure

# loads training file and generates password guesses to training_results.txt file 
def train():
    markovIt = markov({
        "name": CONFIG.NAME,
        "alphabet": CONFIG.ALPHABET,
        "ngram_size": CONFIG.NGRAM_SIZE,
        "number_of_guesses": CONFIG.NUMBER_OF_GUESSES,
        "training_file": CONFIG.TRAINING_FILE
    })
    # Generates guesses
    print("--Starting to generate guesses based on input folders training.txt data-- ", file=sys.stderr)
    try:
        fo = open("results/"+CONFIG.TRAINING_FILE.rstrip('.txt')+"_result.txt", "w")
        with open("input/"+CONFIG.TRAINING_FILE, 'r') as inputfile:
            inputWordList = list()
            for line in inputfile:
                line = line.rstrip('\r\n')
                inputWordList.append(line)
            ngrams = markovIt.build(inputWordList) # generates ngrams from input words
            guesses = markovIt.generate(ngrams) # generates guesses from input ngrams
            for password in guesses:
                fo.write("{}\n".format(password)) # writes guesses to file
                print(password)
            fo.flush()
        fo.close()
    except Exception as e:    
        sys.stderr.write("Training file is empty")
        sys.exit(1)
    print("--Done generating guesses. Guesses were saved in results folder training_results.txt file-- ", file=sys.stderr)

def main():
    try:
        global CONFIG
        CONFIG = Configure({"name":"My Config"})
        train()
    except Exception as e:
        sys.stderr.write("\x1b[1;%dm" % (31) + "Error: {}\n".format(e) + "\x1b[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()