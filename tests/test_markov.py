import unittest

from markov.markov import markov
from configs.configure import Configure

class TestMarkovMethod(unittest.TestCase):

    def setUp(self):

        self.markov = markov({
            "name": "test",
            "alphabet": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
            })

    def test_markov_build_equals(self):
        testi = list()
        testi.append("testi")
        ngram = self.markov.build(testi, 3)
        self.assertEqual(ngram, {('t', 'e', 's'): ['t'], ('e', 's', 't'): ['i'], ('s', 't', 'i'): [None]})

    def test_markov_build_not_equal(self):
        testi = list()
        testi.append("testi")
        ngram = self.markov.build("testi", 3)
        self.assertNotEqual(ngram, {('e', 's', 't'): ['i'], ('s', 't', 'i'): [None]})
    
    def test_markov_generate_equals(self):
        lista = list()
        lista.append("testi")
        ngram = self.markov.build(lista, 3)
        result = self.markov.generate(ngram,3)
        self.assertEqual(len(result), 3)
    
    def test_markov_generate_not_equal(self):
        lista = list()
        lista.append("testi")
        ngram = self.markov.build(lista, 3)
        result = self.markov.generate(ngram,3)
        self.assertNotEqual(result, "testi")

    def test_markov_guess_equals(self):
        guess = list()
        guess.append("password")
        attemps, executionTime = self.markov.guess("password", guess)
        self.assertEqual(attemps, 1)
    
    def test_markov_guess_not_equal(self):
        guess = list()
        guess.append("password")
        attemps, executionTime = self.markov.guess("testi", guess)
        self.assertEqual(attemps, 1)
    


if __name__ == '__main__':
    unittest.main()