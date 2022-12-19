DEFAULT_NUM_OF_VARIANTS_TO_GEN = 350
NUM_OF_RANDOM_BLOCKS_TO_PLACE = 3  # overridden in the place_random_blocks_on_ground function

# ground level
GROUND_LEVEL = -3.5

# sky level (for inverse gravity)
SKY_LEVEL = 10
SKY_PLATFORM_Y_COORDINATE = 10.3

# reachable x range
X_MIN_REACHABLE = -9.960
X_MAX_REACHABLE = 9.397

# unreachable x range
X_MAX_UNREACHABLE = 17

# reachable space
X_LOW_REACHABLE = -10
X_HIGH_REACHABLE = 6
Y_LOW_REACHABLE = -3.4
Y_HIGH_REACHABLE = 4

# precision in the level file
rounding_digits = 4

# block sizes in the game (including novel objects)
blocks = {'SquareHole': [0.84, 0.84], 'RectFat': [0.85, 0.43], 'SquareSmall': [0.43, 0.43], 'SquareTiny': [0.22, 0.22],
		  'RectTiny': [0.43, 0.22], 'RectSmall': [0.85, 0.22],
		  'RectMedium': [1.68, 0.22], 'RectBig': [2.06, 0.22], 'TriangleHole': [0.82, 0.82], 'Triangle': [0.82, 0.82],
		  'Circle': [0.8, 0.8], 'CircleSmall': [0.45, 0.45],
		  'Platform': [0.64, 0.64], 'Magician': [4, 2], 'Wizard': [4, 4], 'Butterfly': [4, 4], 'Worm': [0.64, 0.64],
		  'novel_object_242': [0.64, 0.64], 'novel_object_245': [0.66, 0.66],
		  'novel_object_246': [0.66, 0.66], 'novel_object_253': [0.66, 0.66], 'SquareHanger': [1, 4],
		  'novel_object_255': [0.001, 0.001], 'novel_object_256': [0.64, 0.64], 'novel_object_257': [0.66, 0.66],
		  'novel_object_225': [6, 1], 'novel_object_222': [4, 3], 'novel_object_223': [4, 4],
		  'novel_object_224': [1, 1], 'novel_object_226': [1, 1], 'novel_object_227': [1.5, 1.5],
		  'novel_object_232': [2, 3],
		  'novel_object_233': [4, 2], 'novel_object_234': [4, 4], 'novel_object_235': [4, 4],
		  'novel_object_236': [0.64, 0.64], 'novel_object_237': [4, 4], 'novel_object_2': [2.06, 0.22],
		  'PinkPig': [0.47, 0.45], 'PinkMediumPig': [0.78, 0.76], 'PinkBigPig': [0.99, 0.97],
		  # novelty benchmark novelties start from here
		  'BasicBigFourShots': [0.99, 0.97], 'BasicBigTwoShots': [0.99, 0.97], 'PinkRectFat': [0.85, 0.43],
		  'PinkSquareHole': [0.84, 0.84], 'PinkCircle': [0.8, 0.8], 'Magnet': [8, 8], 'Fan': [0.77, 0.77],
		  # mangnet size considered the magnetic field area
		 # 'InverseAirTurbulence': [4.48, 6.4], 'NonNovelAirTurbulence': [4.48, 6.4], 'NovelAirTurbulence': [4.48, 6.4],
		  'InverseAirTurbulence': [0.64, 0.64], 'NonNovelAirTurbulence': [0.64, 0.64], 'NovelAirTurbulence': [0.64, 0.64],
		  'Storm': [0.01, 0.01], 'InverseGravity': [0.01, 0.01]  # storm size is zero
		  }

# block sizes in the game (excluding novel objects) - will be used as distraction objects
default_blocks = {'SquareHole': [0.84, 0.84], 'RectFat': [0.85, 0.43], 'SquareSmall': [0.43, 0.43],
				  'SquareTiny': [0.22, 0.22], 'RectTiny': [0.43, 0.22], 'RectSmall': [0.85, 0.22],
				  'RectMedium': [1.68, 0.22], 'RectBig': [2.06, 0.22], 'TriangleHole': [0.82, 0.82],
				  'Triangle': [0.82, 0.82], 'Circle': [0.8, 0.8], 'CircleSmall': [0.45, 0.45],
				  'Platform': [0.64, 0.64]}

# pigs sizes in the game
pigs = {'BasicSmall': [0.47, 0.45], 'BasicMedium': [0.78, 0.76], 'BasicBig': [0.99, 0.97],
		'novel_object_1': [0.47, 0.45], 'novel_object_2': [0.47, 0.45], 'novel_object_3': [0.47, 0.45],
		'novel_object_4': [0.47, 0.45], 'novel_object_254': [0.47, 0.45],
		'PinkPig': [0.47, 0.45], 'PinkMediumPig': [0.78, 0.76], 'PinkBigPig': [0.99, 0.97],
		'BasicBigFourShots': [0.99, 0.97], 'BasicBigTwoShots': [0.99, 0.97]}

# tnt size in the game
tnts = {'TNT': [0.66, 0.66]}

reachability_line = [[-6.51, 7.1], [-5.84, 6.91], [-5.274, 6.643], [-4.65, 6.544], [-4.037, 6.292], [-3.43, 5.96],
					 [-2.97, 5.82], [-2.48, 5.62], [-1.98, 5.37], [-1.385, 5.034],
					 [-0.86, 4.71], [-0.394, 4.413], [0.025, 4.229], [0.617, 3.94], [1.027, 3.66], [1.559, 3.266],
					 [2.025, 2.904], [2.63, 2.411], [3.293, 2.005], [3.97, 1.487],
					 [4.648, 1.039], [5.231, 0.489], [5.824, 0.004], [6.24, -0.453], [6.91, -1.005], [7.53, -1.574],
					 [7.999, -2.0], [8.496, -2.481], [8.996, -3.0183],
					 [9.459, -3.494]]
