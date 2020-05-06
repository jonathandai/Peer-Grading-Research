import sys
import numpy as np
import pandas as pd
import pprint
from os import listdir
from os.path import isfile, join

# global constant declaration 
PROBLEM_DIV = '--------------------------------------------------------------------------------'
PERSON_DIV = '--------------------------------------------------'
COMMENT_DIV = '----------'
TA_DIV = '------------------------------'  # ignore text that comes after this before the next PERSON_DIV
PROBLEM_INDICATOR = '********************'
# set proper table heading structure
TABLE_HEADING_2019 = ['Problem ID', 'Person Type','Person ID', 'Algorithm', 'Proof', 'Clarity']
TABLE_HEADING_2017 = ['Problem ID', 'Person Type','Person ID', 'Comments']

def main(): 
	txt_to_format = [] 
	if len(sys.argv) <= 1: 
		print("Please provide parameters: either enter space separated file NAMES or . to format all files in the Data directory")
	elif sys.argv[1] == ".":
		txt_to_format = [f for f in listdir("./Data") if isfile(join("./Data", f))]
	else: 
		txt_to_format = sys.argv[1:]
	for txt in txt_to_format:
		if(txt != '.DS_Store'):
			print("Formatting:", txt)
			path = "./Data/" + txt
			format_data(path)

# formats data into excel sheet 
def format_data(file_path):
	# load txt file into columnwise np array line by line 
	text_array = np.genfromtxt(fname=file_path, dtype=str, delimiter=PROBLEM_DIV, usecols=np.arange(0, 1))

	# load proper table heading 
	if("2019" in file_path):
		table_heading = TABLE_HEADING_2019
	elif("2017" in file_path):
		table_heading = TABLE_HEADING_2017

	parsed_array = []	# num_entries x num_headings 2D list 
	parsed_array.append(table_heading)
	table_row = [] # one row of data in the table  
	problem_id = "THIS PROBLEM HAS NO IDEA"

	# print initial text array 
	pp = pprint.PrettyPrinter(indent=0)
	# pp.pprint(text_array) 

	row_index = 0
	num_rows = text_array.size
	# for each row in text_array 
	while row_index < num_rows:
		if PROBLEM_INDICATOR in text_array[row_index]:
			# set problem ID 
			_ , problem_id = split_field(text_array[row_index])
		if row_index+1 < num_rows and text_array[row_index] == PERSON_DIV:
			# inc row to person ID 
			row_index += 1
			person_type, person_id = split_field(text_array[row_index])
			# append first 3 cols of data 
			table_row.append(problem_id)
			table_row.append(person_type)
			table_row.append(person_id)
			
			while row_index+1 < num_rows and (text_array[row_index+1] != PERSON_DIV and text_array[row_index+1] != PROBLEM_DIV):
				# keep going until you hit the next person 
				if text_array[row_index] == COMMENT_DIV: 
					# add comment after comment div 
					row_index += 1
					_, comment = split_field(text_array[row_index]) 
					while row_index+1 < num_rows and (text_array[row_index+1] != COMMENT_DIV and text_array[row_index+1] != TA_DIV and text_array[row_index+1] != PERSON_DIV):
						# keep searching in case there is a new line within the comment 
						comment += text_array[row_index+1]
						row_index += 1
					table_row.append(comment)
					# row_index += 1
					if row_index < num_rows and text_array[row_index] == TA_DIV:
						# if you run into TA_DIV, keep iterating until you get to the next person 
						while row_index+1 < num_rows and (text_array[row_index+1] != PROBLEM_DIV and text_array[row_index+1] != PERSON_DIV):
							row_index += 1
				else: 
					row_index += 1
			# after each person, push the row and reset
			parsed_array.append(table_row[0:len(table_heading)])
			# pp.pprint(table_row)
			table_row = [] 
		row_index += 1

	# convert 2D list to np array 
	np_parsed_array = np.array(parsed_array)

	# convert np array into a dataframe
	df = pd.DataFrame(np_parsed_array) 

	# save to xlsx file
	filepath = file_path.replace('txt', 'xlsx').replace('Data', 'Excel_Data')
	df.to_excel(filepath, index=False)

# splits row into field and data. if no data after ':' return '' in its place 
def split_field(line):
	split_data = line.split(':', 1)
	if len(split_data) != 2: 
		return split_data[0], ''
	return split_data[0], split_data[1]

if __name__ == "__main__":
	main()