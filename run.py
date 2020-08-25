#!/usr/bin/env python3

''' This script loads the passwords and runs the scripts that try to guess the passwords in input list'''

# imports
import sys
from bforce.brute_force import bruteForce
from markov.markov import markov
from configs.configure import Configure

# loads input files, runs brute force guesser and writes output to results
def run(tries, timeAmount, triesMarkov, timeAmountMarkov):
    fo = open("results/"+CONFIG.TRAINING_FILE.rstrip('.txt')+"_result.txt", "w")
    if timeAmountMarkov != 0:
        fo.write("{}\t{}\t{}\t{}\n".format("It took brute force algorithm " + str(tries), "tries and " + str(timeAmount) + " seconds to guess the password. For markov chain based algorithm it took ", str(triesMarkov), "tries and " + str(timeAmountMarkov) + " seconds to guess the password"))
    else: 
        fo.write("{}\t{}\n".format("It took brute force algorithm " + str(tries), "tries and " + str(timeAmount) + " seconds to guess the password. Markov chain based algorithm wasn't able to guess the password."))
    fo.flush()
    fo.close()

def BruteForce():
    bruteforce = bruteForce({
        "name": CONFIG.NAME,
        "alphabet": CONFIG.ALPHABET
    })

    fo = open("input/"+CONFIG.PASSWORDS_FILE, 'r')
    for line in fo:
            line = line.rstrip('\r\n')
            tries, timeAmount = bruteforce.guess(line)
            fo.flush()
    fo.close()
    return tries, timeAmount

def trainMarkov():
    markovIt = markov({
        "name": CONFIG.NAME,
        "alphabet": CONFIG.ALPHABET
    })
    
    with open("input/"+CONFIG.TRAINING_FILE, 'r') as inputfile, open("input/"+CONFIG.PASSWORDS_FILE, 'r') as inputfile2:
        guesses = list()
        for line in inputfile:
            line = line.rstrip('\r\n')
            ngrams = markovIt.build(line,3)
            guess = markovIt.generate(ngrams,3,line)
            guesses.append(guess)
        for line2 in inputfile2:
            line2 = line.rstrip('\r\n')
            tries, timeAmount = markovIt.guess(line2,guesses)  
    return(tries, timeAmount)

def main():
    try:
        global CONFIG
        CONFIG = Configure({"name":"My Config"})
        tries, timeAmount = BruteForce()
        triesMarkov, timeAmountMarkov = trainMarkov()
        run(tries, timeAmount, triesMarkov, timeAmountMarkov)
    except Exception as e:
        sys.stderr.write("\x1b[1;%dm" % (31) + "Error: {}\n".format(e) + "\x1b[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()