import random
import copy
import math
import sys

from utils.constants import *
from utils.data_classes import *


class GenerateLevels:

	# check if the block is slanted
	def is_slanted_block(self, block):
		# the threshold degree by which the object's rotation is ignored
		slanting_threshold = 5

		if abs(block.rotation) < slanting_threshold or abs(block.rotation - 90) < slanting_threshold or abs(
				block.rotation - 180) < slanting_threshold or abs(block.rotation - 270) < slanting_threshold or abs(
			block.rotation - 360) < slanting_threshold or abs(block.rotation + 90) < slanting_threshold or abs(
			block.rotation + 180) < slanting_threshold or abs(block.rotation + 270) < slanting_threshold or abs(
			block.rotation + 360) < slanting_threshold:
			return False

		return True

	# check the rotation of the block and return the round offed rotation if not slanted
	def get_adjusted_block_rotation(self, block):
		# the threshold degree by which the object's rotation is ignored
		slanting_threshold = 5

		if self.is_slanted_block(block):
			return block.rotation
		else:
			rotation = abs(block.rotation)
			if rotation < slanting_threshold:
				return 0
			elif abs(block.rotation - 90) < slanting_threshold:
				return 90
			elif abs(block.rotation - 180) < slanting_threshold:
				return 180
			elif abs(block.rotation - 270) < slanting_threshold:
				return 270
			elif abs(block.rotation - 360) < slanting_threshold:
				return 360

	def get_horizontal_and_vertical_span(self, block_considered):
		# returns the horizontal and vertical span of a given object

		location_offset_x = 0.1  # used to reduce the horizontal span of the round blocks (which's base is not fully touched)

		horizontal_span_of_the_block = 0
		vertical_span_of_the_block = 0

		# print('block_considered', block_considered)
		# print('xxx', '<class \'__main__.Pig\'>' == str(type(block_considered)))
		# print('xxx', '<class \'__main__.Block\'>' == str(type(block_considered)))

		block_rotation = self.get_adjusted_block_rotation(block_considered)

		# if isinstance(block_considered, Block):
		if '<class \'utils.data_classes.Block\'>' == str(type(block_considered)):
			vertical_span_of_the_block = abs(
				(blocks[block_considered.type][0] * block_considered.scale_x) * math.sin(
					math.radians(block_rotation))) + abs(
				(blocks[block_considered.type][1] * block_considered.scale_y) * math.cos(
					math.radians(block_rotation)))
			horizontal_span_of_the_block = abs(
				(blocks[block_considered.type][0] * block_considered.scale_x) * math.cos(
					math.radians(block_rotation))) + abs(
				(blocks[block_considered.type][1] * block_considered.scale_y) * math.sin(
					math.radians(block_rotation)))
		# elif isinstance(block_considered, Pig):
		elif '<class \'utils.data_classes.Pig\'>' == str(type(block_considered)):
			vertical_span_of_the_block = abs(
				(pigs[block_considered.type][0]) * math.sin(math.radians(block_rotation))) + abs(
				(pigs[block_considered.type][1]) * math.cos(math.radians(block_rotation)))
			horizontal_span_of_the_block = abs(
				(pigs[block_considered.type][0]) * math.cos(math.radians(block_rotation))) + abs(
				(pigs[block_considered.type][1]) * math.sin(math.radians(block_rotation))) - location_offset_x
		elif '<class \'utils.data_classes.Tnt\'>' == str(type(block_considered)):
			vertical_span_of_the_block = abs(
				(tnts[block_considered.type][0]) * math.sin(math.radians(block_rotation))) + abs(
				(tnts[block_considered.type][1]) * math.cos(math.radians(block_rotation)))
			horizontal_span_of_the_block = abs(
				(tnts[block_considered.type][0]) * math.cos(math.radians(block_rotation))) + abs(
				(tnts[block_considered.type][1]) * math.sin(math.radians(block_rotation))) - location_offset_x
		else:
			print('Unknown Object!')

		return horizontal_span_of_the_block, vertical_span_of_the_block

	# returns the blocks which are cut by a horizontal line
	def find_blocks_which_cut_a_horizontal_line(self, template_data, line):
		selected_blocks = []
		selected_horizontal_intervals = []

		for game_object in template_data[0] + template_data[1] + template_data[2]:
			horizontal_span, vertical_span = self.get_horizontal_and_vertical_span(game_object)
			# print('vertical_span', game_object.type, game_object.y - vertical_span / 2, game_object.y + vertical_span / 2)
			# print('horizontal_span', game_object.type, game_object.x - horizontal_span / 2,game_object.x, game_object.y ,game_object.x + horizontal_span / 2)

			# check if the block lies on the line
			# print('line, min mid max', line, block.y - vertical_span / 2, block.y, block.y + vertical_span / 2)
			if game_object.y - vertical_span / 2 < line and line < game_object.y + vertical_span / 2:
				# print('added')
				selected_blocks.append(game_object)
				selected_horizontal_intervals.append(
					[game_object.x - horizontal_span / 2, game_object.x + horizontal_span / 2])

		return [selected_blocks, selected_horizontal_intervals]

	# returns the blocks which are cut by a vertical line
	def find_blocks_which_cut_a_vertical_line(self, template_data, line):
		selected_blocks = []
		selected_vertical_intervals = []
		for game_object in template_data[0] + template_data[1] + template_data[2]:
			horizontal_span, vertical_span = self.get_horizontal_and_vertical_span(game_object)

			# check if the block lies on the line
			# print('line, min mid max', line, block.y - vertical_span / 2, block.y, block.y + vertical_span / 2)
			if game_object.x - horizontal_span / 2 < line and line < game_object.x + horizontal_span / 2:
				selected_blocks.append(game_object)
				selected_vertical_intervals.append(
					[game_object.y - horizontal_span / 2, game_object.y + horizontal_span / 2])

		return [selected_blocks, selected_vertical_intervals]

	def get_occupied_x_spans_below_y_axis(self, template_data, y_axis):
		selected_blocks_x_spans = []
		for block in template_data[0] + template_data[1]:
			horizontal_span, vertical_span = self.get_horizontal_and_vertical_span(block)

			# check the vertical span is below the y_axis considered
			if block.y - vertical_span / 2 < y_axis:
				# save the covered x span
				selected_blocks_x_spans.append([block.x - horizontal_span / 2, block.x + horizontal_span / 2])

		return selected_blocks_x_spans

	def get_occupied_x_spans_above_y_axis(self, template_data, y_axis):
		# used only for placing objects on sky

		selected_blocks_x_spans = []
		for block in template_data[0] + template_data[1]:

			# skip the sky platform
			if abs(block.y - SKY_PLATFORM_Y_COORDINATE) < 0.01:
				# print('skipped sky platform')
				continue

			horizontal_span, vertical_span = self.get_horizontal_and_vertical_span(block)
			# check the vertical span is below the y_axis considered
			if block.y + vertical_span / 2 > y_axis:
				# save the covered x span
				selected_blocks_x_spans.append([block.x - horizontal_span / 2, block.x + horizontal_span / 2])

		return selected_blocks_x_spans

	def does_coordinate_overlap_ranges(self, coordinate, coordinate_ranges):
		for coordinate_range in coordinate_ranges:
			if coordinate_range[0] - 1.05 < coordinate < coordinate_range[
				1] + 1.05:  # 1.05 is the half-length of the longest block (rect big)
				return True
		return False

	def place_random_blocks(self, template_data, restricted_objects=None, restricted_areas=None, onWhere='ground'):
		# handle the default arguments
		if restricted_objects is None:
			restricted_objects = []
		if restricted_areas is None:
			restricted_areas = []

		# number of distraction objects
		NUM_OF_RANDOM_BLOCKS_TO_PLACE = random.randrange(1, 6)

		# place random blocks in the level
		for j in range(NUM_OF_RANDOM_BLOCKS_TO_PLACE):
			self.place_a_random_block(template_data, restricted_objects, restricted_areas, onWhere)

	def place_a_random_block(self, template_data, restricted_objects, restricted_x_areas, onWhere):

		# get a random distraction object (+ material)
		max_no_of_tries = 100
		no_of_tries = 0

		while True:
			random_block, random_block_size = random.choice(list(default_blocks.items()))
			random_block_material = random.choice(['ice', 'wood', 'stone'])

			if (random_block_material.lower() + ' ' + random_block.lower()) not in restricted_objects:
				break  # found a non restricted block and a material
			# else:
			# 	print('restricted distraction object: ' + random_block_material + ' ' + random_block + ' trying another object')

			no_of_tries += 1
			if no_of_tries > max_no_of_tries:
				print('could not find a feasible block + material')
				return False, template_data

		random_block_angle = 0

		y_coordinate = 0
		occupied_x_spans = []
		if onWhere == 'ground':
			y_coordinate = GROUND_LEVEL + random_block_size[1] / 2
			occupied_x_spans = self.get_occupied_x_spans_below_y_axis(template_data,
																	  -2.5)  # -2.5 is top y location of the tallest block (squarehole) when placed on ground
		elif onWhere == 'sky':
			y_coordinate = SKY_LEVEL - random_block_size[1] / 2
			occupied_x_spans = self.get_occupied_x_spans_above_y_axis(template_data,
																	  9.2)  # 9.2 is top y location of the tallest block (squarehole) when placed on ground

		# get blocks on the ground
		# blocks_on_ground = self.find_blocks_which_cut_a_horizontal_line(template_data, -3.39)

		# add the restricted areas as well
		occupied_x_spans += restricted_x_areas

		# print('occupied_x_spans', occupied_x_spans_on_ground)

		# randomly pick a x location that doesn't overlap with existing objects
		no_of_tries = 0
		x_coordinate = round(random.uniform(X_MIN_REACHABLE, X_MAX_REACHABLE), 5)
		while self.does_coordinate_overlap_ranges(x_coordinate, occupied_x_spans):
			x_coordinate = round(random.uniform(X_MIN_REACHABLE, X_MAX_REACHABLE), 5)
			no_of_tries += 1
			if no_of_tries > max_no_of_tries:
				print('could not find a feasible location on ground to place a block')
				return False, template_data

		# if successfully found a x coordinate add the new block to the template_data
		template_data[0].append(
			Block(0, random_block, random_block_material, x_coordinate, y_coordinate, random_block_angle))

		# print('placed a ', random_block_material, random_block, 'at', x_coordinate, y_coordinate)
		return True, template_data

	def get_reachable_x_location_using_reachability_line(self, x_min, x_max, y_location):

		# get the possible max x location considering the closest y
		y_coordinates = [row[1] for row in reachability_line]
		closest_y_on_reachability_line = min(y_coordinates, key=lambda y: abs(y - y_location))

		# get the possible max x location considering the closest y
		x_max_theoretical = reachability_line[y_coordinates.index(closest_y_on_reachability_line)][0]

		# if the theoretical value is lesser than the user given value, overwrite!
		if x_max_theoretical < x_max:
			x_max = x_max_theoretical

		# get a random x location in the feasible range
		random_x_location = round(random.uniform(x_min, x_max), 5)

		return random_x_location

	def get_reachable_location_using_reachability_line(self, x_min, x_max, y_min, y_max):
		# print('input', y_min, y_max)
		random_x_location, random_y_location = 0, 0
		while True:
			# get a random x location
			random_x_location = round(random.uniform(x_min, x_max), 5)

			# find the closest x location form the reachability line
			x_coordinates = [row[0] for row in reachability_line]
			closest_x_on_reachability_line = min(x_coordinates, key=lambda x: abs(x - random_x_location))

			# get the possible max y location considering the closest x
			y_max_theoretical = reachability_line[x_coordinates.index(closest_x_on_reachability_line)][1]
			# if the theoretical value is lesser than the user given value, overwrite!
			if y_max_theoretical < y_max:
				updated_y_max = y_max_theoretical
			else:
				updated_y_max = y_max

			# print('closest_x_on_reachability_line', closest_x_on_reachability_line)
			# print(y_min, updated_y_max)
			if y_min > updated_y_max:
				# print('updated_y_max', updated_y_max)
				print('y_locations are not feasible for the selected x location, retrying')
				continue

			random_y_location = round(random.uniform(y_min, updated_y_max), 5)
			break

		return random_x_location, random_y_location

	def get_location_in_reachability_line(self):

		# get a random x location
		random_x_location = round(random.uniform(reachability_line[0][0], reachability_line[-1][0]), 5)

		# find the closest x location form the reachability line
		x_coordinates = [row[0] for row in reachability_line]
		closest_x_on_reachability_line = min(x_coordinates, key=lambda x: abs(x - random_x_location))

		# get the y location considering the closest x
		y_location = reachability_line[x_coordinates.index(closest_x_on_reachability_line)][1]

		# print('random_x_location', random_x_location)
		# print('closest x', closest_x_on_reachability_line)
		# print('y_location', y_location)
		#
		return random_x_location, y_location

	def get_location_in_reachable_space(self, x_min, x_max, y_min, y_max):
		# select a random y location
		random_x_location = round(random.uniform(x_min, x_max), 5)

		# if x is larger than the middle point, reduce y_max to half
		if random_x_location > (x_min + (x_max - x_min) / 2):
			random_y_location = round(random.uniform(y_min, y_max), 5)
		else:
			random_y_location = round(random.uniform(y_min, y_min + (y_max - y_min) / 2), 5)

		return random_x_location, random_y_location

	def get_location_in_reachable_space_2(self, x_min, x_max, y_min, y_max):
		# select a random y location
		random_x_location = round(random.uniform(x_min, x_max), 5)

		# if x is larger than the middle point, reduce y_max to half
		if random_x_location > (x_min + (x_max - x_min) / 2):
			random_y_location = round(random.uniform(y_min, y_min + (y_max - y_min) / 2), 5)
		else:
			random_y_location = round(random.uniform(y_min, y_max), 5)

		return random_x_location, random_y_location

	def get_location_in_unreachable_space(self, x_min_unreachable, x_max_unreachable, y_min_reachable, y_max_reachable):
		# select a random y location
		random_y_location = round(random.uniform(y_min_reachable, y_max_reachable), 5)

		# if y is larger than the middle point, shift the x unreachable range
		if random_y_location > (y_min_reachable + (y_max_reachable - y_min_reachable) / 2):
			random_x_location = round(random.uniform(x_min_unreachable - 7, x_min_unreachable), 5)
		else:
			random_x_location = round(random.uniform(x_max_unreachable, x_min_unreachable), 5)

		return random_x_location, random_y_location

	def get_location_in_unreachable_space_2(self, x_min_unreachable, x_max_unreachable, y_min_reachable,
											y_max_reachable):
		# select a random y location
		random_y_location = round(random.uniform(y_min_reachable, y_max_reachable), 5)

		# if y is larger than the middle point, shift the x unreachable range
		if random_y_location > (y_min_reachable + (y_max_reachable - y_min_reachable) / 2):
			random_x_location = round(random.uniform(x_min_unreachable - 3, x_min_unreachable), 5)
		else:
			random_x_location = round(random.uniform(x_max_unreachable, x_min_unreachable), 5)

		return random_x_location, random_y_location

	def is_location_overlap_intervals(self, x_location, width_of_object, overlap_intervals):
		# convert the x location to screen coordinate
		# x_location = x_location - partitioner.level_width_min

		# print('platform_range: ', platform_range)
		# print('x_location: ', x_location)
		for platform_span in overlap_intervals:
			# if (platform_span[0] - width_of_object / 2) < x_location < (platform_span[1] + width_of_object / 2):
			if ((x_location - width_of_object / 2) < platform_span[1]) and (
					(x_location + width_of_object / 2) > platform_span[0]):
				return True

		return False

	def get_a_random_location_on_screen(self, template_data):
		# x_location = round(random.uniform(-3, 10), rounding_digits)
		# y_location = round(random.uniform(-2, 6), rounding_digits)

		# boundaries in the screen to instantiate (reachable to bird space)
		x_min = -6.5
		x_max = 2
		y_min = -2.4
		y_max = 4

		x_location = -100
		y_location = -100
		location_found = False

		# for wizard
		width_of_object = 4  # (including space to move)
		height_of_object = 4  # (including space to move)

		location_finding_retries = 0
		while not location_found:
			x_location = round(random.uniform(x_min, x_max), rounding_digits)
			y_location = round(random.uniform(y_min, y_max), rounding_digits)

			# get the objects cut the vertical x_location line and their vertical intervals
			objects_vertical_intervals = self.find_blocks_which_cut_a_vertical_line(template_data, x_location)[1]

			# try placing the object skipping the used vertical spaces
			no_of_y_retries = 0
			while self.is_location_overlap_intervals(y_location, height_of_object, objects_vertical_intervals):
				no_of_y_retries += 1
				y_location = round(random.uniform(y_min, y_max), rounding_digits)

				# if no location is found after 100 reties, exit
				if no_of_y_retries > 100:
					y_location = -100
					location_found = False

			if y_location == -100:  # couldn't find a feasible y location, try from beginning
				continue

			# get the objects that cut the horizontal y_location line and their horizontal intervals
			objects_horizontal_intervals = self.find_blocks_which_cut_a_horizontal_line(template_data, y_location)[1]

			# try placing the object skipping the used spaces
			no_of_x_retries = 0
			while self.is_location_overlap_intervals(x_location, width_of_object, objects_horizontal_intervals):
				no_of_x_retries += 1
				x_location = round(random.uniform(x_min, x_max), rounding_digits)

				# if no location is found after 100 reties, exit
				if no_of_x_retries > 100:
					x_location = -100
					location_found = False

			if x_location != -100:  # feasible x location found
				location_found = True
			elif location_finding_retries > 100:  # couldn't find a feasible x,y pair
				break
			location_finding_retries += 1

		return [x_location, y_location]

	def get_a_random_location_inside_platform(self, all_blocks):
		# for the worm novelty returns a location of a platform above the ground

		# for game_object in all_blocks[::-1]:  # traverse in reverse order
		for game_object in all_blocks:
			if game_object.type == 'Platform':
				if game_object.y > -3:  # only consider platforms above the ground
					if game_object.rotation == 0 and game_object.scale_x > 1:
						return [game_object.x, game_object.y]
					elif game_object.rotation == 90 and game_object.scale_y > 1:
						return [game_object.x, game_object.y]

		return [-100, -100]  # no feasible locations inside the platforms

	def get_a_random_location_at_ground(self, template_data):
		# y location when placing the object on the ground (obtained from placing the object on the ground from the editor)
		# y_location = -3.0505  # helmet pig
		# y_location = -2.764278 # king pig
		# y_location = -3.198051  # egg block
		# y_location = -3.192686  # TNTegg block
		# y_location = -3.268649  # TNTegg block
		# y_location = -3.274892  # pig small
		y_location = -2.829256  # magician

		# width_of_object = 0.47  # pig small
		# width_of_object = 0.45  # egg block
		width_of_object = 4  # magician (including space to move)

		# get the objects that are on the ground and their horizontal intervals (-3.37 is the shortest block that can be on the ground)
		objects_cut_the_line, objects_horizontal_intervals = self.find_blocks_which_cut_a_horizontal_line(template_data,
																										  -3.37)
		# print('objects_cut_the_line', objects_cut_the_line)

		# get a random x location for the new object
		x_location = round(random.uniform(-5, 9), rounding_digits)

		# try placing the object skipping the used spaces
		no_of_retries = 0
		while self.is_location_overlap_intervals(x_location, width_of_object, objects_horizontal_intervals):
			no_of_retries += 1
			x_location = round(random.uniform(-5, 9), rounding_digits)

			# if no location is found after 100 reties, exit
			if no_of_retries > 100:
				x_location = -100

		return [x_location, y_location]

	def get_a_random_location_for_butterfly(self, template_data):
		y_location = -2.84

		# the butterfly can only be instantiated at either ends (on ground) of the convex hull of all the objects in the level
		min_x_level_space = -10
		max_x_level_space = 9

		min_x_occupied = 100
		max_x_occupied = -100
		# find the min and max x locations occupied by the game objects
		for game_object in template_data[0] + template_data[1] + template_data[2]:
			if game_object.x < min_x_occupied:
				min_x_occupied = game_object.x - self.get_horizontal_and_vertical_span(game_object)[0] / 2
			if game_object.x > max_x_occupied:
				max_x_occupied = game_object.x + self.get_horizontal_and_vertical_span(game_object)[0] / 2

		# adjust the width of the butterfly from min and max values
		min_x_occupied -= 0.5
		max_x_occupied += 0.5

		if min_x_occupied < min_x_level_space and max_x_occupied < max_x_level_space:  # rightmost is feasible
			random_x_location = random.uniform(max_x_occupied, max_x_level_space)
		elif min_x_occupied > min_x_level_space and max_x_occupied > max_x_level_space:  # leftmost is feasible
			random_x_location = random.uniform(min_x_level_space, min_x_occupied)
		elif min_x_occupied < min_x_level_space and max_x_occupied < max_x_level_space:  # no feasible locations
			return [-100, -100]
		else:  # both leftmost and rightmost are feasible - select randomly
			if random.choice([True, False]):
				random_x_location = random.uniform(min_x_level_space, min_x_occupied)
			else:
				random_x_location = random.uniform(max_x_occupied, max_x_level_space)

		return [random_x_location, y_location]

	def add_an_external_agent(self, template_data, agent_index):

		location = [-100, -100]
		external_agent = ''
		external_agent_added = False
		attempts_tried_to_add_external_agent = 0
		max_attempts_to_add_external_agent = 100

		while not external_agent_added:

			# randomly select an external agent to add
			# external_agent_index = random.choice([1, 2, 3, 4])
			external_agent_index = agent_index

			if external_agent_index == 0:  # no external agent
				print('no external agent added')
				return True
			if external_agent_index == 1:  # magician
				external_agent = 'Magician'
				location = self.get_a_random_location_at_ground(template_data)
			# todo: only the ground is checked for the feasibility, add checks for the highest point of the magician as well
			elif external_agent_index == 2:  # wizard
				external_agent = 'Wizard'
				location = self.get_a_random_location_on_screen(template_data)
			elif external_agent_index == 3:  # butterfly
				external_agent = 'Butterfly'
				location = self.get_a_random_location_for_butterfly(template_data)
			elif external_agent_index == 4:  # worm
				external_agent = 'Worm'
				location = self.get_a_random_location_inside_platform(template_data[0])

			if location[0] == -100:  # couldn't find a feasible location for the object
				attempts_tried_to_add_external_agent += 1

				if attempts_tried_to_add_external_agent > max_attempts_to_add_external_agent:
					print('could not find a feasible location for the external agent ', external_agent)
					return False

				continue

			print('added external agent ', external_agent)
			external_agent_added = True

		# if successfully found a location add the external agent to the template_data
		template_data[0].append(Block(0, external_agent, '', location[0], location[1], 0))

		return True

	def default_template(self, template_data, external_agent_index):

		# reachable_point = point that needs to be reachable
		# random_x, random_y = reachable location for the reachable_point

		# values for the 24M novelties - in novel, non-novel order

		# L3T9		change unit of coordinates 00001_1_0_9_3
		# reachable_point = [-6.98017, -1.438739]
		# random_x, random_y = self.get_reachable_location_using_reachability_line(-7.420167,	1.400001,	-2.798646,	2.409992)
		reachable_point = [-6.98017, -1.438739]
		random_x, random_y = self.get_reachable_location_using_reachability_line(-7.420167, 1.400001, -2.798646,
																				 2.409992)

		shift_x_value = reachable_point[0] - random_x
		shift_y_value = reachable_point[1] - random_y

		# shift the pigs
		for pig in template_data[1]:
			pig.x -= shift_x_value
			pig.y -= shift_y_value

		# shift the other blocks and platforms
		for block in template_data[0]:
			block.x -= shift_x_value
			block.y -= shift_y_value

		# shift TNTs
		for tnt in template_data[2]:
			tnt.x -= shift_x_value
			tnt.y -= shift_y_value

		# place distraction objects
		self.place_random_blocks(template_data, [])

		# place a random external agent
		external_agent_added = self.add_an_external_agent(template_data, external_agent_index)

		# if an external agent could not be added retun null
		if external_agent_added:
			return template_data
		else:
			print("External agent adding failed!")
			return None

	# def add_a_pig_and_a_bird(self, template_data):
	#
	#     # number of pigs/birds needed to add
	#     NUM_OF_RANDOM_PIGS_AND_BIRDS = random.randrange(1, 3)
	#
	#     # add the birds
	#     for i in range(NUM_OF_RANDOM_PIGS_AND_BIRDS):
	#         template_data[3].append(Bird("BirdRed"))
	#
	#     # add the pigs in the free and reachable space
	#     for j in range(NUM_OF_RANDOM_BLOCKS_TO_PLACE):
	#         self.place_a_random_block_on_ground(template_data, restricted_areas)

	def shift_objects(self, template_data, shift_x_value, shift_y_value):
		# shift the pigs
		for pig in template_data[1]:
			pig.x -= shift_x_value
			pig.y -= shift_y_value

		# shift the other blocks and platforms
		for block in template_data[0]:
			block.x -= shift_x_value
			block.y -= shift_y_value

	# shift TNTs if necessary

	def num_of_variants_to_generate(self):
		# rewrite the NUM_OF_VARIANTS_TO_GEN from the user input
		try:
			num_of_variants = int(sys.argv[1])
			print('user given number of tasks to generate: ', num_of_variants)
		except:
			print('default number of tasks to generate: ', DEFAULT_NUM_OF_VARIANTS_TO_GEN)
			num_of_variants = DEFAULT_NUM_OF_VARIANTS_TO_GEN

		return num_of_variants

	def variation_generation_schema(self, template_name, template_data, ref_point, min_coordinate, max_coordinate,
									restricted_objects):
		# print('ref_point: ', ref_point)
		# print('min_coordinate: ', min_coordinate)
		# print('max_coordinate: ', max_coordinate)

		# validate config data
		# bounds shouldn't be empty (nan values)
		# if ~(all(i == i for i in ref_point) &  all(i == i for i in min_coordinate) & all(i == i for i in max_coordinate)):
		# 	raise Exception("ref_point or min_coordinate or max_coordinate contains nan values")

		# min_coordinate values should be lesser than the max_coordinate values
		if (min_coordinate[0] > max_coordinate[0]) or (min_coordinate[1] > max_coordinate[1]):
			raise Exception("Error with the bounds: min is larger than the max!")

		# get a random location x and y locations
		random_x = round(random.uniform(min_coordinate[0], max_coordinate[0]), 2)
		random_y = round(random.uniform(min_coordinate[1], max_coordinate[1]), 2)

		# calculate the shift values needed for the
		shift_x_value = ref_point[0] - random_x
		shift_y_value = ref_point[1] - random_y

		# shift the game objects
		self.shift_objects(template_data, shift_x_value, shift_y_value)

		# add distraction objects

		if template_name.split('_')[2][3] == '6':  # special case -- inverse gravity novelty
			# for both novel and non-novel, add the sky platform
			template_data[0].append(Block(0, 'Platform', '', 0, SKY_PLATFORM_Y_COORDINATE, 0, scale_x=55, scale_y=1))
			if (template_name.split('_')[3] == '6'):  # for novel add the distractions on the sky
				self.place_random_blocks(template_data, restricted_objects=restricted_objects, onWhere='sky')
			else:  # for non novelty add the distractions to the ground
				self.place_random_blocks(template_data, restricted_objects=restricted_objects)

		else:  # all the other novelties
			self.place_random_blocks(template_data, restricted_objects=restricted_objects)

		return template_data

	def generate_levels_from_template(self, template_name, template_data, config_data):

		print('template considered: ', template_name)
		print('template data: ', template_data)
		print('config data: ', config_data)

		generated_levels = []

		for i in range(self.num_of_variants_to_generate()):
			print('generating task', i + 1)

			generated_levels.append(
				self.variation_generation_schema(template_name, copy.deepcopy(template_data), config_data[0],
												 config_data[1], config_data[2], config_data[3]))

		# print('generated_levels: ', generated_levels)
		print('total generated_levels: ', len(generated_levels))
		return generated_levels
