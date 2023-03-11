##############################################################################
# author: Connor Heard
# date: 11 / 1 / 2022  
# description: Program 06 - Listing All the Ages
#############################################################################

# A function that prompts the user for the number of people this program
# will be comparing.
def num_comparing():
    x = int(input("How many people are you comparing? "))
    if (x > 0):
        return x
    else:
        return num_comparing()

# A function that receives the size of a list, and repeatedly prompts the user
# for that number of names. It then returns the complete list of names.
def get_names(size):
    name_array = []
    count = 1
    while (count < size + 1):
        x = input("What is the name of person number {}: ".format(count))
        name_array.append(x)
        count += 1
    return name_array

# A function that receives the size of a list, and repeatedly prompts
# the user for that number of ages. It then returns the complete list of
# ages.
def get_ages(size):
    age_array = []
    count = 1
    while (count < size + 1):
        x = int(input("What is the age of person number {}: ".format(count)))
        age_array.append(x)
        count += 1
    return age_array

################################ MAIN ################################
# Ask for the number of people using one of the functions defined above.
number = num_comparing()
print("----------------------------------------")

# Ask for the names of the people using one of the functions defined
# above.
list_of_names = get_names(number)
print("----------------------------------------")

# Ask for the ages of the people using one of the functions defined
# above.
list_of_ages = get_ages(number)
print("----------------------------------------")

# Identify the names of the youngest and oldest people in the list.
i = list_of_ages.index(min(list_of_ages))
j = list_of_ages.index(max(list_of_ages))
youngest = min(list_of_ages)
oldest = max(list_of_ages)
youngest_person = list_of_names[i]
oldest_person = list_of_names[j]

# Display information about the lists.
print("{} is the youngest at {} years old".format(youngest_person, youngest))
print("{} is the oldest at {} years old".format(oldest_person, oldest))
print("The average age is {}".format(sum(list_of_ages) / len(list_of_ages)))
