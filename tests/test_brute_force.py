import unittest

from bforce.brute_force import bruteForce
from configs.configure import Configure

class TestBruteForceMethod(unittest.TestCase):

    def setUp(self):

        self.bforce = bruteForce({
            "name": "test",
            "alphabet": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
            })

    def test_bruteForce_equals(self):
        tries, timeToCrack = self.bforce.guess("ale")
        self.assertEqual(tries, 97200, "Should be 97200")
        self.assertAlmostEqual(timeToCrack, 0.03377, places=1)
    
    def test_bruteForce_not_equal(self):
        tries, timeToCrack = self.bforce.guess("ale")
        self.assertNotEqual(tries, 92200, "Correct is 97200")
        self.assertNotEqual(timeToCrack, 0.0408)

if __name__ == '__main__':
    unittest.main()