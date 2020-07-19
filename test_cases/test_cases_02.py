import unittest

class TestFunctionsAndNumerics(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(55, 66), 121)
    def test_movie_time(self):
        self.assertEqual(movie_time(3, 1), 181)
        self.assertEqual(movie_time(2, 29), 149)
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(30), 86.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(35), 95.0)
    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(86), 30.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(95), 35.0)
    def test_bmi_calculator(self):
        self.assertAlmostEqual(bmi_calculator(216, 147), 31.507201646090532)
        self.assertAlmostEqual(bmi_calculator(198, 129), 32.90480563207836)

suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctionsAndNumerics)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)