"""
Sample test
"""

from django.test import SimpleTestCase

from . import calc


class ClacTests(SimpleTestCase):

    def test_add_numners(self):
        """Test adding numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """Test subtracting numbers"""
        res = abs(calc.subtract(2, 5))
        self.assertEqual(res, 3)
