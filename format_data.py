import numpy as np
import sys
# from io import StringIO

def main():
    # c = StringIO(sys.argv[1])

    # files_to_format = [] 
    # if(len(sys.argv) == 0):
    #     # if no input is given, format all documents in data folder 
    # else: 
    separator = '--------------------------------------------------------------------------------'
    text_array = np.genfromtxt(fname=sys.argv[1], dtype=str, delimiter=separator, usecols=np.arange(0,1))
    # text_array = np.genfromtxt(fname=sys.argv[1], dtype=str, usecols=np.arange(0,1))
    # text_array = np.genfromtxt(fname=sys.argv[1], dtype=str, delimiter=separator, usecols=np.arange(0,1))
    print('hello')
    for x in range(text_array.size):
        print(x, text_array[x])


if __name__ == "__main__":
    main()
