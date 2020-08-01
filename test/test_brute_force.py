import unittest

from application.brute_force import bruteForce

class TestBruteForceMethod(unittest.TestCase):

    def test_bruteForce_equals(self):
        tries, timeToCrack = bruteForce("ale")
        self.assertEqual(tries, 97200, "Should be 97200")
        self.assertAlmostEqual(timeToCrack, 0.0208, places=2)
    
    def test_bruteForce_not_equals(self):
        tries, timeToCrack = bruteForce("ale")
        self.assertNotEqual(tries, 92200, "Correct is 97200")
        self.assertNotEqual(timeToCrack, 0.0408)

if __name__ == '__main__':
    unittest.main()