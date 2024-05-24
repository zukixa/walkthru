import unittest
from implementation import get_us_date
class TestGetUSDateFunction(unittest.TestCase):
    def test_day_count_at_start(self):
        self.assertEqual(get_us_date(0), 'January 1, 1960')
    def test_day_count_after_start(self):
        self.assertEqual(get_us_date(10), 'January 11, 1960')
    def test_day_in_next_month(self):
        self.assertEqual(get_us_date(32), 'February 2, 1960')
        
if __name__ == '__main__':
    unittest.main()