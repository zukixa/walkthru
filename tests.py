import unittest
from implementation import get_us_date
class TestGetUSDateFunction(unittest.TestCase):
    def test_day_count_at_start(self):
        self.assertEqual(get_us_date(0), 'January 1, 1960')
    def test_day_count_after_start(self):
        self.assertEqual(get_us_date(10), 'January 11, 1960')
    def test_day_in_next_month(self):
        self.assertEqual(get_us_date(32), 'February 2, 1960')
    def test_day_in_next_year_during_leap(self):
        self.assertEqual(get_us_date(366), 'January 1, 1961')
    def test_for_leap_year_transition(self):
        self.assertEqual(get_us_date(425), 'March 1, 1961')
    def test_day_count_before_start(self):
        self.assertEqual(get_us_date(-1000), 'April 6, 1957')
    def test_a_non_int_value(self):
        with self.assertRaises(ValueError):
            get_us_date('a')
        
if __name__ == '__main__':
    unittest.main()