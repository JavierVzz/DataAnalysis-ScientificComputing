# Javier Vazquez
# Course: COMPSCI X433.3 Python for Data Analysis and Scientific Computing
# Homework 2
# Date: April 29, 2017
# Description: pg 33 - HW assignment 2, Lecture4.pdf

import os
import numpy as np


def main():
    A = np.random.rand(3,5)
    print(A)


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()