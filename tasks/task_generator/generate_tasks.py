import math
import os
import re
import pandas as pd
from utils.generate_variations import GenerateLevels
from utils.data_classes import *

# input and output folders
level_input_folder = './input/'
level_output_folder = './output/'
config_file = 'Novelty Benchmark Naming Convention.xlsx'


class GenerateVariations:

	def read_level_file(self, level_file_name):
		# read the level file and extract the objects
		print('reading the template file', level_file_name)

		all_birds = []
		all_blocks = []
		all_pigs = []
		all_tnts = []
		meta_data = []

		# use the count of the object as an identifier for the object
		object_count = 0

		# there are both UTF-8 encoded and UTF-16 encoded level.xml files, handle them both
		try:
			level_file = open(level_file_name, 'r', encoding='utf-8')
			level_file_content = level_file.readlines()
		except UnicodeError:
			level_file = open(level_file_name, 'r', encoding='utf-16')
			level_file_content = level_file.readlines()

		# with open(level_file_name) as level_file:
		for line in level_file_content:
			if 'Bird type' in line:
				type = re.search('type="(.*?)"', line).group(1)
				all_birds.append(Bird(type))

			elif 'Platform' in line:
				object_count += 1

				type = re.search('type="(.*?)"', line).group(1)
				x = re.search('x="(.*?)"', line).group(1)
				y = re.search('y="(.*?)"', line).group(1)
				scale_x = re.search('scaleX="(.*?)"', line).group(1) if re.search('scaleX="(.*?)"',
																				  line) is not None else 1
				scale_y = re.search('scaleY="(.*?)"', line).group(1) if re.search('scaleY="(.*?)"',
																				  line) is not None else 1
				rotation = re.search('rotation="(.*?)"', line).group(1) if re.search('rotation="(.*?)"',
																					 line) is not None else 0

				all_blocks.append(
					Block(object_count, type, "", float(x), float(y), float(rotation), float(scale_x),
						  float(scale_y)))

			elif 'Block' in line or 'Novelty' in line or 'ExternalAgent' in line:
				object_count += 1
				type = re.search('type="(.*?)"', line).group(1)
				x = re.search('x="(.*?)"', line).group(1)
				y = re.search('y="(.*?)"', line).group(1)
				rotation = re.search('rotation="(.*?)"', line).group(1)
				try:
					material = re.search('material="(.*?)"', line).group(1)
				except:
					material = ""

				scale_x = re.search('scaleX="(.*?)"', line).group(1) if re.search('scaleX="(.*?)"',
																				  line) is not None else 1
				scale_y = re.search('scaleY="(.*?)"', line).group(1) if re.search('scaleY="(.*?)"',
																				  line) is not None else 1

				all_blocks.append(
					Block(object_count, type, material, float(x), float(y), float(rotation), scale_x=float(scale_x),
						  scale_y=float(scale_y)))

			elif 'Pig' in line:
				object_count += 1

				type = re.search('type="(.*?)"', line).group(1)
				x = re.search('x="(.*?)"', line).group(1)
				y = re.search('y="(.*?)"', line).group(1)
				rotation = re.search('rotation="(.*?)"', line).group(1)

				all_pigs.append(Pig(object_count, type, float(x), float(y), float(rotation)))

			elif 'TNT' in line:
				object_count += 1

				x = re.search('x="(.*?)"', line).group(1)
				y = re.search('y="(.*?)"', line).group(1)
				rotation = re.search('rotation="(.*?)"', line).group(1)

				all_tnts.append(Tnt(object_count, float(x), float(y), float(rotation)))

			else:
				if '<GameObjects>' in line or '</GameObjects>' in line or '</Level>' in line or '<Birds>' in line or '</Birds>' in line:
					continue
				else:
					meta_data.append(line)

		level_file.close()
		return all_birds, all_blocks, all_pigs, all_tnts, meta_data

	def write_level_file(self, all_birds, all_blocks, all_pigs, all_tnts, level_base_folder, file_name, meta_data):
		rounding_digits = 4

		try:
			level_file = open(level_output_folder + level_base_folder + '/' + file_name, "w")
		# level_file = open(level_output_folder  + '/' + file_name, "w")
		except:  # folder not present, create it
			os.makedirs(level_output_folder + level_base_folder)
			level_file = open(level_output_folder + level_base_folder + '/' + file_name, "w")

		# write meta data
		for line in meta_data:
			if 'Slingshot' in line:
				# write birds before the slingshot
				level_file.write('  <Birds>\n')
				for bird in all_birds:
					level_file.write('    <Bird type="%s"/>\n' % bird.type)
				level_file.write('  </Birds>\n')
			level_file.write(line)

		level_file.write('  <GameObjects>\n')

		# write pigs
		for pig in all_pigs:
			# unchanged pigs
			level_file.write('    <Pig type="%s" material="" x="%s" y="%s" rotation="%s" />\n' % (
				pig.type, str(round(pig.x, rounding_digits)), str(round(pig.y, rounding_digits)),
				str(round(pig.rotation, rounding_digits))))

		# write TNTs
		for tnt in all_tnts:
			level_file.write(
				'    <TNT type="" x="%s" y="%s" rotation="%s" />\n' % (
					str(round(tnt.x, rounding_digits)), str(round(tnt.y, rounding_digits)),
					str(round(tnt.rotation, rounding_digits))))

		# write blocks
		for block in all_blocks:
			# print("block", block)
			# check if platform
			if block.type == 'Platform':
				level_file.write(
					'    <Platform type="%s" material="" x="%s" y="%s" rotation="%s" scaleX="%s" scaleY="%s" />\n' % (
						block.type, str(round(block.x, rounding_digits)), str(round(block.y, rounding_digits)),
						str(round(block.rotation, rounding_digits)),
						str(round(block.scale_x, rounding_digits)),
						str(round(block.scale_y, rounding_digits))))

			# novel game objects
			elif block.type == 'PinkCircle' or block.type == 'Fan' or block.type == 'InverseAirTurbulence' or block.type == 'NonNovelAirTurbulence' or block.type == 'NovelAirTurbulence' or block.type == 'PinkRectFat' or block.type == 'PinkSquareHole' or block.type == 'Storm' or block.type == 'InverseGravity' or block.type == 'Magnet':
				level_file.write(
					'    <Novelty type="%s" material="" x="%s" y="%s" rotation="%s" scaleX="%s" scaleY="%s" />\n' % (
						block.type, str(round(block.x, rounding_digits)), str(round(block.y, rounding_digits)),
						str(round(block.rotation, rounding_digits)),
						str(round(block.scale_x, rounding_digits)),
						str(round(block.scale_y, rounding_digits))))

			# novel game objects
			# elif block.type == 'novel_object_242' or block.type == 'novel_object_253' or block.type == 'SquareHanger' or block.type == 'novel_object_255' or block.type == 'novel_object_256' or block.type == 'novel_object_257':
			#     level_file.write(
			#         '    <Novelty type="%s" material="" x="%s" y="%s" rotation="%s" scaleX="%s" scaleY="%s" />\n' % (
			#             block.type, str(round(block.x, rounding_digits)), str(round(block.y, rounding_digits)),
			#             str(round(block.rotation, rounding_digits)),
			#             str(round(block.scale_x, rounding_digits)),
			#             str(round(block.scale_y, rounding_digits))))

			# external agents
			# elif block.type == 'Magician' or block.type == 'Wizard' or block.type == 'Butterfly' or block.type == 'Worm' or block.type == 'novel_object_245' or block.type == 'novel_object_246' or block.type == 'novel_object_225' or block.type == 'novel_object_222' or block.type == 'novel_object_223' or block.type == 'novel_object_224' or block.type == 'novel_object_226' or block.type == 'novel_object_227' or block.type == 'novel_object_232' or block.type == 'novel_object_233' or block.type == 'novel_object_234' or block.type == 'novel_object_235' or block.type == 'novel_object_236' or block.type == 'novel_object_237':
			#     level_file.write(
			#         '    <ExternalAgent type="%s" material="" x="%s" y="%s" rotation="%s" />\n' % (
			#             block.type, str(round(block.x, rounding_digits)), str(round(block.y, rounding_digits)),
			#             str(round(block.rotation, rounding_digits))))

			# normal blocks
			else:
				level_file.write('    <Block type="%s" material="%s" x="%s" y="%s" rotation="%s" />\n' % (
					block.type, block.material, str(round(block.x, rounding_digits)),
					str(round(block.y, rounding_digits)),
					str(round(block.rotation, rounding_digits))))

		# close the level file
		level_file.write('  </GameObjects>\n')
		level_file.write('</Level>\n')
		level_file.close()

	def write_all_levels(self, all_birds, meta_data, generated_levels, level_base_name):
		no_of_levels_written = 0
		no_of_levels_written = 0
		for generated_level in generated_levels:
			level_name = str("{0:05d}".format(no_of_levels_written + 1)) + '_' + level_base_name + '.xml'

			level_base_folder = 'novelty_level_' + level_base_name.split('_')[-2] + '/' + 'type' + \
								level_base_name.split('_')[-3] + '/' + 'Levels'

			self.write_level_file(all_birds, generated_level[0], generated_level[1], generated_level[2],
								  level_base_folder, level_name, meta_data)
			no_of_levels_written += 1

	def read_config_file(self):
		# read the config file of the generation and store data in a dataframe
		config_data_raw = pd.read_excel(config_file, sheet_name='Task Variations', engine='openpyxl')

		# clean the data and only store required info
		cleaned_config_data = {}
		for novel_template_name in config_data_raw['Novel Template Name']:
			if not pd.isna(novel_template_name):
				# print(template_name)
				template_data = config_data_raw[config_data_raw['Novel Template Name'] == novel_template_name].values[0]
				# print(template_data)

				# novel template data (from column 9 to 14)
				novel_template_name = '_'.join(novel_template_name.split('_')[-5:])
				novel_template_data = []  # add the template name as the first element
				for i in range(4,
							   7):  # for reference/boundary coordinate points which are in (separate _x,_y columns) are combined as [_x, _y]
					novel_template_data.append([template_data[i * 2], template_data[i * 2 + 1]])

				# non novel template data (from column 3 to 8)
				non_novel_template_name = '_'.join(novel_template_name.split('_')[:-2]) + '_0_' + \
										  novel_template_name.split('_')[-1]
				non_novel_template_data = []  # add the template name as the first element
				for i in range(1,
							   4):  # for reference/boundary coordinate points which are in (separate _x,_y columns) are combined as [_x, _y]
					non_novel_template_data.append([template_data[i * 2], template_data[i * 2 + 1]])

				# get distraction restrictions (restricted objects that are comma separated. eg: wood circle, ice RectFat)
				non_novel_template_data.append([]) if pd.isnull(template_data[14]) else non_novel_template_data.append(
					template_data[14].split(','))
				novel_template_data.append([]) if pd.isnull(template_data[15]) else novel_template_data.append(
					template_data[15].split(','))

				# print('novel_template_data: ', novel_template_data)
				# print('non_novel_template_data: ', non_novel_template_data)
				cleaned_config_data[novel_template_name] = novel_template_data
				cleaned_config_data[non_novel_template_name] = non_novel_template_data
		# processed_data.append(novel_template_data)
		# processed_data.append(non_novel_template_data)

		# cleaned_config_data = pd.DataFrame(processed_data, columns=['template_name', 'ref_point', 'min_coordinate', 'max_coordinate'])
		return cleaned_config_data

	def main(self):
		# read the input template files
		template_files = os.listdir(level_input_folder)

		# read the config file
		all_config_data = self.read_config_file()
		# print(all_config_data)

		level_generator = GenerateLevels()

		for template_file in template_files:
			# read the template file
			all_birds, all_blocks, all_pigs, all_tnts, meta_data = self.read_level_file(
				level_input_folder + template_file)

			# print('all_birds, all_blocks, all_pigs, all_tnts, meta_data', all_birds, all_blocks, all_pigs, all_tnts, meta_data)

			# template name is the last 5 indexes in the template name: levelIndex_exAgent_templateIndex_noveltyType_noveltyLevel_scenarioIndex
			template_name_indexes = template_file.rsplit('.', 1)[0].split('_')
			template_name = '_'.join(template_name_indexes[-5:])

			# create variations of the template
			generated_levels = level_generator.generate_levels_from_template(template_name,
																			 [all_blocks, all_pigs, all_tnts],
																			 all_config_data[template_name])
			# write the generated levels
			self.write_all_levels(all_birds, meta_data, generated_levels, template_name)


if __name__ == "__main__":
	generate_variations = GenerateVariations()
	generate_variations.main()
