import numpy as np
import sys
import pandas as pd

def split_field(line):
	if ': ' in line:
		split_data = line.split(': ', 1)
	elif ':' in line:
		split_data = line.split(':', 1)
	return split_data


def main():
	separator = '--------------------------------------------------------------------------------'

	# This is the right one
	text_array = np.genfromtxt(fname=sys.argv[1], dtype=str, delimiter=separator, usecols=np.arange(0,1))

	# format np matrix into proper excel format
	titles = ['problem id', 'person type',
		'person id', 'Algorithm', 'Proof', 'Clarity']

	parsed_array = []
	parsed_array.append(titles)
	feedback_entry = []
	ta_comment_tracker = False
	comment_with_blanks = ''
	comment_with_blanks_tracker = 0

	i = 0
	while i < text_array.size - 1:
		if '********************' in text_array[i]:
			problem_id = split_field(text_array[i])[1]
		elif text_array[i] == '--------------------------------------------------':
			i += 1
			person_type = split_field(text_array[i])[0]
			person_id = split_field(text_array[i])[1]
			feedback_entry.append(problem_id)
			feedback_entry.append(person_type)
			feedback_entry.append(person_id)
			i += 1
			while i < text_array.size -1 and text_array[i] != '--------------------------------------------------':
				if text_array[i] == '------------------------------':
					ta_comment_tracker = True
				if text_array[i] != '----------' and text_array[i] != '' and ta_comment_tracker == False:
					if '----' not in text_array[i+1]:
						if comment_with_blanks_tracker == 0:
							comment_with_blanks = comment_with_blanks + split_field(text_array[i])[1]
							comment_with_blanks_tracker = 1
						else:
							comment_with_blanks = comment_with_blanks + text_array[i]
					else:
						try:
							if comment_with_blanks == '':
								feedback_entry.append(split_field(text_array[i])[1])
							else:
								feedback_entry.append(split_field(comment_with_blanks))
								comment_with_blanks = ''
								comment_with_blanks_tracker = 0
						except:
							feedback_entry.append('')
				i += 1
			if text_array[i] == '--------------------------------------------------':
				parsed_array.append(feedback_entry)
				feedback_entry = []
				ta_comment_tracker = False
				continue
		i += 1

	df = pd.DataFrame(parsed_array)
	# save to xlsx file
	filepath = 'data.xlsx' 
	df.to_excel(filepath, index=False)

if __name__ == "__main__":
	main()



