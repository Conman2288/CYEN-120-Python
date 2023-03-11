#################################################################################
# name: Connor Heard
# date: 10 / 10 / 2022
# description: Program 3 - Number Properties
#################################################################################

# A function that prompts the user for a number and returns it.
def get_num():
    return int(input("Enter a number:\t    "))


# A function that receives three numbers as arguments, and returns the
# largest of the three numbers.
def get_largest(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c

# A function that receives three numbers as arguments, and returns the
# product of the two largest arguments.
def get_product(x, y, z):
    if (x > y and y > z):
        return x*y
    elif(y > x and x > z):
        return x*y
    elif(x > y and z > y):
        return x*z
    elif(z > x and x > y):
        return x*z
    elif(y > x and z > x):
        return y*z
    else:
        return y*z


# A function that receives an argument and returns a string representing
# whether that argument is even or odd.
def even_odd(x):
    if (x % 2 == 0):
        return "even"
    else:
        return "odd"

# A function that receives an argument and determines whether that
# argument is a prime number.
def is_prime(x):
    i = 2
    while (i < x):
        if (x % i == 0):
            return "False"
        i += 1
    return "True"
    
##################################### MAIN PROGRAM #######################
# Functions that were defined above should be executed below in an order
# that satisfies the original problem statement. Additional statements
# can be included if needed.
##########################################################################

# Prompt for three different numbers and store them appropriately.
num1 = get_num()
num2 = get_num()
num3 = get_num()


# Print out the table header information.
print("--------------------")
print("Num\tEven\tPrime")
print("--------------------")

# Print out the table contents for each of the three numbers.
print(str(num1) + "\t" + even_odd(num1) + "\t" + is_prime(num1))
print(str(num2) + "\t" + even_odd(num2) + "\t" + is_prime(num2))
print(str(num3) + "\t" + even_odd(num3) + "\t" + is_prime(num3))
print("--------------------")

# Print out the identity of the largest number and the largest product
# from the given numbers.
print("The largest number is {}".format(get_largest(num1, num2, num3)))
print("The largest possible product is {}".format(get_product(num1, num2, num3)))
