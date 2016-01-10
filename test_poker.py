import unittest
from poker import *

class test_card(unittest.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError):
            c = Card(234)
        with self.assertRaises(TypeError):
            c = Card([1, 2, 3])

    def test_value_error(self):
        with self.assertRaises(ValueError):
            c = Card("7")
        with self.assertRaises(ValueError):
            c = Card("")
        with self.assertRaises(ValueError):
            c = Card("GK")
        with self.assertRaises(ValueError):
            c = Card("11S")
        with self.assertRaises(ValueError):
            c = Card("6T")

    def test_constructor(self):
        c = Card("jd")
        self.assertEquals(str(c), 'JD')
        c = Card("GB")
        self.assertEquals(str(c), 'GB')
        c = Card("10d")
        self.assertEquals(str(c), '10D')
        c = Card("10D")
        self.assertEquals(str(c), '10D')
        c = Card("AH")
        self.assertEquals(str(c), 'AH')

unittest.main()