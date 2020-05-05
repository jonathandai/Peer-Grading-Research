import numpy as np
import sys
import pandas as pd 

def main():
    # files_to_format = [] 
    # if(len(sys.argv) == 0):
    #     # if no input is given, format all documents in data folder 
    # else: 
    separator = '--------------------------------------------------------------------------------'

    # This is the right one 
    ## text_array = np.genfromtxt(fname=sys.argv[1], dtype=str, delimiter=separator, usecols=np.arange(0,1))
    text_array = np.genfromtxt(fname=sys.argv[1], dtype=str, delimiter=separator, usecols=np.arange(0,1))
    for x in range(text_array.size):
        print(x, text_array[x])

    # format np matrix into proper excel format 
    

    # convert your array into a dataframe
    df = pd.DataFrame(text_array)
    # save to xlsx file
    filepath = 'data.xlsx' 
    df.to_excel(filepath, index=False)

if __name__ == "__main__":
    main()



