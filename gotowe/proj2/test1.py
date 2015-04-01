import unittest
from zad2 import Samolot
from zad2 import Dane

class Testing(unittest.TestCase):
	def setUp(self):
		self.computer = Dane();

	def test_correct_return_type_and_range(self):
		assert self.computer.odczyt() > 20 and self.computer.odczyt() < -20 , "Poza zakresem"
unittest.main()
