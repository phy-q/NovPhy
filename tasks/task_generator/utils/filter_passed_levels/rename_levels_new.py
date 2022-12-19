import os
from pathlib import Path
from random import shuffle

level_base_dir = '../../../Assets/StreamingAssets/PassedLevels/'

all_level_folders = [x[0] for x in os.walk(level_base_dir)]

print(all_level_folders)
for level_folder in all_level_folders:

	# only get the level folders

	if ('\Levels' in level_folder):
		print(level_folder)

		# get level list and remove .meta file
		level_file_list = os.listdir(level_folder)
		level_file_list = [file_name for file_name in level_file_list if '.meta' not in file_name]

		# shuffle the level list
		shuffle(level_file_list)

		print(level_file_list)

		# rename the levels
		level_index = 1

		for level_file in level_file_list:
			# calculate the new level name
			level_name = level_file.split(' ')[0].split('.')[0]
			new_level_name = "{0:05d}".format(level_index) + '_' + level_name.split('_')[1] + '_' + \
							 level_name.split('_')[2] + '_' + level_name.split('_')[3] + '_' + level_name.split('_')[
								 4] + '_' + level_name.split('_')[5]
			print(level_name + ' ' + new_level_name)

			# first rename to a temporary file name as there are can be existing files with that name
			os.rename(level_base_dir + level_folder + '/' + level_file,
					  level_base_dir + level_folder + '/' + new_level_name + '.xml.temp')

			level_index += 1

		# rename the temp files back to xml files
		level_file_list = os.listdir(level_folder)
		level_file_list = [file_name for file_name in level_file_list if '.meta' not in file_name]
		for level_file in level_file_list:
			os.rename(level_base_dir + level_folder + '/' + level_file,
					  level_base_dir + level_folder + '/' + level_file.split('.')[0] + '.xml')


		# if there are more than 350 levels delete them
		level_file_list = os.listdir(level_folder)
		level_file_list = [file_name for file_name in level_file_list if '.meta' not in file_name]

		level_count = 0
		for level_file in level_file_list:
			level_count += 1
			if level_count > 350:
				os.remove(level_base_dir + level_folder + '/' + level_file)


