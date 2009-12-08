#!-*- conding:utf-8 -*-
import re
import random

class Dice:

	def __init__(self):
		self.throws = []

	def roll(self, line):

		prog = re.compile(r"""
			^                 # beginning of line
			(                 # dice string in group(1)
				(?:\d+)?      # optional count
				[dD]          # 'd' for dice
				(?:           # type of dice:
					\d+       # either one or more digits
					|         # or
					%         # a percent sign for d% = d100
				)
			)
			(?:               # grouping-only parens
				([-+xX*/bB])  # a + - * / b(est) in group(2)
				(\d+)         # an offset in group(3)
			)?                # both of those last are optional
		""", re.VERBOSE)

		match = prog.match(line)
		if match == None:
			return

		dice_string = match.group(1)

		sign = match.group(2)
		if sign != None:
			sign = sign.lower()

		offset = match.group(3)
		if offset != None:
			offset = int(offset)

		throws = self.roll_list(dice_string)
		if len(throws) == 0:
			return

		if sign == 'b':
			throws.sort()
			throws.reverse()
			throws = throws[0:offset]

		result = 0
		result += sum(throws)

		if sign == '+':
			result += offset

		if sign == '-':
			result -= offset

		if sign == '*' or sign == 'x':
			result *= offset

		if sign == '/':
			result /= offset
			result = int(result)

		return result

	def roll_list(self, dice_string):

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

		results = []
		for cnt in range(num):
			results.append(random.randint(1,type))

		return results
