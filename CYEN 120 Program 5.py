########################################################################
# author: Connor Heard   
# date: 10 / 26 / 2022
# description: Program 05 - Logbook
########################################################################

import math

# A function that prompts the user for the minimum value and returns it
# to the calling statement. Function to also deal with range checking to
# make sure that minimum value provided is greater than 0

def get_min():
    minimum = float(input("What is the minimum value? "))
    if (minimum > 0):
        return minimum
    else:
        print("ERROR: Minimum should be greater than 0")
        return get_min()      

# A function that prompts the user for the maximum value and returns it
# to the calling statement. Function receives argument that is used in
# range checking to make sure maximum value provided by user is greater
# than minimum value (provided in function argument)

def get_max(minimum):
    max_ = float(input("What is the maximum value? "))
    if (max_ > minimum):
        return max_
    else:
        print("ERROR: Maximum should be greater than " + str(minimum))
        return get_max(minimum)

# A function that prompts the user for the step size and returns it to
# the calling statement. Function also deals with range checking to make
# sure that step size provided is greater than 0.

def get_step():
    step_size = float(input("What is the step size? "))
    if (step_size > 0):
        return step_size
    else:
        print("ERROR: Step size should be greater than 0")
        return get_step()
        
# A function that receives a number as an argument and returns the log
# of that number rounded to 4 decimal places.

def calc_log(x):
     x = round(math.log10(x), 4)
     return x
    
# A function that receives the value at the left size of the log table
# (i.e. the value whose logarithms should be calculated). The function
# then creates a row of logarithmic values for that argument counting
# upwards in steps of 1 significant figure more than the argument. i.e.
# if the argument is 1.3, then the row gives values of the logs for
# 1.30, 1.31, 1.32, 1.33, ..., 1.39. If the argument is 2.456, then it
# gives logs for 2.4560, 2.4561, 2.4562, 2.4563, ..., 2.4569

def row_maker(z):
    z = round(z,5)
    strr = "{:0.4f}\t".format(float(z))
    print(strr , end = " ")
    i = 0
    s = ""
    while (i < 10):
        x = str(round(calc_log((float(str(z) + str(i)))),4))
        s += "{:0.4f} ".format(float(x))
        i += 1
    print(s)
    
# A function that receives the minimum, maximum and step size as
# arguments, and prints the table (making use of the function that
# creates a single row defined earlier)

def make_table(min_, max_, step):
    print("         0      1      2      3      4      5      6      7      8      9")
    print("------------------------------------------------------------------------------")
    while (min_ < max_):
        row_maker(min_)
        min_ += step
        
####################### MAIN #########################################
# Get the minimum, maximum and step size from the user using functions
# defined earlier.
min_ = get_min()
max_ = get_max(min_)
step_size = get_step()
# create the table using the function defined eariler.
make_table(min_, max_, step_size)
