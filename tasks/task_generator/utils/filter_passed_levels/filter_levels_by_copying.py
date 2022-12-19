# importing os module
import os
from shutil import copy
import shutil

level_base_dir = '../../../Assets/StreamingAssets/Levels/'
copying_directory = '../../../Assets/StreamingAssets/PassedLevels/'
# level_list_to_copy = 'all_passed_non_novel.csv'
level_list_to_copy = 'filtered_novel_levels_to_keep.csv'

def main():
	with open(level_list_to_copy) as fp:
		lines = fp.readlines()
		for line in lines[1:]:  # skip the header
			level_file_name = line.strip()

			# make the level path from the level file name
			level_file_directory = level_file_name.split('/')[3] + '/' + level_file_name.split('/')[4] + '/' + level_file_name.split('/')[5] + '/'
			level_file_path = level_base_dir  + level_file_directory + level_file_name.split('/')[6]
			print('copying the level', level_file_path)

			# make directory if not exist
			os.makedirs(os.path.dirname(copying_directory+level_file_directory), exist_ok=True)
			shutil.copy(level_file_path, copying_directory+level_file_directory)

	print('removed ', len(lines) - 1, 'levels')


# i = 1
# # "{0:05d}".format(i)
# for filename in os.listdir(source_dir):
#     # new_file_name = filename.split('_')[0] + '_'+ filename.split('_')[1] + '_0_7_3'
#     new_file_name = filename.split('_')[0] + '_1_0_7_3'
#     print(new_file_name)
#
#     dst = destination_dir + new_file_name + ".xml"
#     src = source_dir + '/' + filename
#
#     os.rename(src, dst)
#     i += 1


# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()
