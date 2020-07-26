# Program extracting all columns 
# name in Python 
import sys
import xlrd
import xlsxwriter

def main():
	filenames_to_format = []
	if len(sys.argv) <= 1:
		print("Please provide parameters: either enter space separated file NAMES or . to format all files in the Excel_Data directory. Files to be formatted should be placed in the Excel_Data directory. Input only the filename, not the entire path.")
	elif sys.argv[1] == ".":
		filenames_to_format = [f for f in listdir("./Excel_Data") if isfile(join("./Excel_Data", f))]
	else:
		filenames_to_format = sys.argv[1:]
	for filename in filenames_to_format:
		if(filename != '.DS_Store'):
			print("Processing:", filename)
			path = "./Excel_Data/" + filename
			format_data(path, filename[:-5])

def format_data(path, filename):
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0) 
    # For row 0 and column 0 
    sheet.cell_value(0, 0)
    data = []
    i=7
    j = 8
    k =9
    l = 10
    
    for i in range(1, sheet.nrows):
        calculated_row = [None] * 12
        sheet_row = sheet.row_values(i)
        corrections = sheet_row[7]
        suggestions = sheet_row[8]
        specificity = sheet_row[9]
        justification = sheet_row[10]
        score = 1
        calculated_row[0:11] = sheet_row[0:11]

        if corrections > 0 or suggestions > 0:
            if corrections + suggestions > 1:
                score += 1
            else:
                if specificity > 3:
                    score += 1
        if specificity > 0:
            score += 1
        if justification > 0:
            score += 1
        else:
            if specificity > 10:
                score += 1

        calculated_row[11] = score
        data.append(calculated_row)
    
    workbook = xlsxwriter.Workbook('./Excel_Data/%s_processed.xlsx' % filename)
    bold = workbook.add_format({'bold': 1})

    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Problem Id', bold)
    worksheet.write('B1', 'Grade', bold)
    worksheet.write('C1', 'Person Type', bold)
    worksheet.write('D1', 'Person ID', bold)
    worksheet.write('E1', 'Comment', bold)
    worksheet.write('F1', 'Negative Points (count)', bold)
    worksheet.write('G1', 'Positive Point (count)', bold)
    worksheet.write('H1', 'Corrections (count)', bold)
    worksheet.write('I1', 'Suggestions (count)', bold)
    worksheet.write('J1', 'Specificity (count)', bold)
    worksheet.write('K1', 'Justification (count)', bold)
    worksheet.write('L1', 'Calculated Quality Score (1-4)', bold)

    curr_row = 1
    curr_col = 0

    for prob_id, grade, person_type, person_id, comment, neg_point, pos_point, corr, sugg, spec, justif, score in data:
        worksheet.write(curr_row, curr_col, prob_id)
        worksheet.write(curr_row, curr_col+1, grade)
        worksheet.write(curr_row, curr_col+2, person_type)
        worksheet.write(curr_row, curr_col+3, person_id)
        worksheet.write(curr_row, curr_col+4, comment)
        worksheet.write(curr_row, curr_col+5, neg_point)
        worksheet.write(curr_row, curr_col+6, pos_point)
        worksheet.write(curr_row, curr_col+7, corr)
        worksheet.write(curr_row, curr_col+8, sugg)
        worksheet.write(curr_row, curr_col+9, spec)
        worksheet.write(curr_row, curr_col+10, justif)
        worksheet.write(curr_row, curr_col+11, score)
        curr_row += 1
    
    print('Calculations completed, please check the Excel_Data folder')
    workbook.close()

if __name__ == "__main__":
	main()