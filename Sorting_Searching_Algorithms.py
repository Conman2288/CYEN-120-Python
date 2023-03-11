#Creating and Populating a List

SIZE = 20

from random import randint

#Create a list of random integers
def generate_nums_list():
    numbers = []
    while (len(numbers) < SIZE):
        # add a random number to the list
        numbers.append(randint(1,99))
    return numbers

#Sequential Search for largest value
def seq_search_largest(numbers):
    largest = numbers[0]
    for index in range(1, len(numbers)):
        if (numbers[index] > largest):
            largest = numbers[index]
    return largest

#Selection Sort
def sel_sort(numbers):
    n = len(numbers)
    for i in range (0, n - 1):
        minPosition = i
        for j in range(i + 1, n):
            if (numbers[j] < numbers[minPosition]):
                minPosition = j
        #Swapping Algorithm
        temp = numbers[i]
        numbers[i] = numbers[minPosition]
        numbers[minPosition] = temp

#Binary Search
def bin_search(num, numbers):
    found = False
    first = 0
    last = len(numbers) - 1
    index = -1

    while (first <= last and found != True):
        mid = (first + last) // 2
        if (num == numbers[mid]):
            found = True
            index = mid
        elif (num > numbers[mid]):
            first = mid + 1
        else:
            last = mid - 1
    return index
#########Main###########
numbers = generate_nums_list()
print("The list: " + str(numbers))
num = int(input("What integer would you like to search for? "))
sel_sort(numbers)
print("The number {} is in the list: {}".format(num, bin_search(num,numbers)))

