#!/usr/bin/env python
# coding: utf-8
print("I have %d pens" %3)
print("%d pen cost %dTL" %(3,12))

print("%d pen cost %.2fTL" %(3,12.3578999))

print("%d pen cost %fTL" %(3,12.3578999))

print("%d pen cost %.7fTL" %(3,12.3578999))
print("%d pen cost %.7fTL" %(3,12.35789997))

print("%9.5f" % 5.1234567890) 
#Total 9 digits (including dot), 5 digits after dot
#and 4 digits for the decimal part (including dot)...

print("%9.5f" % 1234567890.1234567890)
#Total 9 digits (including dot), 5 digits after dot (4 digits for decimals). 
#But decimal digits are more than 4. 
#So all the decimals will be shown...

# THE USE OF F-STRINGS.......
age = 20
python_version = 3.8
print(f'Your age is {age}')
print(f'python_version={python_version}')
print(f'{age=}')
print(f'{python_version=}')
'''
Syntax: {:[width][.precision][type]}
Type:
d: integers
f: floating point numbers
*You need to specify precision only in case of floating point numbers
Study it from here:  
    https://towardsdatascience.com/a-simple-guide-to-string-formatting-in-python-using-f-strings-39e5c39589c3
'''

#...

'''If we want to add 6 blank spaces and align our text to the right, 
we only need to add a width of 8 (the default behavior is to align the text to the right)
'''
number = 20
print(f'{number}')
print(f'{number:8}')
print(f'{number:>8}')   #Align to the right (width=8)
print(f'{number:_>8}')  #Align to the right (width=8)
print(f'{number:#>8}')  #Align to the right (width=8)
print(f'{number:#>20}')  #Align to the right (width=8)
print(f'{number:<8}')    #Align to the left  (width=8)
print(f'{number:_<8}')   #Align to the left  (width=8)
print(f'{number:$<8}')   #Align to the left  (width=8)
print(f'{number:$<20}')   #Align to the left  (width=8)
#We use _ as our padding above

x = 20.123
#Right padding with zeros
print(f'{x:0<8}')
print(f'{x:c<8}') 
print(f'{2.7:6f}')
print(f'{2.7:X>10.6f}')
'''
This is cool, but sometimes using the width makes things complicated because we have to calculate the final width 
of our number after adding the 0's.
It’s simpler to think of the number of decimals we want instead.
We can get this using .precision from the syntax shown before. Let’s add 0’s until we have 5 decimals.
'''
print(f'{x:.5f}')
print(f'{x:10.5f}')
print(f'{x:z>10.5f}')
print(f'{x:z<10.5f}')
#let's now write 01.03.2023 by using a=1, b=3, and c=2023

#Left padding with zeros
'''
Now let’s add 0’s to the left. This is very useful when we need to create customized formats using numbers.
Say we want to obtain the following format: YYYYMMDD and we have regular numbers from 1–9. 
In this case, we’ll need to add 0’s to the left to the month and day.
Here are the 2 ways to do this with f-string.
'''
year = 2022;month = 1;day = 5

# YYYYMMDD
print(f'{year}{month:0>2}{day:0>2}')
print(f'{year}{month:02d}{day:02d}')
print(f'{year}.{month:02d}.{day:02d}')
print(f'{year}.{month:02d}.{day:02d}')
print("year=%d month=%d day=%d" %(year, month, day))
print("year=%d month=%02d day=%02d" %(year, month, day))
print(f'{month:02d}')
print(f'{month:02f}') #Total 2 digits and default precision is 6 digits...
print(f'{month:10f}') #Total 10 digits and default precision is 6 digits...
print(f'{month:X>10.7f}') #See below (total digit number=10, prec is 7)
print(f'{month:X>7.3f}') #See below
'''
Round float to “n” decimals
When it comes to rounding fload numbers to “n” decimals, it’s more practical to use the .precision with f type.
Let’s round the number below to 1 decimal.
'''
x = 20.123; print(f'{x:.1f}')
print(f'{x:.5f}')
print(f'{x:_<10.4f}')
print(f'{x:_>10.4f}')
print(f'{x:A>10.4f}')


print(f'{1234.17:12.3f}')
print(f'{1234.17:X>12.3f}')


print(f'{x:Y<10.4f}')
print(f'{x:Y>10.4f}')
print(f'{x:10.4f}') #default is right aligned...


#Also study from here: https://zetcode.com/python/fstring/

#Now some more examples on various expressions of print functions with f-strings....

s1='Mehmet'; s2='Akif'; s3='Ersoy';birth=1873;death=1936; print("%s %s %s was born in %d and died in %d" %(s1,s2,s3,birth,death))

print(s1+s2+s3,'was born in' ,birth,'and died in',death)

print("Sunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday") # /n means go to a new line

print("%.5f" % 5.1234567890)

