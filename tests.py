import unittest
from implementation import get_us_date
class TestGetUSDateFunction(unittest.TestCase):
    def test_day_count_at_start(self):
        self.assertEqual(get_us_date(0), 'January 1, 1960')
        
if __name__ == '__main__':
    unittest.main()