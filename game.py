# Game 

class Game():
	def __init__(self):
		self._score = 0
		self._raspberries_saved = 0

	def update_score(self, amount):
		self._score += amount

	def get_score(self):
		return self._score

	def update_raspberries_saved(self):
		self._raspberries_saved += 1

	def get_raspberries_saved(self):
		return self._raspberries_saved