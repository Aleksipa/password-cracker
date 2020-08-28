# Load external modules
import json, sys

class Configure:
    
    def __init__(self, dict):
        self.name = dict['name']
        self._read_config()

    def _read_config(self):
        try:
            with open('./configs/config.json', 'r') as configfile:
                config = json.load(configfile)
                self.NAME = config.get("name", "File")
                self.PASSWORDS_FILE = config.get("passwords_file", "passwords.txt")
                self.TRAINING_FILE = config.get("training_file", "training.txt")
                self.NGRAM_SIZE = config.get("ngram_size", 3)
                self.NUMBER_OF_GUESSES = config.get("number_of_guesses", 100)
                self.ALPHABET = config.get("alphabet", "abcdefghijklmnopqrstuvwxyz")

        except Exception as e:
            sys.stderr.write("\x1b[1;%dm" % (31) + "Malformed config file: {}\n".format(e) + "\x1b[0m")
            sys.exit(1)