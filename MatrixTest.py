from numpy import *
import matplotlib.pyplot as plt
from pandas import *
import numpy.fft as fft
from math import *
from os import *

# Set Directory #

chdir('/Users/NikMidttun/Documents/Python')

# Test #

a = zeros([5,5],int)


print(a)

a[2,0] = 999

print(a)
