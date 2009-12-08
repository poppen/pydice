#!-*- conding:utf-8 -*-
import re
import random

class Dice:

	def __init__(self):
		self.throws = []

	def roll_array(self, dice_string):

		prog = re.compile(r"""
			^       # beginning of line
			(\d+)?  # optional count in group[0]
			[dD]    # 'd' for dice
			(       # type of dice in group[1]
				\d+ # either one or more digits
				|   # or
				%   # a percent sign for d% = d100
			)
		""", re.VERBOSE)

		match = prog.match(dice_string)
		if match == None:
			return

		num = match.group(1)
		if num:
			num = int(num)
		else:
			num = 1

		type = match.group(2)
		if type == '%':
			type = 100
		else:
			type = int(type)

		for cnt in range(num):
			self.throws.append(random.randint(1,type))
