#!/usr/bin/env python3

''' This script loads the passwords and runs the scripts that try to guess the passwords in input list'''

# imports
import sys
from bforce.brute_force import bruteForce
from markov.markov import markov
from configs.configure import Configure

# loads input files, runs brute force guesser and writes output to results
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
            fo.write("{}\t{}\n".format(tries, timeAmount))
            fo.flush()
    fo.close()

def runMarkov():
    markovIt = markov({
        "name": CONFIG.NAME,
        "alphabet": CONFIG.ALPHABET
    })
    
    fo = open("results/"+CONFIG.PASSWORDS_FILE.rstrip('.txt')+"_result.txt", "w")
    with open("input/"+CONFIG.PASSWORDS_FILE, 'r') as inputfile:
        for line in inputfile:
            line = line.rstrip('\r\n')
            ngrams = markovIt.build(line,3)
            tries, timeAmount = markovIt.generate(ngrams,3,line)
            fo.write("{}\t{}\n".format(tries, timeAmount))
            fo.flush()
    fo.close()


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