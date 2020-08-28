#!/usr/bin/env python3

''' This script loads the passwords and runs the scripts that try to guess the passwords in input list'''

# imports
import sys
from bforce.brute_force import bruteForce
from markov.markov import markov
from configs.configure import Configure

# loads input files, runs brute force and markov chain based guesser and writes output to results
def run():

    bruteforce = bruteForce({
        "name": CONFIG.NAME,
        "alphabet": CONFIG.ALPHABET
    })

    fo = open("results/"+CONFIG.PASSWORDS_FILE.rstrip('.txt')+"_result.txt", "w")
    with open("input/"+CONFIG.PASSWORDS_FILE, 'r') as inputfile:
        for line in inputfile:
            line = line.rstrip('\r\n')
            tries, timeAmount = bruteforce.guess(line)
            triesMarkov, timeAmountMarkov = trainMarkov(line)
            if timeAmountMarkov != 0:
                fo.write("{}\n".format("Password to guess: " + line + ". Brute force algorithm " + str(tries) + " tries and " + str(timeAmount) + " seconds. Markov chain based algorithm: " + str(triesMarkov) + " tries and " + str(timeAmountMarkov) + " seconds to guess the password."))
            else: 
                fo.write("{}\n".format("Password to guess: " + line + ". Brute force algorithm " + str(tries) + " tries and " + str(timeAmount) + " seconds. Markov chain based algorithm wasn't able to guess the password."))
            fo.flush()
    fo.close()

# loads training file and returns tries and time it took to guess the given password
def trainMarkov(passwordToGuess):
    markovIt = markov({
        "name": CONFIG.NAME,
        "alphabet": CONFIG.ALPHABET,
        "ngram_size": CONFIG.NGRAM_SIZE,
        "number_of_guesses": CONFIG.NUMBER_OF_GUESSES
    })
    try:
        with open("input/"+CONFIG.TRAINING_FILE, 'r') as inputfile:
            guesses = list()
            inputWordList = list()
            for line in inputfile:
                line = line.rstrip('\r\n')
                inputWordList.append(line)
            ngrams = markovIt.build(inputWordList)
            guesses = markovIt.generate(ngrams)
            tries, timeAmount = markovIt.guess(passwordToGuess,guesses)  
        return(tries, timeAmount)
    except Exception as e:    
        sys.stderr.write("Training file is empty")
        sys.exit(1)

def main():
    try:
        global CONFIG
        CONFIG = Configure({"name":"My Config"})
        run()
    except Exception as e:
        sys.stderr.write("\x1b[1;%dm" % (31) + "Error: {}\n".format(e) + "\x1b[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()