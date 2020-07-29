import unittest

class TestModulesClasses(unittest.TestCase):
    def test_BMI(self):
        from bmi_calculator import BMI
        bmi = BMI(198, 129) # Zion Williamson
        self.assertAlmostEqual(bmi.get_bmi(), 32.90480563207836)
        self.assertEqual(bmi.get_bmi_label(), 'Obese')
        bmi = BMI(206, 113) # LeBron James
        self.assertAlmostEqual(bmi.get_bmi(), 26.628334433028563)
        self.assertEqual(bmi.get_bmi_label(), 'Overweight')
    def test_Casino(self):
        from casino import Casino
        my_casino = Casino()
        self.assertIn(my_casino.toss_a_coin(), {'Head', 'Tail'})
        self.assertIn(my_casino.roll_a_dice(), {1, 2, 3, 4, 5, 6})
        self.assertIn(my_casino.deal_a_card(), {'10 of clubs', 'jack of hearts', 'ace of clubs', '5 of hearts', 'ace of diamonds', '4 of hearts', '10 of hearts', '2 of clubs', 'jack of diamonds', '6 of spades', '10 of spades', '8 of clubs', '6 of diamonds', 'king of clubs', '8 of spades', '7 of spades', '2 of diamonds', 'jack of spades', '2 of spades', '8 of diamonds', '9 of diamonds', 'ace of spades', '3 of clubs', 'king of spades', 'queen of spades', '6 of hearts', 'king of diamonds', '4 of spades', '5 of spades', '3 of hearts', 'ace of hearts', '7 of hearts', '3 of diamonds', 'queen of clubs', 'queen of diamonds', '4 of diamonds', 'king of hearts', '9 of hearts', '4 of clubs', '7 of clubs', '8 of hearts', 'jack of clubs', '7 of diamonds', '10 of diamonds', '5 of clubs', '9 of spades', '9 of clubs', '2 of hearts', '6 of clubs', '3 of spades', 'queen of hearts', '5 of diamonds'})
        
    def test_Stats(self):
        from stats import Stats
        statistics = Stats(1, 2, 2, 3, 4, 7, 9)
        self.assertAlmostEqual(statistics.mean(), 4.0)
        self.assertEqual(statistics.median(), 3)
        self.assertEqual(statistics.modes(), [2])
        statistics = Stats(1, 2, 2, 3, 4, 7, 9, 7)
        self.assertAlmostEqual(statistics.mean(), 4.375)
        self.assertAlmostEqual(statistics.median(), 3.5)
        self.assertEqual(statistics.modes(), [2, 7])

suite = unittest.TestLoader().loadTestsFromTestCase(TestModulesClasses)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)