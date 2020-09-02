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
            "number_of_guesses" : 50000,
            "alphabet" : "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?",
            "training_result_file": "training_result.txt"
            })

    # tests that ngrams are successfully created
    def test_markov_build_equals(self):
        testi = list()
        testi.append("testi")
        ngram = self.markov.build(testi)
        self.assertEqual(ngram, {('t', 'e', 's'): ['t'], ('e', 's', 't'): ['i'], ('s', 't', 'i'): [None]})

    # tests that ngrams are successfully created
    def test_markov_build_not_equal(self):
        testi = list()
        testi.append("testi")
        ngram = self.markov.build("testi")
        self.assertNotEqual(ngram, {('e', 's', 't'): ['i'], ('s', 't', 'i'): [None]})
    
    # tests that password guesses are successfully created
    def test_markov_generate_equals(self):
        lista = list()
        lista.append("testi")
        ngram = self.markov.build(lista)
        result = self.markov.generate(ngram)
        self.assertEqual(len(result), 3)
    
    # tests that password guesses are successfully created
    def test_markov_generate_not_equal(self):
        lista = list()
        lista.append("testi")
        ngram = self.markov.build(lista)
        result = self.markov.generate(ngram)
        self.assertNotEqual(result, "testi")

if __name__ == '__main__':
    unittest.main()