from django.test import TestCase

from app.calc import add

class CalcTests(TestCase):
  
  def test_add_number(self):
    """Test the sum works"""
    self.assertEqual(add(3,4), 7)