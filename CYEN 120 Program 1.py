################################################################################
# Name: Connor Heard
# Date: 9 / 28 / 2022
# Description: CYEN 130 Program 1
################################################################################


def average(a, b):
    return (a + b)/2

# a statement that prompts the user for his name


User_Name = input("Please enter your name: ")


# statement(s) that prompts the user for two test scores.


Score1 = int(input("Hi " + User_Name + ". What did you score on your first test? "))

Score2 = int(input("What did you score on your second test? "))


# display the final output

print("The average of " + str(Score1) + " and " + str(Score2) + " is " + str(average(Score1, Score2)) + ".")




