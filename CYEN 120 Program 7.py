####################################################################
# author: Connor Heard
# date: 11 / 4 / 2022
# desc: Program 07 - Random Grade Assignments
###################################################################

from random import randint

# constants defined to limit the scope of the randomly generated grades.
LOWEST_GRADE = 65
HIGHEST_GRADE = 100


# A function that prompts the user for the number of students in the
# class and returns that value to the calling statement.
def get_num_students():
    x = int(input("How many students are in this imaginary class? "))
    return x

# A function that receives the number of students as an argument, and
# creates a list of random integers of that size. The complete list is
# returned to the calling statement.
def get_list_grades(num_of_students):
    num_grades = []
    i = 0
    while (i < num_of_students):
        num_grades.append(randint(LOWEST_GRADE, HIGHEST_GRADE))
        i += 1
    return num_grades

# A function that receives a single grade as its argument, and returns a
# letter corresponding to the correct letter grade.
def get_letter_grade(list_of_nums):
    list_of_letters = []
    for num_grade in list_of_nums:        
        if (num_grade >= 90):
            list_of_letters.append("A")
        elif (90 > num_grade >= 80):
            list_of_letters.append("B")
        elif (80 > num_grade >= 70):
            list_of_letters.append("C")
        else:
            list_of_letters.append("D")
    return list_of_letters
        
# A function that receives a list of values, and prints them in order
# separated by a tab space.
def print_list(arr):
    string = ""
    for i in arr:        
        string += str(i) + "\t"
    print(string)    


# A function that recieves a list of numerical values, and returns the
# mean/average of that list.
def get_average(num_list):
    return (sum(num_list) / len(num_list))

############################# main ############################

# using functions defined above, get the class size, numerical grade
# list, and letter grade list.
x = get_num_students()
nums = get_list_grades(x)
letters = get_letter_grade(nums)
  
# Print out both numerical and letter grades as well as the average.
print("Numerical Grades:")
print_list(nums)
print("Letter Grades:")
print_list(letters)
print("The average grade for the class is {}".format(get_average(nums)))
