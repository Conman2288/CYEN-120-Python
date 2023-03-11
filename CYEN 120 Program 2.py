################################################################################
# Name: Connor Heard   
# Date: 10 / 3 / 2022
# Description: This program asks the user for two test scores and prints out the average.
################################################################################

# A function that prompts the user for a name and returns it to the
# calling statement.
def give_name():
    name = input("Please enter your name: ")
    return name

# A function that prompts the user for a score and returns it to the
# calling statement.
def get_score():
    score = int(input("Enter your score: "))
    return score

# A function that receives two numbers and returns the average of those
# two values to the calling statement.
def average(a, b):
    return (a + b) / 2

# A function that receives a string and a number (the name and the
# average score) and prints it out on the screen in the appropriate format.
def output(a, b):
    return print("Hi, " + a + ". Your average score is " + str(b) + ".")

#############################################################################
#       MAIN PART OF PROGRAM
# Functions that were defined above should be executed below in an order
# that satisfies the problem statement. Additional statements can be
# included below as well if needed.
#############################################################################

# prompt for name
name = give_name()

# prompt for two scores
score1 = get_score()
score2 = get_score()

# calculate the average
avg = average(score1, score2)

# display the final output
output(name, avg)

