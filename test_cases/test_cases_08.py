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
        self.assertEqual(aggregator.summation(5, 5, 6, 6), 22)
    def test_NewCalculator(self):
        new_calculator = NewCalculator()
        self.assertEqual(new_calculator.add(5, 6), 11)
        self.assertEqual(new_calculator.subtract(5, 6), -1)
        self.assertEqual(new_calculator.multiply(5, 6), 30)
        self.assertAlmostEqual(new_calculator.divide(6, 3), 2.0)
        self.assertEqual(new_calculator.power(5, 2), 25)
        self.assertEqual(new_calculator.get_modulo(5, 6), 5)
        self.assertEqual(new_calculator.get_quotient(5, 6), 0)
    def test_NewAggregator(self):
        new_aggregator = NewAggregator()
        self.assertEqual(new_aggregator.product(5, 5, 6, 6), 900)
        self.assertEqual(new_aggregator.summation(5, 5, 6, 6), 22)
        self.assertEqual(new_aggregator.length(5, 5, 6, 6), 4)
        #self.assertEqual(new_aggregator.mean(5, 5, 6, 6), 5.5)
    def test_Recursives(self):
        recursives = Recursives(0)
        self.assertEqual(recursives.factorial(), 1)
        self.assertEqual(recursives.fibonacci(), 0)
        recursives = Recursives(1)
        self.assertEqual(recursives.factorial(), 1)
        self.assertEqual(recursives.fibonacci(), 1)
        recursives = Recursives(2)
        self.assertEqual(recursives.factorial(), 2)
        self.assertEqual(recursives.fibonacci(), 1)

suite = unittest.TestLoader().loadTestsFromTestCase(TestClasses)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)