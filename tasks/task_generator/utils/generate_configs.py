'''
This script generates the config files from the splitted configs (where non-novel levels and novel levels are in separate files)
'''

from os import listdir
from os.path import isfile, join
import random

splitted_config_file_path = './config_files/splitted_configs/'
combined_config_file_path = './config_files/config.xml'
generated_config_info_file_path = './config_files/generated_config_info.csv'
novel_level_count = 40
combined_config_data = []
# read the split config files

splitted_config_files = [f for f in listdir(splitted_config_file_path) if isfile(join(splitted_config_file_path, f))]
print(splitted_config_files)

# to generate the combined config file take 1-40 levels from the non-novel and take all 40 levels from the novel levels
for split_config_file in splitted_config_files:
	# type(split_config_file)
	# get the normal level config files and then find their novel config file to create the combined config file
	if 'normal' in split_config_file:  # normal level config file
		trial_data = []
		non_novel_level_count = random.randint(1, 40)
		line_count = 0
		for line in open(splitted_config_file_path + split_config_file):  # get the non novel levels
			line_count += 1
			trial_data.append(line)
			if line_count >= non_novel_level_count:
				break

		novel_split_config_file = split_config_file.replace('normal', 'novel')
		line_count = 0
		for line in open(splitted_config_file_path + novel_split_config_file):  # get the novel levels
			line_count += 1
			trial_data.append(line)
			if line_count >= novel_level_count:
				break

		combined_config_data.append(trial_data)
		# print('combined_config_data: ', combined_config_data)

# write the combined config file
starting_meta_data = '<?xml version="1.0" encoding="utf-16"?>\n<evaluation>\n  <novelty_detection_measurement step="1" measure_in_training="True" measure_in_testing="True" />\n  <trials>\n'
ending_meta_data = '  </trials>\n</evaluation>'
combined_config_file = open(combined_config_file_path, 'w')
combined_config_file.write(starting_meta_data)
trial_id = 0
time_limit = 10000

# write the config_info file at the same time
generated_config_info_file = open(generated_config_info_file_path, 'w')
generated_config_info_file.write('novelty_type, trial_id, non_novel_level_count, novel_level_count\n')

# write the final combined config and config_info files
for trial_data in combined_config_data:

	# write the config file
	combined_config_file.write('    <trial id="{}" number_of_executions="1" checkpoint_time_limit="200" checkpoint_interaction_limit="200" notify_novelty="False">\n'.format(trial_id))
	combined_config_file.write('      <game_level_set mode="training" time_limit="{}" total_interaction_limit="60000" attempt_limit_per_level="1" allow_level_selection="False">\n'.format(time_limit))

	for game_level in trial_data:
		combined_config_file.write('        <game_levels level_path="{}" />\n'.format(game_level[:-1]))

	combined_config_file.write('      </game_level_set>\n    </trial>\n')

	# write the config info file
	generated_config_info_file.write('{}, {}, {}, {}\n'.format(trial_data[0].split('/')[4], trial_id, len([i for i in trial_data if 'novelty_level_0' in i]), novel_level_count))
	trial_id += 1

combined_config_file.write(ending_meta_data)

combined_config_file.close()
generated_config_info_file.close()


