#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dice import Dice
import unittest

class TestDiceClass(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()
        self.roll_list = self.dice.roll_list("100d100")

    def tearDown(self):
        pass

    def testLen_roll_list(self):
        self.assertEqual(100, len(self.roll_list))

    def testNumber_roll_list(self):
        for member in self.roll_list:
            assert(1 <= member and member <= 100)

    def testSimple_roll(self):
        result = self.dice.roll("1d100")
        assert(1 <= result and result <= 100)

    def testAdd_roll(self):
        result = self.dice.roll("1d100+1")
        assert(2 <= result and result <= 101)

    def testPlus_roll(self):
        result = self.dice.roll("1d100+1")
        assert(2 <= result and result <= 101)

    def testMinus_roll(self):
        result = self.dice.roll("1d100-1")
        assert(0 <= result and result <= 99)

    def testMulti_roll(self):
        result = self.dice.roll("1d100*2")
        assert(2 <= result and result <= 200)
        assert(result % 2 == 0)

    def testDiv_roll(self):
        result = self.dice.roll("1d100/2")
        assert(1 <= result and result <= 50)

if __name__ == "__main__":
    unittest.main()
