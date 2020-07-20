import unittest

class TestConditionals(unittest.TestCase):
    def test_odd_or_even(self):
        self.assertEqual(odd_or_even(0), 'even')
        self.assertEqual(odd_or_even(1), 'odd')
        self.assertEqual(odd_or_even(2), 'even')
        self.assertEqual(odd_or_even(3), 'odd')
    def test_absolute(self):
        self.assertEqual(absolute(-5), 5)
        self.assertEqual(absolute(-6), 6)
        self.assertEqual(absolute(0), 0)
        self.assertEqual(absolute(56), 56)
    def test_step(self):
        self.assertEqual(step(0.1), 0)
        self.assertEqual(step(0.4), 0)
        self.assertEqual(step(0.5), 1)
        self.assertEqual(step(0.9), 1)
    def test_bmi_condition(self):
        self.assertEqual(bmi_condition(198, 129), '身高 198 公分體重 129 公斤是 Obese')
        self.assertEqual(bmi_condition(206, 113), '身高 206 公分體重 113 公斤是 Overweight')
        self.assertEqual(bmi_condition(198, 98), '身高 198 公分體重 98 公斤是 Normal weight')
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')
        self.assertEqual(fizz_buzz(5), 'Buzz')
        self.assertEqual(fizz_buzz(15), 'Fizz Buzz')
        self.assertEqual(fizz_buzz(16), 16)

suite = unittest.TestLoader().loadTestsFromTestCase(TestConditionals)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)