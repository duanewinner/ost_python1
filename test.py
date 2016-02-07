#!/usr/local/bin/python3

import math

def r5(number):
    y = math.ceil(number / 4)
    while True:
        if y % 5 == 0:
            y_tic = int(y / 5)
            y_bin = {}
            for i in range(y_tic, y*4+1, y_tic):
                y_bin[i]=0
            return(y,y_tic,sorted(y_bin))
        y+=1


if __name__ == "__main__":
    print(r5(4498))
