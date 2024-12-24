# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 02:56:09 2023

@author: LENOVO
"""


'''
Multiplatform data visualisation library built on Numpy arrays. 
Purpose is to create Matlab-style plots by using Gnuplot with Python.
Gnuplot, by the way, is also a very popular visualisation library (or tool) 
since it can be used with any programming language. http://www.gnuplot.info/
'''
!pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,11);print(x)

plt.plot(x,np.cos(x))
plt.plot(x,np.sin(x));plt.plot(x,np.cos(x))
x=np.linspace(0,10,101);print(x)
plt.plot(x,np.sin(x));plt.plot(x,np.cos(x))

plt.plot(x,np.sin(x-0));plt.plot(x,np.sin(x-1));plt.plot(x,np.sin(x-2))

plt.plot(x,np.sin(x-0),color='blue');plt.plot(x,np.sin(x-1),color='g');plt.plot(x,np.sin(x-2),color='#000000')

plt.plot(x,np.sin(x-0),color='blue');plt.plot(x,np.sin(x-1),color='g');plt.plot(x,np.sin(x-2),color='#FFCC33') 
#See https://www.color-hex.com/color-palettes/   for hexadecimal color codes

plt.plot(x,np.sin(x-0),color='blue');plt.plot(x,np.sin(x-1),color='g');plt.plot(x,np.sin(x-2),color=(0.5,0.5,0.5))

# Matplotlib chetasheets: https://matplotlib.org/cheatsheets/

plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),color='blue',linestyle='dashdot');
plt.plot(x,np.sin(x-4),color=(0.5,0.1,0.3),linestyle='dashdot')


plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),color='blue',linestyle='dashdot');
plt.plot(x,np.sin(x-4),'--g')

plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),color='blue',linestyle='dashdot');
plt.plot(x,np.sin(x-4),'-.r')

plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),color='blue',linestyle='dashdot');
plt.plot(x,np.sin(x-4),'-..g')


plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),color='blue',linestyle='dashdot');
plt.plot(x,np.sin(x-3),'--.r')

plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),'ob'); plt.plot(x,np.sin(x-3),'+b');
plt.plot(x,np.sin(x-4),'*g')

plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),'sr');
plt.plot(x,np.sin(x-4),'Dg')   # See https://matplotlib.org/stable/api/markers_api.html


plt.plot(x,np.sin(x-4),color='red', marker='d')
plt.plot(x,np.sin(x-4),color='red', marker='3')


plt.xlim?


plt.xlim(-15,12);plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');

plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-3),'sr');
plt.plot(x,np.sin(x-4),'.g')


#plt.xlim(-15,12);plt.ylim(-1.5,2.5);The same effect as before, now by plt.axis
plt.axis([-10,12,-1.5,2]);plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),'-.r');
plt.plot(x,np.sin(x-4),'.r')


#add title to plot
plt.axis([-10,12,-1.5,2]);plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),'-.r');
plt.plot(x,np.sin(x-4),'.r');plt.title('my first plot')

#add axes labels
plt.axis([-10,12,-1.5,2]);plt.plot(x,np.sin(x-0),color='blue',linestyle='solid');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),'-.r');
plt.plot(x,np.sin(x-4),'.r');plt.title('my first plot');plt.xlabel('angle');plt.ylabel('functions')

#add legends (we add here only for the first function)

plt.axis([-10,12,-1.5,2]);plt.plot(x,np.sin(x-0),color='blue',linestyle='solid',label='1');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted'); plt.plot(x,np.sin(x-4),'-.r');
plt.plot(x,np.sin(x-4),'.r');plt.title('my first plot');plt.xlabel('angle');plt.ylabel('functions');plt.legend()


#Now we add legend to all functions
plt.axis([-10,12,-1.5,2]);plt.plot(x,np.sin(x-0),color='blue',linestyle='solid',label='1: Sin(x)');plt.plot(x,np.sin(x-1),color='g',linestyle='dashed', label='2:Sin(x-1');
plt.plot(x,np.sin(x-2),color='#FFCC33',linestyle='dotted',label='3:Sin(x-2'); plt.plot(x,np.sin(x-4),'-.r',label='4:Sin(x-3');
plt.plot(x,np.sin(x-4),'.r',label='5:Sin(x-4');plt.title('my first plot');plt.xlabel('angle');plt.ylabel('functions');plt.legend()

plt.scatter?
plt.scatter(x,np.sin(x),color='blue')

x=np.linspace(0,10,10);plt.scatter(x,np.sin(x),color='blue')

x=np.linspace(0,10,40);plt.scatter(x,np.sin(x),color='blue')

x=np.linspace(0,10,40);plt.scatter(x,np.sin(x),color='blue', marker='D')  #https://matplotlib.org/stable/api/markers_api.html

x=np.linspace(0,10,40);plt.scatter(x,np.sin(x),color='blue', marker='d')

x=np.linspace(0,10,40);plt.scatter(x,np.sin(x),color='blue', marker='3')


x=np.linspace(0,10,40);plt.scatter(x,np.sin(x),c='r',s=0.5, marker='D')

x=np.linspace(0,10,40);plt.scatter(x,np.sin(x),c='b',s=10, marker='D')  #c: color, s: size

x=np.linspace(0,10,40);plt.scatter(x,np.sin(x),c='r',s=8.5, marker='D'); plt.scatter(x,np.sin(x-1),c='b',s=8.5, marker='v');
plt.scatter(x,np.sin(x-2),c='g',s=8.5, marker='^')


x=np.linspace(0,10,40);plt.scatter(x,np.sin(x),c='r',s=8.5, marker='D'); plt.scatter(x,np.sin(x-1),c='b',s=8.5, marker='v');
plt.scatter(x,np.sin(x-2),c='g',s=8.5, marker='^'); plt.scatter(x,np.sin(x-2),c='black',s=8.5, marker='s')

