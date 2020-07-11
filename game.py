
import numpy as np
import random
import time
from itertools import product
import sys

_BIRTH = 3
_SUSTAIN = (2, 3)
_LONELY = (0, 1)
_CROWDED = 4




class Game:
	"""
	Generate game on a field with a fixed size
	"""

	def __init__(self, **kwargs):
		"""Initiate a new game """

		self.x_size = kwargs.get('size', 10)
		self.y_size = kwargs.get('size', 10)
		self.rnseed = kwargs.get('rnseed', 0)
		self.cell_density = kwargs.get('cell_density', 50)

		self.fdelay = kwargs.get('fdelay', 0.3)

		self.live_marker = kwargs.get('live_marker', 'O')
		self.dead_marker = kwargs.get('dead_marker', '.')
		self.sep_marker = kwargs.get('sep_marker', '  ')

		self.xys = []
		self.history = {}
		self.log = {}

		self.isrepeat = False

		self._set_xys()
		self._initiate_step()

	def __str__(self):
		""" Return str(self) """
		atts = vars(self)
		out = 'Game parameters:\n'
		for k in atts.keys():
			if k not in ['xys', 'history']:
				out = out + f'\n{str(k)}: {atts[k]}'

		return out

	def _set_xys(self):
		"""Create generator of (x, y) coordinates pairs"""

		self.xys = list(product(list(range(self.x_size)), list(range(self.y_size))))

		return True

	def _initiate_step(self):
		"""Create initial step with randomly allocated cells"""

		density = self.cell_density
		rnseed = self.rnseed
		x_size = self.x_size
		y_size = self.y_size

		weights = [100 - density, density]
		k = x_size*y_size
		random.seed(rnseed)
		first_step = np.array(random.choices([0, 1],
									   weights = weights,
									   k = k)).reshape(x_size, y_size)
		self.add_to_history(0, first_step)

		return first_step

	def add_to_history(self, step_count, step):
		"""Add most recent step to history that logs all steps"""
		self.history[step_count] = step

		return True

	def get_next_step(self, step):
		'''Generate next step from a previous step'''
		
		next_step = np.zeros((self.x_size, self.y_size), dtype=int)
		for xy in list(self.xys):
			status = self.update_cell(step, xy)
			next_step[xy[0], xy[1]] = status

		return next_step

	def update_cell(self, step, xy):
		'''Update cell status for new iteration'''

		neighbor_sum = self.count_neighbors(step, xy)

		if step[xy[0], xy[1]] == 1:

			if neighbor_sum in _LONELY:
				status = 0

			elif neighbor_sum in _SUSTAIN:
				status = 1

			else:
				status = 0

		else:
			if neighbor_sum == _BIRTH:
				status = 1

			else:
				status = 0

		return status

	def count_neighbors(self, step, xy):
		'''Count neighbors for a cell'''
		neighbors = []
		for x in range(max(0, xy[0] - 1), min(xy[0] + 2, self.x_size)):
			for y in range(max(0, xy[1] - 1), min(xy[1] + 2, self.y_size)):
				try:
					neighbors.append(step[x, y])
				except IndexError:  # if index out of range
					print('index out of range')
					pass

		neighbors_count = sum(neighbors) - step[xy[0], xy[1]]

		return neighbors_count

	def detect_repeat(self, new_num, new_step):
		'''Detect if step is repeat of a previous step'''

		if self.isrepeat:
			pass
		else:
			for num in self.history.keys():
				step = self.history[num]
				if np.array_equal(step, new_step) and (num != new_num):
					self.isrepeat = True
					self.log['repeat_start'] = num
					self.log['repeat_end'] = new_num
					self.log['cells_last'] = new_step.sum()

				else:
					pass

		return self.isrepeat

	def add_to_log(self):
		'''Add entry for a step to the log'''

		atts = self.__dict__

		log_keys = ['x_size', 'y_size', 'cell_density','isrepeat', 'rnseed']

		self.log.update({k:atts[k] for k in log_keys})
		return True

	def run_until_repeat(self):
		'''Run until fields start to cycle'''
		num = 0
		while not self.isrepeat:
			new_step = self.get_next_step(self.history[num])
			num = num + 1
			self.detect_repeat(num, new_step)
			self.add_to_history(num, new_step)

		self.add_to_log()

		return num

	def format_step(self, step):
		'''Convert binary field into a picture'''
		alive = self.live_marker
		dead = self.dead_marker
		sep = self.sep_marker
		pm = np.where(step < 1, dead, alive)

		pm_str = '\n'.join([sep.join([str(cell) for cell in row]) for row in pm])

		return pm_str

	def animation(self):
		'''Output animation for each step'''
		if len(self.history.keys()) < 2:
			total = self.run_until_repeat()
		else:
			total = max(self.history.keys())

		for num in self.history.keys():
			step = self.history[num]
			fstep = self.format_step(step)
			pops = step.sum()
			frame = '\nstep: ' + str(num) \
					+ ' cells: ' + str(pops) \
					+ '\n' + fstep + '\n'
			sys.stdout.write(frame)
			sys.stdout.flush()
			time.sleep(self.fdelay)

		print(f'\nsteps in iteration: {total}')

		return self

if __name__ == '__main__':

	def play_game():
		game = Game()
		game.animation()
		for k, v in game.log.items():ip
			print(f'{k}: {v}')
		return game


	play_game()








