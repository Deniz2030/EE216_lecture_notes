# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
alist=[1,1.3,2,3,5,7,9.4,'Ali'] #define a python list
print(type(alist))
print(alist)
a1=np.array([1,2.3,4,5,8.9])
print(type(a1)) #define a numpy array in 1D (row matrix)
print("Array is of type: ", type(a1))
print("Our np-rray is: ", a1)
a2=np.array([[1],[2],[3],[4],[5],[8.9]]) #define a numpy array in 1D (column matrix)
print(a2)
a3=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) #define a numpy array (a 4 by 3 matrix)
print(a3)
a4=np.eye(5, 5,  0, dtype = float)
print(a4)
a5=np.eye(5, 5,  -1, dtype = float)
print(a5)
a6=np.eye(5, 5,  -3, dtype = float)
print(a6)
a7=np.array([1,2,3, 0], dtype = 'float64') #another example for array construction in real elements
print(a7)
a8=np.array([1.2,2.,3.7, 0.5], dtype = 'int16') #another example for array construction in integer elements
print(a7)
a9=np.zeros(10);print(a9)  #construct a zero raw matrix (row involves 10 columns)
a10=np.zeros([4,3]);print(a10)  #construct a zero 4 by 3 matrix
a11=np.full(8,7);print(a11) #construct a full raw matrix (row involves 8 columns with elements 7)
a11=np.full(8,7,dtype = 'float64');print(a11) #Now in real elements
a13=np.full([4,3],7);print(a13) #construct a full 4 by 3 matrix (with elements 7)
#Now some matrix constructions with specific arrangements#
np.arange(10)
a14=np.arange(0,10,2);print(a14)  #array-arrange starting from 0 up to 10 by 2 increments
a15=np.linspace(0,10,21);print(a15)  #linear space starting from 0 up to 10 with a total of 21 elements
a16=np.random.random((3,4));print(a16)  #costruct a 3 by 4 random matrix. 
#Note that default definition of random values are between 0 and 1###
a17=np.random.randint(10,20,15);print(a17) #Now define random integer of 15-element row matrix 
#with elements between 10 and 20-1=19. Note that last value=20 is not included
a18=np.random.randint(10,20,[5,6]);a18  # Now the same but in a 5 by 6 matrix
#let's see the shape and dimension of it
a18.shape     #it's a 5 by 6 matrix
a18.ndim      # it is in 2D
#diagonal matrix again (a review with examples)
a19=np.eye(5,4);a19
a20=np.eye(5,4,-2);a20  #negative sign in -2 indicates row-wise shift (lower-diagonal)
a21=np.eye(5,5);a21
a22=np.eye(5,5,1);a22 #positive sign in +1 indicates column-wise shift (upper-diagonal)
#See https://www.geeksforgeeks.org/numpy-eye-python/  for detailed explanation
#Now selections of parts of constructed matrices... (very important)...
a23=np.arange(1,30,2);a23 #construct our row array first
a24=a23[0:5:1];a24 #We select i=0 and j=5th element (indices start from 0 not from 1, 
# and the 5th element is not included !!!!)
a25=a23[0:5:2];a25
a26=a23[0::1];a26
a27=a23[:6:1];a27
a28=a23[::-1];a28
a29=a23[:6:-1];a29   #i1 indicates reverse order from right to he left
a30=a23[:6:-2];a30
#Let's now do it for the column matrises
a31=np.array([np.arange(1,30,2)]).transpose();a31 #construct our column array first
a32=a31[0:5];a32 #select column elements between 0th and 4th elements(the 5th is not included)
a33=a31[3:5];a33 #select column elements between 3rd and 4th elements(the 5th is not included)
a34=a31[:4];a34 #select column elements between 0th and 3rd elements(the 4th is not included)
a35=a31[3:];a35 #select elements from indice 3 to all
a36=a31[3::-1];a36 #select elements from indice 3 to all but in the reverse order
#some examples in m by n matrices...
a37=np.random.randint(10,100,[7,7])
a37  #construction first
a37[0,5]   #We select i=0 and j=5th element (indices start from 0 not from 1 !!!!)
a37[3,4]   #We now select i=3 and j=4th element
"""our formula for row-wise selection: a23[start:stop:step]----
Defaıult value of start is 0 and stop value is not included"""
a37[0:4:2]
a37
a37[:4:2]   #select the ows between i=0,2, and 4 (the 4th one is not included)
"""Formula: array[r-start:r-stop:r-increment,c-start:c-stop:c-increment], 
here r-:row, c-:column(stops are not included)"""
a37[1:3:1]   #another example (first 2 rows are selected-stop index is not included!!!)
a37[1:3,2:4] #select row 1,2 and column 2,3 (rw3 and colum 4 is not included)
a37[2:6:3,4:7]    #select row 2,5 and column 4,5,6 (row 6 and column 7 is not included)
a37
a37[1:3:1,::-1]
a37[::-1,]    #All rows are reversed
a37[::-1]    #The same
a37[::,::-1] #All columns are reversed
a37[5:3:-1,::] # from row 5 to row 3 in the reverse direction (end point row 3 is not included''')
a37[::,6:2:-2]   #from column 6 to 2 (end point 2 is not included!) with step 2
#Now some matrix operations
a38=np.array([[1,2],[3,4]]);a39=np.array([[1,0],[2,5]])
a40=np.eye(2);a40
2*a40
a41= np.dot(a38,a39);a41  #dot product formula: #dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
a41=a38*a39;a41 #elementwise product
a42=np.multiply(a38,a39);a42 #the same as before
print ("the transpose of a38={0} is {1}".format(a38,a38.transpose()) )
print ("the inverse of a38={0} is {1}".format(a38,np.linalg.inv(a38)) )
a43=np.linalg.inv(a38);a43
#proof that a43 is the inverse o a38 is as follows
np.dot(a38,a43)
#now lets calculate the determinant
a38
from numpy import linalg as adu; adu.det(a38)  
np.linalg.det(a38)   #or like thisss
#now power of a matrix
a38
pow(a38,2)  #elementwise product(not matrix square)
np.power(a38,2)
#proof
np.dot(a38,a38)
#A complicated example on shaping matrices
a43=np.array([[1,2,3,4,5,6,7,8,9],[0,1,2,0,3,0,0,1,0],[0,1,0,1,1,0,1,2,0],[1,0,0,0,0,1,1,0,0]]);a43
a44=a43[::,0:4:2];a44
a45=a43[0:5,:2].transpose();a45
a46=np.dot(a44,a45);a46
a47=np.dot(a43[::,0:4:2],a43[0:5,:2].transpose());a47 #a47 is the same as a46
a48=a47.transpose();a48 #transpose of a47
a49=np.linalg.inv(a46);a49 #find inverse of a46 or 47 gives no result here because it is a singular matrix (det=0)
a50=a43[3:0:-1,0:3];a50
a51=np.linalg.inv(a50);a51 #find inverse of a50
#for proof:
np.dot(a51,a50)
#NOW RESHAPE COMMAND----VERY IMPORTANT!!!
a52 = np.arange(6);a52
a52.reshape((3, 2))
np.reshape(a52, (2, 3))
 # C-like index ordering
