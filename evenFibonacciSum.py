# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:03:06 2023

@author: hein

For the even fibonacci numbers you only have to calculate every third value,
this can be calculated by N = N-1 * 4 + N-2.

"""

import sys
 


def CalculateSum(maxValue = 4000000):
    # Set initial values
    newValue = 2
    prevValue = 0
    sumValue = 0
    # Calculate the sum until maximum value is reached
    while newValue < maxValue:
        sumValue += newValue
        newValue, prevValue = 4*newValue+prevValue, newValue
    return sumValue


if __name__ == "__main__":
    if len(sys.argv) < 2:
        maxValue = 4000000
    else:
        maxValue = int(sys.argv[1])
    sumOutput = CalculateSum(maxValue)
    print(sumOutput)
    
