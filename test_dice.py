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

    def testNone_roll_list(self):
        self.assertEqual(None, self.dice.roll_list("aaaa"))

    def testNumber_roll_list(self):
        for member in self.roll_list:
            assert(1 <= member and member <= 100)

    def testSimple_roll(self):
        result = self.dice.roll("1d100")
        assert(1 <= result and result <= 100)
    
    def testSimple2_roll(self):
        self.assertEqual(150, self.dice.roll("2d100", [100,50]))

    def testNone_roll(self):
        self.assertEqual(None, self.dice.roll("aaaa"))


    def testPlus_roll(self):
        result = self.dice.roll("1d100+1")
        assert(2 <= result and result <= 101)

    def testPlus2_roll(self):
        self.assertEqual(151, self.dice.roll("2d100+1", [100,50]))

    def testMinus_roll(self):
        result = self.dice.roll("1d100-1")
        assert(0 <= result and result <= 99)

    def testMinus2_roll(self):
        self.assertEqual(149, self.dice.roll("2d100-1", [100,50]))

    def testMulti_roll(self):
        result = self.dice.roll("1d100*2")
        assert(2 <= result and result <= 200)
        assert(result % 2 == 0)

        result = self.dice.roll("1d100x2")
        assert(2 <= result and result <= 200)
        assert(result % 2 == 0)

    def testMulti2_roll(self):
        self.assertEqual(300, self.dice.roll("2d100*2", [100,50]))
        self.assertEqual(300, self.dice.roll("2d100x2", [100,50]))

    def testDiv_roll(self):
        result = self.dice.roll("1d100/2")
        assert(1 <= result and result <= 50)

    def testDiv2_roll(self):
        self.assertEqual(75, self.dice.roll("2d100/2", [100,50]))

if __name__ == "__main__":
    unittest.main()
