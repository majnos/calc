import unittest

from app.calc import Calc

## https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137

class TestAssignment(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_empty_returns_0(self):
        res = self.calc.add("")
        self.assertEqual(res,0)

    def test_add_one_number_return_self(self):
        res = self.calc.add("1")
        self.assertEqual(res,1)

    def test_add_two_numbers_return_correct(self):
        res = self.calc.add("1,2")
        self.assertEqual(res, 3)

    def test_n_numbers_correct(self):
        res = self.calc.add("1,2,5,9,1000,10000")
        self.assertEqual(res, 11017)

    def test_two_separators_correct(self):
        res = self.calc.add("1,2\n3")
        self.assertEqual(res, 6)

    def test_custom_separator_correct(self):
        res = self.calc.add("[:]\n1:2:3")
        self.assertEqual(res, 6)

    def test_custom_separator_semicolon_correct(self):
        res = self.calc.add("[;]\n1;2;3")
        self.assertEqual(res, 6)

    def test_three_numbers_two_separators_incorrect(self):
        with self.assertRaises(ValueError):
            self.calc.add("1,2\n 3")

    def test_one_number_two_separators_incorrect(self):
        with self.assertRaises(ValueError):
            self.calc.add("1,\n")

    def test_randomstring_raises(self):
        with self.assertRaises(ValueError):
            self.calc.add("ran,do/mstring")

    def test_negatives_not_allowed_raises(self):
        with self.assertRaises(ValueError):
            self.calc.add("1,-2,-5,10,-101,-52")


if __name__ == '__main__':
    unittest.main()
