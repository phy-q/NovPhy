def template_1_1_1(self, template_data):
    # only x axis can be changed, pig should be within the reachable range
    for pig in template_data[1]:
        # generate a random x location with the reachable range
        # random_x_location = round(random.uniform(X_MIN_REACHABLE, X_MAX_REACHABLE), 5)
        random_x_location = self.get_reachable_x_location_using_reachability_line(X_MIN_REACHABLE, X_MAX_REACHABLE, -3.263795)
        pig.x = random_x_location

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_1_1_2(self, template_data):
    # generate a random x and y location within the reachable range for the pig
    random_x, random_y = self.get_reachable_location_using_reachability_line(-7, X_HIGH_REACHABLE, -2.829752, Y_HIGH_REACHABLE)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


# def template_1_1_5(self, template_data):
# 	# generate a random x and y location within the reachable range for the pig
# 	random_x, random_y = self.get_location_in_reachable_space(X_LOW_REACHABLE + 1.5, X_HIGH_REACHABLE - 1.5, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE - 1.5)
# 	shift_x_value = 0
# 	shift_y_value = 0
#
# 	# place the pig in the random location
# 	for pig in template_data[1]:
# 		shift_x_value = pig.x - random_x
# 		shift_y_value = pig.y - random_y
# 		pig.x = random_x
# 		pig.y = random_y
#
# 	# adjust the platform to the pig's location
# 	for block in template_data[0]:
# 		block.x -= shift_x_value
# 		block.y -= shift_y_value
#
# 	self.place_random_blocks_on_ground(template_data, [])
# 	return template_data

