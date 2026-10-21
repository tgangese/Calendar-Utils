import unittest
from calendar_utils import is_leap, days_in_month

class TestCalendarUtils(unittest.TestCase):
    def test_is_leap(self):
        self.assertTrue(is_leap(2020))
        self.assertTrue(is_leap(2000)) # divisible by 400
        self.assertFalse(is_leap(1900)) # divisible by 100 but not 400
        self.assertFalse(is_leap(2026))

    def test_days_in_month(self):
        self.assertEqual(days_in_month(2026, 2), 28)
        self.assertEqual(days_in_month(2024, 2), 29)
        self.assertEqual(days_in_month(2026, 1), 31)
        self.assertEqual(days_in_month(2026, 4), 30)

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            days_in_month(2026, 13)

if __name__ == "__main__":
    unittest.main()