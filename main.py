# This is a sample Python script.

'''Graph plotting code for functions.
XY plot
X axis range in integers'''

import matplotlib.pyplot as plt
#from matplotlib import rc
from matplotlib.ticker import MultipleLocator
import numpy as np


#################SAMPLE SPACE#######################
fig, ax = plt.subplots()
######Function Range############
xrange = [-10, 10]
#yrange = [-100, 100]
x = np.linspace(xrange[0], xrange[1], 200000)
plt.axhline(y = 0, color = 'k', linestyle = '-')
plt.axvline(x = 0, color = 'k', linestyle = '-')
##########Function###########
function = [[5*x**3,'$y=5x^3$'],[15*x**2,'$y=15x^2$'] ]
#function_label = ['$y=x^2$', '$y=x^3$']

def fctn(function, xrange):
    i = len(function)
    #x = np.linspace(xrange[0], xrange[1], 200000)
    for y in function:
        x = np.linspace(xrange[0], xrange[1], 200000)
        ax.plot(x, y[0],label = y[1])

        plt.legend()

        #print(y)
    return plt.show()
plt.grid()
fctn(function,xrange)
