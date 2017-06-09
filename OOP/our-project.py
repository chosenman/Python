import random

class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
	def show(self):
		print self.suit + str(self.value)