a53 = np.array([[1,2,3], [4,5,6]]);a53
a54=np.reshape(a53, 6);a54
a53.shape
a54.shape
a55= np.array([[2,3,4], [5,6,7]]);a55   
a56=np.reshape(a55, (3, 2));a56
    #See the following wep page https://www.w3resource.com/numpy/manipulation/reshape.php
    #and https://geekflare.com/numpy-reshape-arrays-in-python/
    # and https://towardsdatascience.com/reshaping-numpy-arrays-in-python-a-step-by-step-pictorial-tutorial-aed5f471cf0b
    #Use of -1 is as follows: 
"""Use -1 for at most one dimension in the new shape 
if you would like the dimension to be automatically inferred."""
a57=np.arange(20) ;a57       
# But let' suppose we wish to rehape it to 4 by 3 now
np.reshape(a57, (4,3))   # it gives error since we have totally 20 elements but 4 by 3 has 12 elements
np.reshape(a57, (4,6))   # similarly we can't reshape a 1 by 20 matrix to a 4 by 6!!!!
#But we use -1 to let numpy determine the column number
a58=np.reshape(a57, (4,-1));a58
#it is just the same as follows:
a59=np.reshape(a57, (4,5));a59
#Similarly:
a60=np.reshape(a57, (2,-1));a60
a61=np.reshape(a57, (2,-2));a61
a62=np.reshape(a57, (2,-3));a62
a64=np.reshape(a57, (2,-7));a64  # all are the same
a65=np.reshape(a57,[5,-1]);a65            
a66=np.reshape(a57,[5,-9]);a66 
a67=np.reshape(a57,[5,4]);a67  # all the last three ones are the same 
# note the folowing synta is gives the same result
a68=a57.reshape(5,4);a68
a69=a57.reshape(5,-1);a69
#How to create a column matrix by using reshaoe
a70=np.arange(10).reshape((10, 1));a70
np.array([np.arange(1,10)]).transpose()
np.array([np.arange(1,30,2)]).transpose()   #see a31 above
#NOW VSTACK AND HSTACK
#See the following web page: https://www.geeksforgeeks.org/numpy-hstack-in-python/
# # Python program explaining
# hstack() AND vstack()function
#EXAMPLE1
import numpy as np
# input array
in_arr1 = np.array([ 1, 2, 3] )
print ("1st Input array : \n", in_arr1)

in_arr2 = np.array([ 4, 5, 6] )
print ("2nd Input array : \n", in_arr2)

# Stacking the two arrays horizontally
out_arr_hor = np.hstack((in_arr1, in_arr2))
print ("Output horizontally stacked array:\n ", out_arr_hor)
# Stacking the two arrays verticaltally
out_arr_ver = np.vstack((in_arr1, in_arr2))
print ("Output vertically stacked array:\n ", out_arr_ver)
#EXAMPLE2
# Python program explaining
# hstack() and vstack) function

import numpy as np

# input array
in_arr1 = np.array([[ 1, 2, 3], [ -1, -2, -3]] )
print ("1st Input array : \n", in_arr1)

in_arr2 = np.array([[ 4, 5, 6], [ -4, -5, -6]] )
print ("2nd Input array : \n", in_arr2)

# Stacking the two arrays horizontally
out_arr_hor = np.hstack((in_arr1, in_arr2))
print ("Output stacked array :\n ", out_arr_hor)
# Stacking the two arrays vertically
out_arr_ver = np.vstack((in_arr1, in_arr2))
print ("Output stacked array :\n ", out_arr_ver)
