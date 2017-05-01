# 1. Include a section with your name
# Javier Vazquez
# Course: COMPSCI X433.3 Python for Data Analysis and Scientific Computing
# Homework 2
# Date: April 29, 2017
# Description: pg 33 - HW assignment 2, Lecture4.pdf

import os
import numpy as np


def main():
    # 2. Create matrix A with size (3,5) containing random numbers
    A = np.random.rand(3,5)
    print(A)

    # 3. Find the size and length of matrix A
    print("A size: ",A.size)
    print("A lenght: ", A.shape)

    # 4. Resize (crop) matrix A to size (3,4)
    A = np.delete(A, 4, 1)
    print("Matrix A resize to (3,4): \n", A)

    # 5. Find the transpose of matrix A and assign it to B
    B = A.T
    print("Matrix B: \n", B)

    # 6. Find the minimum value in column 1 of matrix B
    print("Minimum col 1: \n", np.amin(B[:,1]))

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()