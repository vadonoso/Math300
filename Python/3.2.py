# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def sum(N, x = []):
    
    x_totals = []
    for i in range(len(x)):
        total = 0
        for n in range(N+1):
            total += (((-1)**(n+1))*(1/n))
            
        x_totals.append(total)
        
    plt.plot(x_totals)
    #return x_totals