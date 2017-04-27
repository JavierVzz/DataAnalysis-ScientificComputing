# Javier Vazquez
# File Operation
# Date: April 26, 2017

import os
import pandas as pd
import numpy as np

class file_operations():

    def __init__(self):
        pass

    def write_my_file(self, array, fileName = "theFile.txt"):
        file = open(fileName, "w")
        file.write(str(array))
        return 0

    def read_my_file(self, fileName = "theFile.txt"):
        fo = open(fileName, "r")
        line = fo.readlines()
        fo.close()
        strLine = line[0].replace("[", "")
        strLine = strLine.replace("]", "")
        print(strLine)

        newArray = np.asarray(line)
        return newArray


if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")