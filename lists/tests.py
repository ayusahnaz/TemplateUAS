from django.test import TestCase
from lists.views import *

# Create your tests here.
class KonversiTest(TestCase):
	def test_positive(self):
		self.assertEqual(konversi(1), "00000000000000000000000000000001")

	def test_nol(self):
		self.assertEqual(konversi(0), "00000000000000000000000000000000")

	def test_negative(self):
		self.assertEqual(konversi(-1), "11111111111111111111111111111111")