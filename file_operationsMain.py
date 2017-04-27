# Javier Vazquez
# File Operation
# Date: April 26, 2017

import os, sys
import file_operationsClass
import numpy as np

def main():
    fo = file_operationsClass.file_operations()
    fiveTo45 = np.random.random_integers(5, 45, 6)
    print(fiveTo45)
    fo.write_my_file(fiveTo45)
    print(fo.read_my_file())




if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()