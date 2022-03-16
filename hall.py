from random import randint, shuffle


class MontyHall:
	def __init__(self, iterations: int = 1000):
		self.variants = ['Goat', 'Goat', 'Car']
		self.wins = 0
		self.iterations = iterations
		self.choose_another = False

	def __repr__(self):
		win_ratio = self.wins / self.iterations
		loses = self.iterations - self.wins
		lose_ratio = loses / self.iterations
		return f"""
			Win ratio: {win_ratio}
			Lose ratio: {lose_ratio}
			Iteration: {self.iterations} 
			Wins: {self.wins}
			Loses: {loses}"""

	def __reset(self):
		self.variants = ['Goat', 'Goat', 'Car']
		shuffle(self.variants)

	def reset(self):
		self.wins = 0
		self.__reset()

	def switch_mode(self):
		self.choose_another = not self.choose_another


	def start(self):
		for _ in range(self.iterations):
			random_index = randint(0, 2)
			choice = self.variants.pop(random_index)

			random_remaining_index = randint(0, 1)
			if self.variants[random_remaining_index] == 'Car':
				stay = self.variants.pop(random_remaining_index)
				door_with_goat = self.variants[0]
			else:
				door_with_goat = self.variants.pop(random_remaining_index)
				stay = self.variants[0]

			if door_with_goat != 'Goat':
				raise Exception('Goat not chosen')

			if self.choose_another:
				choice = stay

			if choice == 'Car':
				self.wins += 1

			self.__reset()