#(Here we do slicing strings)
(ss1,ss2,ss3,bbirth,ddeath)='Mehmet','Akif','Ersoy',1873,1936
print(ss1+ss2+ss3,'was born in' ,bbirth,'and died in',ddeath)
var1="It’s Sunday"
var2 = "Have a great day";
var3 = var1[:5] + var2[5:13] + var1[5:];
print(var3)
var4=var1[:5] + var2[5:13] + var1[8:];
print(var4)
len(var1)

'Sam has {0} red balls and {1} yellow balls'.format(12, 31)

'Sam has {1} red balls and {0} yellow balls'.format(12, 31)
#Burada kaldık...Perşembe buradan devam edilecek...

# Python program showing how to use
# string modulo operator(%) to print
# fancier output
# format:  %[flags][width][.precision]type 

# print integer and float value
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))
print("Total students : %3d, Boys : %5d" % (240, 120)) # attention:3 blanks on the left of 120

# print octal value
print("%7.3o" % (25))
print("%5.3o" % (25))
print("%7.2o" % (25))
# print exponential value
print("%10.3E" % (356.08977))
print("%9.3E" % (356.08977))
print("%15.3E" % (356.08977)) #☻see the differences (blanks on the left)

# using format() method
print('I love {} and "{}!"'.format('Aydin', 'Adu'))

# using format() method and referring
# a position of the object
print('{0} and {1}'.format('Aydin', 'Adu'))

print('{1} and {0}'.format('Aydin', 'Adu'))


# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.

# Expressions of Integers in binary, octal, Hexadecimal, and E-forms
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

String1 = "{0:o}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

String1 = "{0:x}".format(16)
print("\nHexadecimal representation of 16 is ")
print(String1)

String1 = "{0:x}".format(31)
print("\nHexadecimal representation of 31 is ")
print(String1)


String1 = "{0:X}".format(31)  #♥ in big charactersssss
print("\nHexadecimal representation of 31 is ")
print(String1)


# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)


#Study also th followings (Very important!!!): 
    https://www.numpyninja.com/post/how-to-format-strings-using-print-in-python

print(f"I love {'Adu'} in \"{'Aydin'}!\"")    
#Above: Pay attention that \" means a quotation mark inside double quotation marks.

# using format() method and referring
# a position of the object
print(f"{'Aydin'} and {'Adu'}")

# Python program showing
# a use of format() method

# combining positional and keyword arguments
print('{0} is a university in {1}, which is a city in the west of {other}.'.format('Adu', 'Aydin', other ='Turkey'))

# using format() method with number
print("Adu :{0:2d}, Portal :{1:8.2f}".format(12, 00.546))
print("Adu :{0:4d}, Portal :{1:8.2f}".format(12, 00.546))
print("Adu:{0:4d}, Portal :{1:4.2f}".format(12, 00.546))
print("Adu :{0:4d}, Portal :{1:Z>8.2f}".format(12, 00.546)) #See the differences...
print("Numberplate of Aydın :{0:4d}, Telephone code of Aydin:{1:0>5.3f}".format(9, 00.256)) 
print("Numberplate of Aydın :{0:0>2.0f}, Telephone code of Aydin:{1:0>5.3f}".format(9, 00.256))#See the differences...
print("Numberplate of Aydın :{0:0>2d}, Telephone code of Aydin:{1:0>5.3f}".format(9, 00.256)) #See the differences...
# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))
print("Second argument: {1:3d}, first one: {0:$>7.2f}".format(47.42, 11))
print("Second argument: {1:3d}, first one: {0:$>7.4f}".format(47.42, 11))
print("Second argument: {1:3d}, first one: {0:$>10.2f}".format(47.42, 11)) #See the differences...
print("Geeks: {a:5d}, Portal: {p:8.2f}".format(a = 453, p = 59.058))

# Python program to
# format a output using
# string() method
 
cstr = "I love Adu in Aydin in Turkey"
len(cstr)   #Number of characters (lenth of cstr)
# Printing the center aligned 
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
 
# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
 
# Printing the right aligned string
# with "-" padding 
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))


#Now slicing texts.... (very important)......

"""String Slicing
To access a range of characters in the String, the method of slicing is used. 
Slicing in a String is done by using a Slicing operator (colon). """

cstr = "I love Adu in Aydin in Turkey"
print("Initial String: ")
print(cstr)
# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(cstr[3:12]) # last value (12th value) is not included...
print(cstr[0:10]) # last value (10th value) is not included...
print(cstr[0:6]+' '+cstr[23:29])
# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " + "7th and 10th last character: ")
print(cstr[7:-10])

print(cstr[::-1])  #reversing a string

# Reverse the string using reversed and join function
new = "".join(reversed(cstr))
print(new)

# Python Program for
# Formatting of Strings

# Default order
String1 = "I love {} in {} {} of {}".format('Adu', 'Aydin', 'in the west', 'Turkey')
print("Print String in default order: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])



# Positional Formatting
String1 = "{1} {0} {2} {3}".format('Adu', 'Aydin', 'in the west', 'Turkey')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{Ad} is in {Ay} and it is {i} of {T}.".format(Ad='Adu', Ay='Aydin', i='in the west',T='Turkey')
print("\nPrint String in order of Keywords: ")
print(String1)





