# 1. Include a section with your name
# Javier Vazquez
# Course: COMPSCI X433.3 Python for Data Analysis and Scientific Computing
# Homework 2
# Date: April 29, 2017
# Description: pg 33 - HW assignment 2, Lecture4.pdf

import os
import numpy as np

def function8(X, A):
    print("\nfunction8(X,A)")
    print("Vector X: ", X)
    print("Matrix A:\n ", A)

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

    # 7. Find the minimum and maximum values for the entire matrix A
    print("Maximum value in matrix A: \n", np.amax(A))
    print("Minimum value in matrix A: \n", np.amin(A))

    # 8. Create Vector X (an array) with 4 random numbers
    X = np.random.rand(4)
    print("Vector X: ", X)

    # 9. Create a function and pass Vector X and matrix A in it
    function8(X, A)

    # 15. Display a text on the screen: ‘Name is done with HW2‘, but pass your ‘Name’ as a string variable
    Name = "Javier Vazquez"
    print(Name + " is done with HW2")

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()