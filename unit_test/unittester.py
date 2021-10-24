import unittest
from code_for_unit_test.classexplore import *

class MyTestCase(unittest.TestCase):
    def test_default_constructor(self):
        a = First()
        b = Second()
        self.assertEqual(a.a, 1)
        self.assertEqual(a.b, 1)
        self.assertEqual(a.c, 1)
        self.assertEqual(b.a, 1)
        self.assertEqual(b.b, 1)
        self.assertEqual(b.c, 1)
        self.assertEqual(b.d, 1)
        self.assertEqual(b.e, 1)

    def test_add_operator(self):
        a = First()
        b = Second()
        c = b + a
        self.assertEqual(c.a, 2)
        self.assertEqual(c.b, 2)
        self.assertEqual(c.c, 2)
        self.assertEqual(c.d, 1)
        self.assertEqual(c.e, 1)

    def test_factory_method(self):
        a = First.firstFactoryMethod()
        b = Second.secondFactoryMethod()
        self.assertEqual(a.a, 3)
        self.assertEqual(a.b, 6)
        self.assertEqual(a.c, 7)
        self.assertEqual(b.a, 11)
        self.assertEqual(b.b, 22)
        self.assertEqual(b.c, 33)
        self.assertEqual(b.d, 1)
        self.assertEqual(b.e, 1)

class MySecondTestCase(unittest.TestCase):
    def test_constructor(self):
        a = First(2, 3, 4)
        b = Second(11, 12, 13, 14, 15)

        self.assertEqual(a.a, 2)
        self.assertEqual(a.b, 3)
        self.assertEqual(a.c, 4)
        self.assertEqual(b.a, 11)
        self.assertEqual(b.b, 12)
        self.assertEqual(b.c, 13)
        self.assertEqual(b.d, 14)
        self.assertEqual(b.e, 15)

if __name__ == '__main__':
    unittest.main()
