from argparse import Namespace
import pandas as pd
import game
import argparse
import time
import importlib
importlib.reload(game)
import random

class Play():

	def __init__(self):
		"""Initiate a new play """

		self.args_keys = []
		self.len_gkeys = 0
		self.args_read = self._set_parser()
		self.arg_d = {}
		self.collection = []
		self.log = []
		self.df = None

	def _set_parser(self):
		"""Set parser and parse arguments"""
		parser = argparse.ArgumentParser()
		arg_opts = self._set_arguments()
		for a in arg_opts.values():
			parser.add_argument(*a[:-1], **a[-1])


		res: Namespace = parser.parse_args()


		return res

	def _set_arguments(self):
		'''Set arguments'''

		arg_options = {
			'size': ['-s', '--size',
					   {'type': int,
						'default': 10,
						'help': 'size of square game field'
						}],
			'cell_density': ['-d', '--cell_density',
							  {'type': int,
							   'default': 50,
							   'help': 'percent of live cells at start'
							   }],
			'noanimation': ['-na', '--noanimation',
						  {'action': 'store_true',
						   'default': False,
						   'help': 'run without command line animation'
						   }],
			'fdelay': ['-fd', '--fdelay',
					   {'type': float,
						'default': 0.3,
						'help': 'animation frame delay'
						}],
			'iters': ['-i', '--iters',
			 {'type': int,
			  'default': 1,
			  'help': 'number of game repeats'
			  }],
			'rnseed': ['-rn', '--rnseed',
				   {'type': int,
					'default': random.randint(0,1000),
					'help': 'select random seed to start'
					}]
			}
		self.args_keys = [k for k in arg_options.keys()]
		self.len_gkeys = len(self.args_keys)

		return arg_options

	def check_limits(self):
		lims = {'size': (2, 51),
				'cell_density': (10, 90),
				'fdelay': (0.1, 1),
				'iters': (1, 1001),
				'rnseed':(0, 1000)
				}
		for k, v in lims.items():
			if (v[0] > self.arg_d[k]) or (self.arg_d[k] > v[1]):
				self.arg_d[k] = v[0]
				print(f'{k} was out of range, set to {v[0]}')

		return True


	def play_many_games(self):
		self.arg_d = vars(self.args_read)
		self.check_limits()
		arg_d = self.arg_d
		iters = arg_d.get('iters', 3)
		for i in range(iters):
			arg_d['rnseed'] = arg_d['rnseed'] + i
			if not arg_d.get('noanimation', False):
				g = self.play_a_game()
				print(f'iteration {i+1}')
				g.animation()
				self.log.append(g.log)
				self.collection.append(g)
				time.sleep(1)
			else:
				g = self.play_a_game()
				g.run_until_repeat()
				self.log.append(g.log)
				self.collection.append(g)

		self.print_report()

		return True

	def play_a_game(self):
		arg_d = self.arg_d
		g_keys = self.args_keys[:self.len_gkeys]
		g_args = {k: arg_d[k] for k in g_keys}

		g = game.Game(**g_args)

		return g

	def print_report(self):

		rep_keys = ['repeat_start', 'repeat_end', 'cells_last']
		df = pd.DataFrame(self.log)
		df = df[rep_keys]
		df['cycle_len'] = df['repeat_end'] - df['repeat_start']
		self.df = df
		print('summary:')
		print(df)

		return True



if __name__ == '__main__':
	p = Play()
	p.play_many_games()





