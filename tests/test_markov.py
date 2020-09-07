import unittest

from markov.markov import markov
from configs.configure import Configure

# Unit tests for bruteForce class
class TestMarkovMethod(unittest.TestCase):

    def setUp(self):

        self.markov = markov({
            "name" : "test-file",
            "passwords_file" : "passwords.txt",
            "training_file" : "training.txt",
            "ngram_size" : 3,
            "max_number_of_guesses" : 50000,
            "alphabet" : "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
            })

    # tests that ngrams are successfully created
    def test_markov_build_equals(self):
        testi = list()
        testi.append("tes")
        ngram = self.markov.buildNgrams(testi)
        self.assertEqual(ngram, {'tes': {'ip_count': 1, 'cp_counter': 1, 'next_letter': {None: 1}}})

    # tests that ngrams are successfully created
    def test_markov_build_not_equal(self):
        testi = list()
        testi.append("testi")
        ngram = self.markov.buildNgrams("testi")
        self.assertNotEqual(ngram, {('e', 's', 't'): ['i'], ('s', 't', 'i'): [None]})
    
    # tests that password guesses are successfully created
    def test_markov_generate_equals(self):
        lista = list()
        lista.append("testi")
        lista.append("toinen")
        lista.append("kolmas")
        ngram = self.markov.buildNgrams(lista)
        result = self.markov.generateGuesses(ngram)
        self.assertEqual(len(result), 3)
    
    # tests that password guesses are successfully created
    def test_markov_generate_not_equal(self):
        lista = list()
        lista.append("testi")
        ngram = self.markov.buildNgrams(lista)
        result = self.markov.generateGuesses(ngram)
        self.assertNotEqual(result, "testi")

if __name__ == '__main__':
    unittest.main()