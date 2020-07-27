import unittest

class TestFunctions(unittest.TestCase):
    def test_product(self):
        self.assertEqual(product(0, 1, 2), 0)
        self.assertEqual(product(1, 2, 3, 4, 5), 120)
        self.assertEqual(product(1, 3, 5, 7, 9), 945)
    def test_iso_country(self):
        self.assertEqual(iso_country(TWN='Taiwan'), {'TWN': 'Taiwan'})
        self.assertEqual(iso_country(TWN='Taiwan', USA='United States of America'), {'TWN': 'Taiwan', 'USA': 'United States of America'})
        self.assertEqual(iso_country(TWN='Taiwan', USA='United States of America', JPN='Japan'), {'TWN': 'Taiwan', 'USA': 'United States of America', 'JPN': 'Japan'})
    def test_mean(self):
        self.assertAlmostEqual(mean(1, 3, 5, 7, 9), 5.0)
        self.assertAlmostEqual(mean(3, 4, 5, 6, 7), 5.0)
        self.assertAlmostEqual(mean(3), 3.0)
    def test_std(self):
        self.assertAlmostEqual(std(1, 3, 5, 7, 9), 3.1622776601683795)
        self.assertAlmostEqual(std(3, 4, 5, 6, 7), 1.5811388300841898)
        self.assertAlmostEqual(std(3), 'Please input at least 2 numbers.')
    def test_fibonacci_list(self):
        self.assertEqual(fibonacci_list(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_list(5, 1, 2), [1, 2, 3, 5, 8])
        self.assertEqual(fibonacci_list(10, 1, 2), [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)