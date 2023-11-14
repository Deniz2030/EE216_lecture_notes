# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:48:56 2023

@author: LENOVO
"""
######################################################################
for i in range(10):
    print(i)
    print (10*i)

######################################################################   
for j in range(10):
    print(j)

######################################################################
for i in range(0,10,2):
    print(i)
    print (10*i)

######################################################################
for i in range(10):
    if i%2==0:
        print("modulus is zero")
    else:
        print (i)

######################################################################       
tr_letters = "şçöğüİı"
for letter in tr_letters:
    print(letter)

######################################################################
tr_letters = "şçöğüİı"
pswd = input("Your pwsd: ")
for char in pswd:
    if char in tr_letters:
        print("You can't use Turkish characters in your pswd")
 
######################################################################
i=0;tr_letters = "şçöğüİı"
pswd = input("Your pwsd: ")
for char in pswd:
    if char in tr_letters:
        i=i+1
if i>0:
      print("You have entered {} Turkish characters.\nYou can't use Turkish characters in your pswd".format(i))

######################################################################
#See the deffect when the indent of the second "if" is changed...
i=0;tr_letters = "şçöğüİı"
pswd = input("Your pwsd: ")
for char in pswd:
    if char in tr_letters:
        i=i+1
        if i>0:
            print("You have entered {} Turkish characters.\nYou can't use Turkish characters in your pswd".format(i))
#It becomes too badf now. Do yu know why?
#(Because the second if runs inside the first if due to 
#the indented position of the second "if")
######################################################################

#Evaluate the output of these commands in your mind first. Then run and see
#whether your evaluation is correct or not.
for i in range(10):
    if i%2==0:
        print(i,"-->square: ",i*i)
    elif i%3==0:
        print(i,"-->cube: ",pow(i,3))
    else:
        print (i)
     
######################################################################
#Now see the following:
for i in range(20):
    if i%2==0 and i%3!=0 and i%5!=0:
        print(i,"-->can be divided by 2")
    elif i%2!=0 and i%3==0 and i%5!=0:
        print(i,"-->can be divided by 3")
    elif i%2 !=0 and i%3 !=0 and i%5==0:
        print(i,"-->can be divided by 5")
    elif i%2==0 and i%3==0 and i%5!=0:
        print(i,"-->can be divided by 6: ") 
    else:
        print (i)    
#Better but not so good...

######################################################################
#Let's try the following:
number=int(0);
number=int(input("enter a number between 0 and 22: "));two=0;three=0;five=0;seven=0;
eleven=0;thirteen=0;seventeen=0;nineteen=0;
num=number;
while num%2==0: 
    num=num/2;two+=1
while num%3==0:
    num=num/3;three+=1;
while num%5==0:
    num=num/5;five+=1;
while num%7==0:
    num=num/7;seven+=1;
while num%11==0:
    num=num/11;eleven+=1;
while num%13==0:
    num=num/13;thirteen+=1;
while num%17==0:
    num=num/17;seventeen+=1;
while num%19==0:
    num=num/19;nineteen+=1;
print(number,"can be divided by: 2^{}*3^{}*5^{}*7^{}*11^{}*13^{}*17^{}*19^{}".format(two,three,five,seven,eleven,thirteen,seventeen,nineteen)) 
   
######################################################################
#Now let's do somethng better in the final print command:
number=int(0);
number=int(input("enter a number between 0 and 22: "));two=0;three=0;five=0;seven=0;
eleven=0;thirteen=0;seventeen=0;nineteen=0;
num=number;
while num%2==0: 
    num=num/2;two+=1
while num%3==0:
    num=num/3;three+=1;
while num%5==0:
    num=num/5;five+=1;
while num%7==0:
    num=num/7;seven+=1;
while num%11==0:
    num=num/11;eleven+=1;
while num%13==0:
    num=num/13;thirteen+=1;
while num%17==0:
    num=num/17;seventeen+=1;
while num%19==0:
    num=num/19;nineteen+=1;

del str;
# Note: for numbers we use "variable=None"
# but for strings: "del string name"
str="1"
if two!=0:
    str=str+"*2^"+"%s"%two
if three!=0:
    str=str+"*3^"+"%s"%three
if five!=0:
    str=str+"*5^"+"%s"%five
if seven!=0:
    str=str+"*7^"+"%s"%seven
if eleven!=0:
    str=str+"*11^"+"%s"%eleven 
if thirteen!=0:
    str=str+"*13^"+"%s"%thirteen
if seventeen!=0:
    str=str+"*17^"+"%s"%seventeen
if nineteen!=0:
    str=str+"*19^"+"%s"%nineteen
print(number,"can be divided by: ", str)

######################################################################    

https://www.stechies.com/python-prime-number/

######################################################################
pip install numpy
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
type(arr)
len(arr)
arr.shape
print("Question: Find the positions of the elements that can be divided by 5)
#Let's do it

a=arr.shape
b=np.array(a)
type(a)
type(b)
print(a)
print(b)  #See the difference between a and b
b[0]
for i in range(b[0]):
    for j in range(b[1]):
        print(arr[i,j])

######################################################################

for i in range(b[0]):
    for j in range(b[1]):
        if arr[i,j]%5==0:
           print("index:",i,j,"-->element:",arr[i,j])
          
####################################################################   
#Let's now choose the diagonal elements and define it as an array
#First learn this:
data=[1,2,3,4,5,"Ali"]; xs = ["Mehmet"]
for item in data:
    xs.append(item)
print (xs)    
  

print(b)
np.empty(shape=1)

arr2=np.empty(shape=1)
    for i in range(b[0]):
        for j in range(b[1]):
            if i=j:
           arr2=np.append(arr2,arr[i,j])
print(arr2)
      
          

