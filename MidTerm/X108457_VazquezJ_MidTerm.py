# Javier Vazquez
# Course: COMPSCI X433.3 Python for Data Analysis and Scientific Computing
# MidTerm
# Date: May 3, 2017

import os

import numpy as np
import pylab as plb


def sma(A, wwidth=2):
    sma = np.cumsum(A)
    sma[wwidth:] = sma[wwidth:] - sma[:-wwidth]
    return sma[wwidth - 1:] / wwidth, wwidth

def main():
    A = np.arange(5, 12*2+5, 2)
    B, Bw = sma(A)
    C, Cw = sma(A, 4)

    print("\033[1mThe original array is: \033[0m\n",A)
    print("\n\033[1mMoving average result is: \033[0m\n",B,"\n",C)
    print("\n\033[1mWindow width is:\033[0m\n",Bw,"\n",Cw)

    plb.figure(figsize=(10, 6), dpi=120)
    plb.title("Sin(B) and Sin(C)")
    plb.plot(plb.sin(B), color="r", label="Sin(B)")

    plb.plot(plb.sin(C), color="b", linewidth=2, linestyle="-.", label="Sin(C)")
    plb.ylim(min(plb.sin(B)) - .5, max(plb.sin(B)) + .5)
    plb.legend()
    plb.grid()
    plb.show()


if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()