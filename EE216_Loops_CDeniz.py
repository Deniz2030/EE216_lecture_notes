# 

inp = """
(1) add
(2) subtract
(3) multiply
(4) divide
(5) square
(6) square root
(7) modulus
Enter q for quitting...
"""
print(inp)
# Remember also the following:
inp = "(1) add \n(2) subtract \n(3) multiply \n(4) divide \n(5) square \n(6) square root\n(7) modulus\nEnter q for quitting..."
print(inp)

while True:
    operation = input("Enter the number of the operation you want: ")
   
    if operation == "q":
        print("quitting...")
        break

    elif operation== "1":
         num1 = int(input("Enter the first number for addition: "))
         num2 = int(input("Enter the second number for addition: "))
         print(num1, "+", num2, "=", num1 + num2)

    elif operation== "2":
         num3 = int(input("Enter the first number for subtraction: "))
         num4 = int(input("Enter the second number for subtraction: "))
         print(num3, "-", num4, "=", num3 - num4)

    elif operation == "3":
         num5 = int(input("Enter the first number for multiplication: "))
         num6 = int(input("Enter the second number for multiplication: "))
         print(num5, "x", num6, "=", num5 * num6)

    elif operation == "4":
         num7 = int(input("Enter the first number for division:  "))
         num8 = int(input("Enter the second number for division: "))
         print(num7, "/", num8, "=", num7 / num8)

    elif operation== "5":
         num9 = int(input("Enter the number whose square will be calculated: "))
         print("Square of ", num9, " = ", num9 ** 2)

    elif operation == "6":
         num10 = int(input("Enter the number whose square-root will be calculated: "))
         print("Square-root of ", num10, " = ", num10 ** 0.5)
    elif operation == "7":
          num11 = int(input("Enter the first number for calculation of modulus: "))
          num12 = int(input("Enter the second number for calculation of modulus: "))
          print("modulus of ", num11, " and ", num12, "=", num11 % num12)

    else:
         print("Wrong input.")
         print("Enter one of the operations below:", inp)
        
#############################################################################

a = 0

while a < 100:
    a += 1
    if a % 2 == 0:
        print(a)        

#############################################################################     
        
repeat = 1
while repeat <= 3:
    print("repeat: ", repeat)
    repeat += 1
    a=input("How are you, are you fine? (0 or 1): ")
    print("bool result of answer: ", bool(int(a)))
    print("bool result of index: ", bool(repeat <= 3))      

bool(1)

#############################################################################
tr_letters = "şçöğüİı"

for letter in tr_letters:
    print(letter)
    
#############################################################################

tr_letters = "şçöğüİı"

pswd = input("Your pwsd: ")

for char in pswd:
    if char in tr_letters:
        print("You can't use Turkish characters in your pswd")

#############################################################################

for i in range(3):
    pswd = input("Determine your pswd: ")
    if not pswd:
        print("You have to determine your paswd!")

    elif len(pswd) in range(3, 8):
        print("Your bew pswd", pswd)
        break

    elif i == 2:
        print("You entered invalid pswd in 3 times.",
        "Please try again 30 minutes later!")

    else:
        print("Pswd should not be more than 8 and less than 3 characters...")
    
#############################################################################
for i in range(0, 10, 2):
    print(i)

#############################################################################

for i in range(10, 0, -1):
    print(i)
    
#############################################################################
while True:
    pswd= input("Please determine your pswd: ")
    if len(pswd) < 5:
        print("Pswd should not be less than 5 characters!")
    else:
        print("Your pswd has been accepted!")
        break
#############################################################################
while True:
    s = input("Enter a number (or q for quit): ")
    if s == "q":
        break

    if len(s) <= 3:
        continue

    print("You can enter a number with maximum 3 digits.")
    
#############################################################################

%run bubble_sort.py
!pip install os
import os
mydir = os.getcwd() # would be the same path as a.py
mydir
mydir_new = os.chdir(mydir+"\\Lets_learn_python")
mydir = os.getcwd() # would be the same path as a.py
mydir
%run BubbleSort.py
%run?
%env
%pwd

#python magic commands: https://ipython.readthedocs.io/en/stable/interactive/magics.html
# https://www.tutorialspoint.com/jupyter/ipython_magic_commands.htm
