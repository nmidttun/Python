# Nikolas Midttun #

# Import Modules #

from numpy import *
import matplotlib.pyplot as plt
from pandas import *
import numpy.fft as fft
from math import *
from os import *

# Set directory #

chdir('/Users/NikMidttun/Documents/Python')

# Code #

BHE = read_csv('BHE.txt')

time = linspace(0,len(BHE)-1,len(BHE))
freq = 1/time

fftBHE = fft.fft(BHE)

fftAbsBHE = abs(fftBHE)

plt.plot(time, BHE)
plt.show()


plt.plot(freq, fftAbsBHE)
plt.show()
