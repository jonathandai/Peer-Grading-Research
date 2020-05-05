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
    text_array = np.genfromtxt(fname="./Data/2019_Fall_Assignment_6.2.txt", dtype=str, delimiter=separator, usecols=np.arange(0,1))
#     text_array = np.genfromtxt(fname="Data/Fall_Assignment_6.2.txt", dtype=str, delimiter=separator, usecols=np.arange(0,1))
    for x in range(text_array.size):
        print(x, text_array[x])



    # format np matrix into proper excel format 
    titles = ['problem id', 'person type', 'person id', 'Algorithm', 'Proof', 'Clarity']

    parsed_array = []
    parsed_array[0] = titles

	feedback_entry = []

    # for line in text_array:
    #     if line.contains('********************'):
	# 		problem_id = get_field(line)
	# 		feedback_entry[0] = problem_id
	# 	elif line.contains('TA id'):
	# 		person_type = 'TA'
	# 		person_id = get_field(line)
	# 		feedback_entry[1] = person_id
	# 		feedback_entry[2] = person_type
	# 	elif line.contains('peer id'):
	# 		person_type = 'peer'
	# 		person_id = get_field(line)
	# 		feedback_entry[1] = person_id
	# 		feedback_entry[2] = person_type
	# 	elif line.contains('*Algorithm*'):
	# 		algorithm_text = get_field(line)
	# 		feedback_entry[3] = algorithm_text

	i = 0
	while i < text_array.size:
		if text_array[i].contains('********************'):
			problem_id = split_field(line)[1]
			feedback_entry.push(problem_id)
	    elif text_array[i] == '--------------------------------------------------':
			i += 1
			person_type = split_field(text_array[i])[0]
			person_id = split_field(text_array[i])[1]
			feedback_entry.push(person_type)
			feedback_entry.push(person_id)
			i += 1
			while text_array[i+1] != '--------------------------------------------------':
				


    # convert your array into a dataframe
    df = pd.DataFrame(text_array)
    # save to xlsx file
    filepath = 'data.xlsx' 
    df.to_excel(filepath, index=False)

if __name__ == "__main__":
    main()



