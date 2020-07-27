import unittest

class TestClasses(unittest.TestCase):
    def test_Calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(5, 6), 11)
        self.assertEqual(calculator.subtract(5, 6), -1)
        self.assertEqual(calculator.multiply(5, 6), 30)
        self.assertAlmostEqual(calculator.divide(6, 3), 2.0)
    def test_Aggregator(self):
        aggregator = Aggregator()
        self.assertEqual(aggregator.product(5, 5, 6, 6), 900)
        self.assertEqual(aggregator.sum(5, 5, 6, 6), 22)

suite = unittest.TestLoader().loadTestsFromTestCase(TestClasses)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)