def template_1_2_1(self, template_data):
    # only x axis can be changed, pig should be within the reachable range
    for pig in template_data[1]:
        # generate a random x location with the reachable range
        random_x_location = round(random.uniform(X_MIN_REACHABLE + 1, X_MAX_REACHABLE - 1), 5)
        pig.x = random_x_location

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_1_2_2(self, template_data):
    # generate a random x and y location within the reachable range for the pig
    random_x, random_y = self.get_location_in_reachable_space(X_LOW_REACHABLE + 2, X_HIGH_REACHABLE - 2, Y_LOW_REACHABLE + 2, Y_HIGH_REACHABLE - 2)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_1_2_5(self, template_data):
    # generate a random x and y location within the reachable range for the pig
    random_x, random_y = self.get_location_in_reachable_space(X_LOW_REACHABLE + 5, X_HIGH_REACHABLE - 1.5, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE - 1.5)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_1_1_6(self, template_data):
    # generate a random x and y location within the reachable range for the pig
    random_x, random_y = self.get_reachable_location_using_reachability_line(X_LOW_REACHABLE + 5, X_HIGH_REACHABLE - 5, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE - 4)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_1_1(self, template_data):
    # only x axis can be changed, pig should be within the unreachable range
    for pig in template_data[1]:
        # generate a random x location with the reachable range
        random_x_location = round(random.uniform(X_MAX_REACHABLE + 1, X_MAX_UNREACHABLE), 5)
        pig.x = random_x_location

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_1_2(self, template_data):
    # generate a random x and y location within the unreachable range for the pig
    random_x, random_y = self.get_location_in_unreachable_space(X_MAX_REACHABLE + 1, X_MAX_REACHABLE + 5, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_1_4(self, template_data):
    shift_x_value = 0

    # only x axis can be changed, pig should be within the unreachable range
    for pig in template_data[1]:
        # generate a random x location with the reachable range
        random_x_location = round(random.uniform(X_MAX_REACHABLE + 1, X_MAX_UNREACHABLE), 5)
        shift_x_value = pig.x - random_x_location
        pig.x = random_x_location

    # adjust the ball's x location
    for block in template_data[0]:
        block.x -= shift_x_value

    self.place_random_blocks_on_ground(template_data, [[-3, X_MAX_REACHABLE]])
    return template_data


def template_2_1_5(self, template_data):
    # generate a random x and y location within the unreachable range for the pig
    random_x, random_y = self.get_location_in_unreachable_space(X_MAX_REACHABLE + 2, X_MAX_REACHABLE + 1, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_1_6(self, template_data):
    # generate a random x and y location within the unreachable range for the pig
    random_x, random_y = self.get_location_in_unreachable_space_2(X_MAX_REACHABLE, X_MAX_REACHABLE + 3, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE - 5)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_1_7(self, template_data):
    shift_x_value = 0

    # only x axis can be changed, pig should be within the reachable range
    for pig in template_data[1]:
        # generate a random x location with the reachable range
        random_x_location = round(random.uniform(X_MIN_REACHABLE + 6, X_MAX_REACHABLE), 5)
        shift_x_value = pig.x - random_x_location
        pig.x = random_x_location

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_1_8(self, template_data):
    # generate a random x and y location
    random_x, random_y = self.get_location_in_reachable_space(X_MIN_REACHABLE + 5, X_MAX_REACHABLE - 3, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE - 2)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_1_9(self, template_data):
    # generate a random x and y location
    random_x, random_y = self.get_location_in_reachable_space(X_MIN_REACHABLE + 5, X_MAX_REACHABLE, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE - 5)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_2_1(self, template_data):
    # point that needs to be reachable (big rock circle)
    reachable_point = [-5.31003, -0.7899181]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-8.747027, 1.549163, -0.5899642, 1.23003)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_2_2(self, template_data):
    # generate a random x and y location
    random_x, random_y = self.get_location_in_reachable_space_2(X_MIN_REACHABLE + 5, X_MAX_REACHABLE - 7, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE - 3)
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_2_8(self, template_data):
    # generate a random x and y location
    random_x, random_y = self.get_location_in_reachable_space_2(X_MIN_REACHABLE + 5, X_MAX_REACHABLE - 7, Y_LOW_REACHABLE + 1, Y_HIGH_REACHABLE - 3)
    shift_x_value = 0
    shift_y_value = 0

    # place the first pig in the random location
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y
        break

    # second pig
    template_data[1][1].x -= shift_x_value
    template_data[1][1].y -= shift_y_value

    # adjust the platform to the pig's location
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_3_1(self, template_data):
    # point that needs to be reachable (square hole)
    reachable_point = [2.44, 1.71176]

    # place the square hole in the reachability line
    random_x, random_y = self.get_location_in_reachability_line()

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # for block in template_data[0]:
    # 	if block.type == 'SquareHole':
    # 		shift_x_value = block.x - random_x
    # 		shift_y_value = block.y - random_y
    # 		block.x = random_x
    # 		block.y = random_y

    # shift the platform and pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_3_2(self, template_data):
    # point that needs to be reachable (square hole)
    reachable_point = [-5.59846, 1.02442]

    # place the square hole in a reachable location
    random_x, random_y = self.get_reachable_location_using_reachability_line(X_MIN_REACHABLE + 5, X_MAX_REACHABLE, Y_LOW_REACHABLE + 1, 100)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift all the objects
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    # for block in template_data[0]:
    # 	if block.type == 'SquareHole':
    # 		shift_x_value = block.x - random_x
    # 		shift_y_value = block.y - random_y
    # 		block.x = random_x
    # 		block.y = random_y
    #
    # # shift the platform and pig
    # for pig in template_data[1]:
    # 	pig.x -= shift_x_value
    # 	pig.y -= shift_y_value
    #
    # for block in template_data[0]:
    # 	if block.type == 'Platform':
    # 		block.x -= shift_x_value
    # 		block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_3_3(self, template_data):
    shift_x_value = 0

    # only x axis can be changed, pig should be within the unreachable range
    for pig in template_data[1]:
        # generate a random x location with the reachable range
        random_x_location = round(random.uniform(X_MAX_REACHABLE + 1, X_MAX_UNREACHABLE - 4), 5)
        shift_x_value = pig.x - random_x_location
        pig.x = random_x_location

    # adjust the block's x location
    for block in template_data[0]:
        block.x -= shift_x_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_3_4(self, template_data):
    shift_x_value = 0

    # only x axis can be changed
    for pig in template_data[1]:
        # generate a random x location with the reachable range
        random_x_location = round(random.uniform(X_MIN_REACHABLE + 3, X_MAX_REACHABLE), 5)
        shift_x_value = pig.x - random_x_location
        pig.x = random_x_location

    # adjust other objects
    for block in template_data[0]:
        block.x -= shift_x_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_3_5(self, template_data):
    # point that needs to be reachable (wood hole)
    reachable_point = [-1.51509, -1.64602]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(X_MIN_REACHABLE + 5, X_MAX_REACHABLE, Y_LOW_REACHABLE + 2, 100)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    # # place the square hole in a reachable location
    # random_x, random_y = self.get_reachable_location_using_reachability_line(X_MIN_REACHABLE + 5, X_MAX_REACHABLE, Y_LOW_REACHABLE + 2, 100)
    # for block in template_data[0]:
    # 	if block.type == 'SquareHole':
    # 		shift_x_value = block.x - random_x
    # 		shift_y_value = block.y - random_y
    # 		block.x = random_x
    # 		block.y = random_y
    #
    # # shift the platform and pig
    # for pig in template_data[1]:
    # 	pig.x -= shift_x_value
    # 	pig.y -= shift_y_value
    #
    # for block in template_data[0]:
    # 	if block.type == 'Platform':
    # 		block.x -= shift_x_value
    # 		block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_4_1(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in a reachable location
    random_x, random_y = self.get_reachable_location_using_reachability_line(X_MIN_REACHABLE + 5, 0, Y_LOW_REACHABLE + 2, 4)
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # shift the platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_4_3(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in a reachable location
    random_x, random_y = self.get_reachable_location_using_reachability_line(X_MIN_REACHABLE + 5, 0, Y_LOW_REACHABLE + 2, 2)
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # shift the platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_4_4(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in a reachable location
    random_x, random_y = self.get_reachable_location_using_reachability_line(X_MIN_REACHABLE + 5, X_MAX_REACHABLE - 5, Y_LOW_REACHABLE + 2, 1)
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # shift the platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_2_4_6(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the pig in a reachable location
    random_x, random_y = self.get_reachable_location_using_reachability_line(X_MIN_REACHABLE + 5, 0, Y_LOW_REACHABLE + 2, 0)
    for pig in template_data[1]:
        shift_x_value = pig.x - random_x
        shift_y_value = pig.y - random_y
        pig.x = random_x
        pig.y = random_y

    # shift the platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_1_1(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the stone square-hole in a reachable place
    random_x, random_y = self.get_reachable_location_using_reachability_line(-7.5, 5, 2.3, 5.3)
    for block in template_data[0]:
        if block.material == 'stone' and block.type == 'SquareHole':
            shift_x_value = block.x - random_x
            shift_y_value = block.y - random_y
            block.x = random_x
            block.y = random_y

    # shift the platforms and the wood block
    for block in template_data[0]:
        if not (block.material == 'stone' and block.type == 'SquareHole'):
            block.x -= shift_x_value
            block.y -= shift_y_value

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_1_2(self, template_data):
    # point that needs to be reachable ( wood square hole)
    reachable_point = [3.48, 1.410032]

    # place the square hole in a reachable location
    random_x, random_y = self.get_reachable_location_using_reachability_line(3.3, 3.5, 1.47, 3.3)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift all the objects
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    # # place the wood square-hole in a reachable place
    # random_x, random_y = self.get_reachable_location_using_reachability_line(3.3, 3.5, 1.47, 3.3)
    # for block in template_data[0]:
    # 	if block.material == 'wood' and block.type == 'SquareHole':
    # 		shift_x_value = block.x - random_x
    # 		shift_y_value = block.y - random_y
    # 		block.x = random_x
    # 		block.y = random_y
    #
    # # shift the platforms and the stone block
    # for block in template_data[0]:
    # 	if not (block.material == 'wood' and block.type == 'SquareHole'):
    # 		block.x -= shift_x_value
    # 		block.y -= shift_y_value
    #
    # # shift the pig
    # for pig in template_data[1]:
    # 	pig.x -= shift_x_value
    # 	pig.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_1_3(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the small stone ball in a reachable place
    random_x, random_y = self.get_reachable_location_using_reachability_line(-7, 0, 2.3, 4)
    for block in template_data[0]:
        if block.type == 'CircleSmall' and block.material == 'stone':
            shift_x_value = block.x - random_x
            shift_y_value = block.y - random_y
            block.x = random_x
            block.y = random_y

    # shift the platforms and the stone block
    for block in template_data[0]:
        if not (block.type == 'CircleSmall' and block.material == 'stone'):
            block.x -= shift_x_value
            block.y -= shift_y_value

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_1_4(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the small stone ball in a reachable place
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5, 0, 0.3, 4)
    for block in template_data[0]:
        if block.type == 'CircleSmall' and block.material == 'stone':
            shift_x_value = block.x - random_x
            shift_y_value = block.y - random_y
            block.x = random_x
            block.y = random_y

    # shift the platforms and the stone block
    for block in template_data[0]:
        if not (block.type == 'CircleSmall' and block.material == 'stone'):
            block.x -= shift_x_value
            block.y -= shift_y_value

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_1_6(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the wood hole block in a reachable place
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5, 0, -0.5, 2)
    for block in template_data[0]:
        if block.material == 'wood' and block.type == 'SquareHole':
            shift_x_value = block.x - random_x
            shift_y_value = block.y - random_y
            block.x = random_x
            block.y = random_y

    # shift the platforms and the stone block
    for block in template_data[0]:
        if not (block.material == 'wood' and block.type == 'SquareHole'):
            block.x -= shift_x_value
            block.y -= shift_y_value

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_2_1(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # place the RectBig in the reachability line
    random_x, random_y = self.get_location_in_reachability_line()
    for block in template_data[0]:
        if block.type == 'RectBig':
            shift_x_value = block.x - random_x
            shift_y_value = block.y - random_y
            block.x = random_x
            block.y = random_y

    # shift the other blocks
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    for block in template_data[0]:
        if not (block.type == 'RectBig'):
            block.x -= shift_x_value
            block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_2_2(self, template_data):
    # place the higher stone hole block in a reachable place, y axis can not be changed (too high)
    random_x = self.get_reachable_x_location_using_reachability_line(-8, X_MAX_REACHABLE, 4.27)

    # find the higher stone hole block
    higher_stone_block = Block(0, '', '', 0.0, 0.0, 0.0)
    for block in template_data[0]:
        if block.material == 'stone' and block.type == 'SquareHole':
            if block.y > higher_stone_block.y:
                higher_stone_block = block

    # shift it to the selected random palce
    shift_x_value = higher_stone_block.x - random_x
    higher_stone_block.x = random_x

    # shift the other blocks and platforms
    for block in template_data[0]:
        if block.identifier != higher_stone_block.identifier:
            block.x -= shift_x_value

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_2_3(self, template_data):
    # place the lower stone hole block in a reachable place, y axis can not be changed (too high)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-6, X_MAX_REACHABLE, 0.9341, Y_HIGH_REACHABLE)

    # find the higher stone hole block
    lower_stone_block = Block(0, '', '', 0.0, 100.0, 0.0)
    for block in template_data[0]:
        if block.material == 'stone' and block.type == 'SquareHole':
            if block.y < lower_stone_block.y:
                lower_stone_block = block

    # print('lower_stone_block', lower_stone_block)
    # shift it to the selected random place
    shift_x_value = lower_stone_block.x - random_x
    shift_y_value = lower_stone_block.y - random_y
    lower_stone_block.x = random_x
    lower_stone_block.y = random_y

    # shift the other blocks and platforms
    for block in template_data[0]:
        if block.identifier != lower_stone_block.identifier:
            block.x -= shift_x_value
            block.y -= shift_y_value

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_2_4(self, template_data):
    # bouncing platform should be reachable from lower trajectory
    random_x, random_y = self.get_reachable_location_using_reachability_line(-2, 2.6, -0.97782, 1.3)

    # find the bouncing platform (platform with highest x)
    bouncing_platform = Block(0, '', '', -100.0, 0.0, 0.0)
    for block in template_data[0]:
        if block.type == 'Platform':
            if block.x > bouncing_platform.x:
                bouncing_platform = block

    # shift it to the selected random place
    shift_x_value = bouncing_platform.x - random_x
    shift_y_value = bouncing_platform.y - random_y
    bouncing_platform.x = random_x
    bouncing_platform.y = random_y

    # shift the other blocks and platforms
    for block in template_data[0]:
        if block.identifier != bouncing_platform.identifier:
            block.x -= shift_x_value
            block.y -= shift_y_value

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_3_1(self, template_data):
    # point that needs to be reachable (wide opening)
    reachable_point = [-4.89, 0.95]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(X_MIN_REACHABLE + 3, X_MAX_REACHABLE, 0.95, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_3_2(self, template_data):
    # point that needs to be reachable (big rock circle)
    reachable_point = [-6.21018, 2.18042]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-9.850999, X_MAX_REACHABLE, 3.319321, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_3_3(self, template_data):
    # point that needs to be reachable (wide opening)
    reachable_point = [-0.986, 2.635]

    # get a reachable location for the reachable point (reachable_point should be in the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5, X_MAX_REACHABLE, -0.97, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_3_4(self, template_data):
    # point that needs to be reachable (wide opening)
    reachable_point = [-0.831, 2.684]

    # get a reachable location for the reachable point (reachable_point should be in the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5, X_MAX_REACHABLE, -0.363, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_4_1(self, template_data):
    # point that needs to be reachable (wide opening)
    reachable_point = [2.25871, 1.39156]

    # get a reachable location for the reachable point (reachable_point should be in the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-7.94429, X_MAX_REACHABLE, 1.39156, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_4_2(self, template_data):
    # point that needs to be reachable (wood triangle)
    reachable_point = [-6.912, 1.2258]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-8.729, X_MAX_REACHABLE, 1.2258, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_4_3(self, template_data):
    # point that needs to be reachable (ice triangle)
    reachable_point = [-4.795, -1.19961]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-7.485002, X_MAX_REACHABLE, -1.19961, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_4_4(self, template_data):
    # point that needs to be reachable (edge of the upper stone block)
    reachable_point = [-5.048, 1.88]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-8, -4, 1.88, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_5_1(self, template_data):
    # point that needs to be reachable (furthest pig)
    reachable_point = [2.820013, 1.026101]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-0.89, X_MAX_REACHABLE, -0.7995539, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_5_2(self, template_data):
    # point that needs to be reachable (top antenne point)
    reachable_point = [-2.4, 5.8]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-6.45, X_MAX_REACHABLE, 3.68, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_5_3(self, template_data):
    # point that needs to be reachable (topmost pig)
    reachable_point = [-3.379822, -2.420288]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-6, 1.558355, -0.9386116, 1.5)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_5_4(self, template_data):
    # point that needs to be reachable (pig in the bucket)
    reachable_point = [-6.1519, -2.8896]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-6.1519, 4, -3.174598, 0.3)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_5_5(self, template_data):
    # point that needs to be reachable (topmost pig)
    reachable_point = [-1.20842, 2.02951]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-3.914959, X_MAX_REACHABLE, 2.02951, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_6_1(self, template_data):
    # point that needs to be reachable (left ice block)
    reachable_point = [-3.709073, -2.15922]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-7.66196, X_MAX_REACHABLE, -2.417462, Y_HIGH_REACHABLE - 2)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_6_2(self, template_data):
    # point that needs to be reachable (pig)
    reachable_point = [1.79002, -2.535197]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5.311675, -2.535197, -2.535197, -1.0)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_6_3(self, template_data):
    # point that needs to be reachable (right most pig)
    reachable_point = [-2.219439, -0.03752904]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5.379386, -0.03903953, -0.03752904, 0.29331)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_6_4(self, template_data):
    # point that needs to be reachable (top most pig)
    reachable_point = [-3.399167, 0.2950496]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-4.354696, 1.563726, 0.2950496, 1.565926)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_6_5(self, template_data):
    # point that needs to be reachable (right most pig)
    reachable_point = [-2.170179, -1.350999]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-4.354696, -1.353722, -1.350999, 0.4000222)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_6_6(self, template_data):
    # point that needs to be reachable (right most pig)
    reachable_point = [-2.221663, -0.5047105]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-7.040801, -0.7267894, -1.064094, 0.5543331)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_6_7(self, template_data):
    # point that needs to be reachable (right most pig)
    reachable_point = [-2.384823, -0.1313629]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5.755874, 5.775358, -0.575754, 1.737329)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_7_1(self, template_data):
    # point that needs to be reachable (pig)
    reachable_point = [-1.11452, 0.0996229]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-4.312766, X_MAX_REACHABLE, 0.7, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_7_2(self, template_data):
    # point that needs to be reachable (pig)
    reachable_point = [-0.1495501, 0.7360905]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-4.70958, 4.69, 0.7360905, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_7_3(self, template_data):
    # point that needs to be reachable (pig)
    reachable_point = [-0.09999022, 0.3341722]

    # get a reachable location for the reachable point (should be the lower trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-4.70958, 4.69, 0.3341722, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_7_4(self, template_data):
    # point that needs to be reachable (stone ball)
    reachable_point = [-3.74237, 2.16261]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-9.347918, X_MAX_REACHABLE - 2, 2.16261, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_7_5(self, template_data):
    # point that needs to be reachable (stone ball)
    reachable_point = [-3.06, 4.45124]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-7.828814, X_MAX_REACHABLE - 5, 3.999, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_8_1(self, template_data):
    # only add distract objects for the correct timing levels
    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_9_1(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # pig should be within the unreachable range
    for pig in template_data[1]:
        # generate a random x location with the unreachable range
        random_x_location = round(random.uniform(X_MAX_REACHABLE + 4, X_MAX_UNREACHABLE), 5)

        # generate a random y location with the reachable range
        random_y_location = round(random.uniform(Y_LOW_REACHABLE, Y_HIGH_REACHABLE), 5)

        shift_x_value = pig.x - random_x_location
        shift_y_value = pig.y - random_y_location
        pig.x = random_x_location
        pig.y = random_y_location

    # adjust the platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_9_2(self, template_data):
    shift_x_value = 0
    shift_y_value = 0

    # pig should be within the unreachable range
    for pig in template_data[1]:
        # generate a random x location with the unreachable range
        random_x_location = round(random.uniform(X_MAX_REACHABLE + 1, X_MAX_UNREACHABLE), 5)

        # generate a random y location with the reachable range
        random_y_location = round(random.uniform(Y_LOW_REACHABLE, Y_HIGH_REACHABLE), 5)

        shift_x_value = pig.x - random_x_location
        shift_y_value = pig.y - random_y_location
        pig.x = random_x_location
        pig.y = random_y_location

    # adjust the platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_9_3(self, template_data):
    # point that needs to be reachable (furthers pig)
    reachable_point = [1.90999, -0.05851]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-2.910033, X_MAX_REACHABLE, -0.05851, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_9_4(self, template_data):
    # point that needs to be reachable (top of the divider)
    reachable_point = [0.97, 2.33]

    # get a reachable location for the reachable point
    random_x, random_y = self.get_reachable_location_using_reachability_line(-2.910033, X_MAX_REACHABLE - 5, 2.33, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_9_5(self, template_data):
    # point that needs to be reachable (pig)
    reachable_point = [3.35, 0.1286316]

    # get a reachable location for the reachable point (low trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5.369997, X_MAX_REACHABLE, -1.421352, 2.8)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_9_6(self, template_data):
    # point that needs to be reachable (middle of the bridge)
    reachable_point = [-0.8199974, -1.90136]

    # get a reachable location for the reachable point (high trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-6.249995, X_MAX_REACHABLE - 5, -2.330358, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_9_7(self, template_data):
    # point that needs to be reachable (opening)
    reachable_point = [-0.32, -1.43]

    # get a reachable location for the reachable point (high trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-8.876295, X_MAX_REACHABLE - 5, -1.43, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data


def template_3_9_8(self, template_data):
    # point that needs to be reachable (topmost pig)
    reachable_point = [0.2198468, 0.8202759]

    # get a reachable location for the reachable point (high trajectory)
    random_x, random_y = self.get_reachable_location_using_reachability_line(-5.219497, X_MAX_REACHABLE - 5, 0.8202759, Y_HIGH_REACHABLE)

    shift_x_value = reachable_point[0] - random_x
    shift_y_value = reachable_point[1] - random_y

    # shift the pig
    for pig in template_data[1]:
        pig.x -= shift_x_value
        pig.y -= shift_y_value

    # shift the other blocks and platforms
    for block in template_data[0]:
        block.x -= shift_x_value
        block.y -= shift_y_value

    self.place_random_blocks_on_ground(template_data, [])
    return template_data
