# 1. Include a section with your name
# Javier Vazquez
# Course: COMPSCI X433.3 Python for Data Analysis and Scientific Computing
# Homework 2
# Date: May, 2017
# Description: pg 33 - HW assignment 3, Lecture5.pdf

import os

# 2. Work only with these imports:
# from numpy import matrix, array, random, min, max
# import pylab as plb (... or use matplotlib)
from numpy import matrix, array, random, min, max
import pylab as plb


# 5. Using if, for or while, create a func4on that overwrites every element in A
# that falls outside of the interval [2:9), and overwrite that element with the
# average between the smallest and largest element in A
def functionOverwriter(A):
    mean_A = (min(A) + max(A))/2
    A = [mean_A if i <=2 or i > 9 else i for i in A]
    print("\n\033[1mList A: \n\033[0m", A)

    # 6. Normalize each list element to be bound between [0:0.1]
    A = [(i - min(A))/(max(A) - min(A))for i in A]
    print("\n\033[1mNormalized A: \n\033[0m", A)

    return A

def main():
    # 3. Create a list A of 600 random numbers bound between (0:10)
    A = [random.random_integers(0,10) for i in range(600)]
    print("\033[1mList A: \n\033[0m",A)


    # 4. Create an array B with with 500 elements bound in the range [-3*pi:2*pi]
    B = plb.linspace(-3*plb.pi, 2*plb.pi, 500, endpoint=True)
    print("\n\033[1mArray B: \n \033[0m", B)

    # 7. Return the result from the function to C
    C = functionOverwriter(A)
    print("\n\033[1mC: \033[0m", type(C))
    print(C)

    # 8. Cast C as an array
    C = array(C)
    print("\n\033[1mC: \033[0m", type(C))
    print(C)

    # 9. Add C to B (think of C as noise) and record the result in D
    D = B+C[:B.size]
    print("\n\033[1mD: \033[0m", D)

    # 10. Create a figure, give it a title and specify your own size and dpi
    plb.figure(figsize=(10, 6), dpi=120)
    plb.title("Sin(D)")


    # 11. Plot the sin of D, in the (2,1,1) location of the figure
    plb.subplot(2, 1, 1)
    plb.plot(plb.sin(D), color = "r", label= "Sin")

    # 12. Overlay a plot of cos using D, with different color, thickness and type of line
    plb.plot(plb.cos(D), color = "b", linewidth =2, linestyle= "-.", label="Cos")

    # 13. Create some space on top and bottom of the plot (on the y axis) and show the grid
    plb.ylim(min(plb.cos(D))-.5, max(plb.cos(D))+.5)
    plb.grid()

    # 14. Specify the following: title, Y-axis label and legend to fit in the best way
    plb.title("Sin(D) and Cos(D)")
    plb.legend()
    plb.ylabel("Y-axis")
    plb.legend(loc="upper right")

    # 15. Plot the tan of D, in location (2,1,2) with grid showing, X-axis label, Y-axis label
    # and legend on top right
    plb.subplot(2, 1, 2)
    plb.plot(plb.tan(D), color="g", label="Tan")
    plb.ylabel("Y-axis")
    plb.xlabel("X-axis")
    plb.legend(loc="upper right")

    plb.show()

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()