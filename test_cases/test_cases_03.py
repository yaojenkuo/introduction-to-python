import unittest

class TestDataTypes(unittest.TestCase):
    def test_what_ross_said(self):
        self.assertEqual(what_ross_said(), """Let's put aside the fact that you "accidentally" pick up my grandmother's ring.""")
        self.assertIs(type(what_ross_said()), str)
    def test_hello_something(self):
        self.assertEqual(hello_something('world'), 'Hello, world!')
        self.assertEqual(hello_something('Earth'), 'Hello, Earth!')
    def test_is_odd(self):
        self.assertFalse(is_odd(0))
        self.assertTrue(is_odd(1))
        self.assertFalse(is_odd(2))
        self.assertTrue(is_odd(3))
    def test_last_digit_is_odd(self):
        self.assertTrue(last_digit_is_odd('A123456789'))
        self.assertFalse(last_digit_is_odd('A123456780'))
    def test_is_overweight(self):
        self.assertTrue(is_overweight(198, 129))
        self.assertFalse(is_overweight(198, 98))

suite = unittest.TestLoader().loadTestsFromTestCase(TestDataTypes)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)