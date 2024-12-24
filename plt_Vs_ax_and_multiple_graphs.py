# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:46:40 2023

@author: LENOVO
"""



!pip install matplotlib


#https://python-academia.com/en/matplotlib-plt-ax/
#Now a simple plot with matplotlib.pyplot

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi * 4, 100)
y = np.sin(x)

%matplotlib inline #This line is necessary....

plt.plot(x, y)
plt.show()


#Now the same plot with ax
import numpy as np
import matplotlib.pyplot as plt

    #Importing IPython to execute the magic command
from IPython import get_ipython
    #The get_ipython() function can return the current IPython session object. 
    #The session object has functions that can be called to run the magic commands. 
    #The %matplotlib inline command then can be executed using the following code  
session = get_ipython()
session.run_line_magic('matplotlib', 'inline')

x = np.linspace(0, np.pi * 4, 100)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y)
plt.show()


#matplotlib inline issue.... (if we didn't do the following all the ax- use giwould give error...)
# https://www.scaler.com/topics/matplotlib/matplotlib-inline/
from matplotlib import pyplot as plt
import numpy as np

%matplotlib inline

data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
plt.title('%matplotlib inline function')
plt.boxplot(data);  
# https://www.educative.io/answers/what-is-the-randomnormal-function-in-numpy
# https://sparkbyexamples.com/numpy/how-to-use-numpy-random-normal-in-python/
# For random.normal(... ): https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html

#for sorted-command: it sorts in an ascending order: https://www.geeksforgeeks.org/python-sorted-function/

#A very simple example on boxplot:
# Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)
 
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(data)
 
# show plot
plt.show()


#Another boxplot example:
# Creating dataset
np.random.seed(10)
 '''
 The numpy random seed is a numerical value that generates a new set or repeats pseudo-random numbers. 
 The value in the numpy random seed saves the state of randomness. 
 If we call the seed function using value 1 multiple times, the computer displays the same random numbers.
 The seed() method is used to initialize the random number generator. 
 The random number generator needs a number to start with (a seed value), to be able to generate a random number. 
 By default the random number generator uses the current system time.
 can take values from 0 and 2**32 - 1.
 '''
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]
 
fig = plt.figure(figsize =(10, 7))
 
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])
 
# Creating plot
bp = ax.boxplot(data)
 
# show plot
plt.show()

  
#MATPLOTLIB INLINE FOR SPYDER
import numpy as np
import matplotlib.pyplot as plt

from IPython import get_ipython
session = get_ipython()
session.run_line_magic('matplotlib', 'inline')


x = np.linspace(0, 20, 1000)
y = np.sin(x)

fig, ax = plt.subplots()


line1, = ax.plot(x, y,
        label='Using set_dashes()')
line1.set_dashes([2, 2, 10, 2])   ## 2pt line, 2pt break, 10pt line, 2pt break

line2, = ax.plot(x, y - 0.2, dashes=[6, 2],
        label='Using the dashes parameter')

ax.legend()   #try also this: ax.legend(loc='lower left')
plt.show()

https://towardsdatascience.com/a-beginners-guide-to-creating-clean-and-appetizing-python-charts-f7e1cf1899d2

#you can study "lin1,=" from here: https://stackoverflow.com/questions/65337288/line-ax-plotx-y
#namely,
lst = [1, 2, 3]
first, second, third = lst    # first == 1, second == 2, third == 3; "unpacking" a list

lst = [1, 2]                  
first, second = lst           # first == 1, second == 2

list = [1]
first, = list                  # first == 1

first = list                   # first == [1]   # not the same as previous

#Another example:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi * 4, 100)
y = np.sin(x)

plt.plot(x, y)

plt.xlabel('X', labelpad = 20, weight ='bold', size = 18, color ='black')
plt.ylabel('Y', labelpad = 20, weight ='bold', size = 18, color ='black')

plt.xlim(0, np.pi * 4)
plt.ylim(-1, 1)


plt.xticks(np.arange(0, np.pi*5, np.pi),['0', 'π', '2π', '3π', '4π'])
plt.yticks([-1, -0.5, 0, 0.5, 1])

plt.minorticks_on()

plt.grid(which = 'major', color='black' )
plt.grid(which = 'minor', color='gray', linestyle='--')

plt.show()



#Now the same graph with ax

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi * 4, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize = (8,6))

ax.plot(x, y)

ax.set_xlabel('X', labelpad = 20, weight ='bold', size = 18, color ='black')
ax.set_ylabel('Y', labelpad = 20, weight ='bold', size = 18, color ='black')

ax.set_xlim(0, np.pi * 4)
ax.set_ylim(-1, 1)

ax.set_xticks(np.arange(0, np.pi*5, np.pi))
ax.set_xticklabels(['0', 'π', '2π', '3π', '4π'])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])

ax.minorticks_on()

ax.grid(which = 'major', color='black' )
ax.grid(which = 'minor', color='gray', linestyle='--')

plt.show()


#Now lets learn 2 row-figures:
    #https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

    #a single fig first to see
        
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A single plot')
    #Now 2 figures:
        #vertically:
fig, axs = plt.subplots(2)  #2 rows ax[0] for the first row and ax[1] for the second.}
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)
        #horizontally:
fig, (ax1, ax2) = plt.subplots(1, 2) #1 row and 2 columns, ax1 defined for the first column and ax2 for the second.
fig.suptitle('Horizontally stacked subplots')
ax1.plot(x, y)
ax2.plot(x, -y)

    #following is also possible for the horizontalcal one
fig, ax = plt.subplots(1,2) #1 row and 2 columns, ax1 defined for the first column and ax2 for the second.
fig.suptitle('Horizontally stacked subplots')
ax[0].plot(x, y)
ax[1].plot(x, -y)


#Now 2 by 2 figure arrays:


ax=0; x = np.linspace(0, 2 * np.pi, 400);y = np.sin(x ** 2)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
    
    
    
  #Following is another alternative:
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle('Sharing x per column, y per row')
ax1.plot(x, y)
ax2.plot(x, y**2, 'tab:orange')
ax3.plot(x, -y, 'tab:green')
ax4.plot(x, -y**2, 'tab:red')

for ax in fig.get_axes():
    ax.label_outer()
    #Axes.label_outer() means: Only show "outer" labels and tick labels.
    
   #Sharing axes:
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Axes values are scaled individually by default')
ax1.plot(x, y)
ax2.plot(x + 1, -y) 


        #You can use sharex or sharey to align the horizontal or vertical axis.
fig, (ax1, ax2)=plt.subplots(2, sharex=True)
fig.suptitle('Aligning x-axis using sharex')
ax1.plot(x, y)
ax2.plot(x + 1, -y)
fig.show()

    
    #Another 2 by 2 example:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2, 2)
x = np.linspace(0, 8, 1000)

ax[0, 0].plot(x, np.sin(x), 'g') #row=0, col=0
ax[1, 0].plot(x, np.tan(x), 'k') #row=1, col=0
ax[0, 1].plot(range(100), 'b') #row=0, col=1
ax[1, 1].plot(x, np.cos(x), 'r') #row=1, col=1
fig.show()



print(matplotlib.__file__)
print(matplotlib.__version__)


 #HW:
     
# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math  
ax=0; x = np.linspace(0, 2 * np.pi, 400);y1 = np.sin(x);y2=np.cos(x);


# Using Numpy to create an array X
X = np.arange(0, math.pi*2, 0.05)

# Assign variables to the y axis part of the curve
y = np.sin(X)
z = np.cos(X)

# Plotting both the curves simultaneously
plt.plot(X, y, color='r', label='sin')
plt.plot(X, z, color='g', label='cos')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Angle")
plt.ylabel("Magnitude")
plt.title("Sine and Cosine functions")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
plt.show()


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle('Plots of the given functions')
ax1.plot(x, y)
ax2.plot(x, y**2, 'tab:orange')
ax3.plot(x, -y, 'tab:green')
ax4.plot(x, -y**2, 'tab:red')

for ax in fig.get_axes():
    ax.label_outer()
    #Axes.label_outer() means: Only show "outer" labels and tick labels.
    
    
    #Axes.flat
    #flat means a 1D iterator over the array. 
#If you have to set parameters for each subplot it's handy 
#to iterate over all subplots in a 2D grid using for ax in axs.flat:.

import matplotlib.pyplot as plt
import numpy as np
import math 
x = np.arange(0, math.pi*3, 0.05)
y = np.sin(x)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
    
x
#flat means a 1D iterator over the array.    
# let's see it:
a = np.array([[2,3],
              [4,5],
              [6,7]])
print(a)
for i in a.flat:
    print(i)

for i in enumerate(a.flat):  #see the difference, each element is a row-wise enumrated...
    print(i)
#...

import matplotlib.pyplot as plt
x = np.arange(0, math.pi*3, 0.05)
y = np.sin(x)

fig, axes = plt.subplots(ncols=2,nrows=3, sharex=True, sharey=True)

for i, ax in enumerate(axes.flat):  
    #For each iteration it yields the next axes from that array, 
    #such that you may easily plot to all axes in a single loop.
    ax.scatter([i//2+1, i],[i,i//3])  #x//y is a floor division
    print(i,ax)
    ax.grid(True)
plt.show()
x
y
#A very nice explanation with for enumerate loop: 
   #https://www.geeksforgeeks.org/enumerate-in-python/
   #https://realpython.com/python-enumerate/
print(list("hello"))
# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))    
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, axes = plt.subplots(nrows=2, ncols=3)
x = np.random.rand(10)
y = np.random.rand(10)
for _, ax in enumerate(axes.flat):
   ax.plot(x, y)
plt.show()


#Potting from dataframes (very important):
https://pythonguides.com/python-plot-multiple-lines/

#see also this: 
    # https://www.tutorialspoint.com/how-do-you-create-line-segments-between-two-points-in-matplotlib
    # https://datatofish.com/line-chart-python-matplotlib/
    # https://www.geeksforgeeks.org/matplotlib-axes-axes-plot-in-python/
    # https://stackabuse.com/matplotlib-line-plot-tutorial-and-examples/    (we can omit x axis)
    # https://www.w3schools.com/python/matplotlib_line.asp
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html  (numpy details here...)
z=np.random.randint(4, [5, 6, 7]);z



import matplotlib.pyplot as plt

#define figure
fig = plt.figure()

#add subplots
fig.add_subplot(331).set_title('321')
fig.add_subplot(312).set_title('323')
fig.add_subplot(339).set_title('325')
##fig.add_subplot(142).set_title('022')

#display plots
plt.show()

#ex2

fig = plt.figure()

#add subplots
fig.add_subplot(322).set_title('321')
fig.add_subplot(334).set_title('323')
fig.add_subplot(313).set_title('325')
##fig.add_subplot(142).set_title('022')

#display plots
plt.show()


#ex3
fig = plt.figure()

#add subplots
fig.add_subplot(322).set_title('321')
fig.add_subplot(347).set_title('323')
fig.add_subplot(313).set_title('325')
##fig.add_subplot(142).set_title('022')

#display plots
plt.show()

#ex4a
x=np.linspace(0,5*np.pi,100);S=np.sin(x);C=np.cos(x)
fig = plt.figure()
f, axes = plt.subplots(1, 3)    # 1 row and 3 columns

# Using subplot 
axes[0].plot(x, C, '.')
axes[0].set_ylabel('Cos')

axes[1].plot(x, S, '-')
axes[1].set_ylabel('Sin')

axes[2].plot(x, S+0.1, 'o')
axes[2].set_ylabel('MSin')

#Ex4b
plt.clf()  # clear the plot
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5*np.pi,100);S=np.sin(x);C=np.cos(x)
fig = plt.figure()

ax=fig.add_subplot(131)
ax.plot(x, C, '.')

ax=fig.add_subplot(133)
ax.plot(x, S)

#Ex4c
plt.clf()  # clear the plot
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5*np.pi,100);S=np.sin(x);C=np.cos(x)
fig = plt.figure()

sub1=plt.subplot(131)
sub1.plot(x, C, '.')
sub3=plt.subplot(133)
sub3.plot(x, S)