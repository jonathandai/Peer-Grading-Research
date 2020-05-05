import numpy as np
import sys
import pandas as pd

# def parse_problem():


def split_field(line):
	split_data = line.split(': ', 1)
	return split_data


def main():
	# files_to_format = []
	# if(len(sys.argv) == 0):
	#     # if no input is given, format all documents in data folder
	# else:
	separator = '--------------------------------------------------------------------------------'

	# This is the right one
	## text_array = np.genfromtxt(fname=sys.argv[1], dtype=str, delimiter=separator, usecols=np.arange(0,1))
	text_array = np.genfromtxt(fname="./Data/2019_Fall_Assignment_6.2.txt",
							dtype=str, delimiter=separator, usecols=np.arange(0, 1))
#     text_array = np.genfromtxt(fname="Data/Fall_Assignment_6.2.txt", dtype=str, delimiter=separator, usecols=np.arange(0,1))
	# for x in range(text_array.size):
	# 	print(x, text_array[x])

	# format np matrix into proper excel format
	titles = ['problem id', 'person type',
		'person id', 'Algorithm', 'Proof', 'Clarity']

	parsed_array = []
	parsed_array.append(titles)
	feedback_entry = []

	i = 0
	while i < text_array.size:
		if text_array[i] == '********************':
			print(text_array[i])
			problem_id = split_field(line)[1]
			feedback_entry.append(problem_id)
		elif text_array[i] == '--------------------------------------------------':
			i += 1
			print(text_array[i])
			person_type = split_field(text_array[i])[0]
			person_id = split_field(text_array[i])[1]
			feedback_entry.append(person_type)
			feedback_entry.append(person_id)
			i += 1
			while text_array[i+1] != '--------------------------------------------------':
				if text_array[i] != '----------':
					print(text_array[i])
					try:
						feedback_entry.append(split_field(text_array[i])[1])
					except:
						feedback_entry.append('')
					i += 1
				i += 1
		i += 1
		parsed_array.append(feedback_entry)
	print(parsed_array)

	# convert your array into a dataframe
	df = pd.DataFrame(text_array)
	# save to xlsx file
	filepath = 'data.xlsx' 
	df.to_excel(filepath, index=False)

if __name__ == "__main__":
	main()



