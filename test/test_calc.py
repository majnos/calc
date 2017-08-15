import unittest

from app.calc import Calc

## https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137

class TestAssignmentOne(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_empty_returns_0(self):
        res = self.calc.add("")
        self.assertEqual(res,0)

    def test_add_one_number_return_self(self):
        res = self.calc.add("1")
        self.assertEqual(res,1)

    def test_add_two_numbers_return_correct(self):
        res = self.calc.add("1\n2")
        self.assertEqual(res, 3)

    def test_two_separators_correct(self):
        res = self.calc.add("1\n2\n3")
        self.assertEqual(res, 6)

    # def test_randomstring_raises(self):
    #     with self.assertRaises(ValueError):
    #         self.calc.add("ran,do/mstring")
    #     print("dummy")

class TestAssignmentTwo(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_n_numbers_correct(self):
        res = self.calc.add("1\n2\n5\n9\n500\n800")
        self.assertEqual(res, 1317)

class TestAssignmentThree(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_custom_separator_correct(self):
        res = self.calc.add("[:]\n1:2:3")
        self.assertEqual(res, 6)

    def test_custom_separator_semicolon_correct(self):
        res = self.calc.add("[;]\n1;2;3")
        self.assertEqual(res, 6)

    # def test_three_numbers_two_separators_incorrect(self):
    #     with self.assertRaises(Exception):
    #         self.calc.add("1,2\n3")

    # def test_one_number_two_separators_incorrect(self):
    #     with self.assertRaises(Exception):
    #         self.calc.add("1,\n")

class TestAssignmentFour(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    # def test_negatives_not_allowed_raises(self):
    #     with self.assertRaises(ValueError) as context:
    #         self.calc.add("1\n-2\n3\n-5")
    #     self.assertTrue("Negatives not allowed ['-2', '-5']" in context.exception.args[0])


class TestAssignmentFive(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_larger_than_thousand_ignored(self):
        res = self.calc.add("2\n2000")
        self.assertEqual(res, 2)

    def test_larger_than_thousand_ignored(self):
        res = self.calc.add("2\n2000\n10")
        self.assertEqual(res, 12)

class TestAssignmentSix(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_larger_than_thousand_ignored(self):
        res = self.calc.add("[;;;]\n1;;;2;;;3")
        self.assertEqual(res, 6)

if __name__ == '__main__':
    unittest.main()
