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

suite = unittest.TestLoader().loadTestsFromTestCase(TestModulesClasses)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)