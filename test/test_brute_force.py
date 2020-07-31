import unittest

from application.brute_force import bruteForce

class TestBruteForceMethod(unittest.TestCase):

    def test_bruteForce(self):
        tries, timeToCrack = bruteForce("ale")
        self.assertEqual(tries, 97200, "Should be 9039621")

if __name__ == '__main__':
    unittest.main()