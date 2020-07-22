import unittest

class TestIterations(unittest.TestCase):
    def test_find_odds(self):
        self.assertEqual(find_odds(5, 10), [5, 7, 9])
        self.assertEqual(find_odds(10, 15), [11, 13, 15])
        self.assertEqual(find_odds(11, 19), [11, 13, 15, 17, 19])
    def test_fizz_buzz_100(self):
        self.assertEqual(fizz_buzz_100(), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'Fizz Buzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'Fizz Buzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'Fizz Buzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'Fizz Buzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz'])
    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels('Luke Skywalker'), 'LUkE SkywAlkEr')
        self.assertEqual(reverse_vowels('Darth Vadar'), 'DArth VAdAr')
        self.assertEqual(reverse_vowels('The Avengers'), 'ThE avEngErs')
    def test_find_primes(self):
        self.assertEqual(find_primes(1, 7), [2, 3, 5, 7])
        self.assertEqual(find_primes(11, 20), [11, 13, 17, 19])
        self.assertEqual(find_primes(11, 29), [11, 13, 17, 19, 23, 29])
    def test_ascii_dict(self):
        self.assertEqual(ascii_dict(), {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122})

suite = unittest.TestLoader().loadTestsFromTestCase(TestIterations)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)