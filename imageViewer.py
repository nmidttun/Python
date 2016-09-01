from numpy import *
import matplotlib.pyplot as plt
from pandas import *
import numpy.fft as fft
from math import *
from os import *

### Set directory

chdir('/Users/NikMidttun/Documents/Python')

### Load and format data

a = loadtxt('blur.txt',dtype=float)

plt.figure(1)
plt.gray()
plt.subplot(211)
plt.imshow(a)



ashp=shape(a)
xrng=arange(1024)
yrng=arange(1024)
sigma=25

gaussian =zeros([1024,1024],float)
gaussian1=zeros([1024,1024],float)
gaussian2=zeros([1024,1024],float)
gaussian3=zeros([1024,1024],float)
gaussian4=zeros([1024,1024],float)

for x in xrng:
    for y in yrng:
        gaussian1[x,y]=np.exp(-(x**2+y**2)/(2*(sigma**2)))
        gaussian2[-x,y]=np.exp(-(x**2+y**2)/(2*(sigma**2)))
        gaussian3[x,-y]=np.exp(-(x**2+y**2)/(2*(sigma**2)))
        gaussian4[-x,-y]=np.exp(-(x**2+y**2)/(2*(sigma**2)))

gaussian = gaussian1 + gaussian2 + gaussian3 + gaussian4


#plt.imshow(gaussian)
#plt.show()

### Process data with fourier transfroms

aFFT = fft.rfft2(a)
gaussianFFT = fft.rfft2(gaussian)
divFFT = aFFT/gaussianFFT
sharp = fft.irfft2(divFFT)

plt.subplot(212)
plt.imshow(sharp)

plt.show()






#    a = loadtxt('blur.txt')
#
#    with open('blur.txt') as file:
#        array2d=[[float(digit) for digit in line.split()] for line in file]
#
#    print(array2d)
