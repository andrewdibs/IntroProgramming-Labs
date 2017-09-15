#pi.py
#Author: Andrew DiBella
#Date: 15 September 2017

import math

def main():

    n = int(input("Enter number for nth term to approximate Pi: "))
    approx = 0
    sign = 1
    for i in range(1,2*n,2): 
        
        approx =  approx +sign * (4/i)
        sign=-sign
            
        
        
    print("Approximation: "+ str(approx))
    print("Accuracy difference:" + str((math.pi - approx)))

main()
