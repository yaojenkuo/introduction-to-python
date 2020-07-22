import unittest

class TestDataStructure(unittest.TestCase):
    def test_select_sw(self):
        self.assertEqual(select_sw(cast), 'Elizabeth Olsen')
    def test_first_five(self):
        self.assertEqual(first_five(cast), ['Robert Downey Jr.', 'Chris Hemsworth', 'Mark Ruffalo', 'Chris Evans', 'Scarlett Johansson'])
    def test_select_sh(self):
        self.assertEqual(select_sh(cast), ('Robert Downey Jr.', 'Benedict Cumberbatch'))
    def test_get_release_dates(self):
        self.assertEqual(get_release_dates(the_avengers), ('11 April 2012', '25 April 2012'))
    def test_select_bw_hawkeye(self):
        self.assertEqual(select_bw_hawkeye(the_avengers), ('Natasha Romanoff', 'Clint Barton'))
    def test_tpe_zip_code(self):
        self.assertEqual(tpe_zip_code('松山區'), '105')
        self.assertEqual(tpe_zip_code('信義區'), '110')
        self.assertEqual(tpe_zip_code('中山區'), '104')

suite = unittest.TestLoader().loadTestsFromTestCase(TestDataStructure)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)