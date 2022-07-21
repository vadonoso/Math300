# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt

def sum2(N, x = []):

    x_totals = []
    for i in range(len(x)):
        total = 0
        for n in range(N+1):
            total += (((x[i]**n))/(n))
        
        x_totals.append(total)
        
    plt.plot(x,x_totals)
    #return x_totals
        
        