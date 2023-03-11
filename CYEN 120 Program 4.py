#########################################################################
# name: Connor Heard
# date: 10 / 14 / 2022
# description: Program 04 - Blocks in a Pyramid
#########################################################################

# A function to prompt the user for the number of levels that their
# pyramid will have and return it to the calling statement.
def get_number_levels():
    levels = int(input("How many levels will your pyramid have? "))
    return levels


# A function that receives the number of pyramid levels and the number
# of blocks as arguments, and prints the appropriate results to the
# screen.
def final_output(num_level, num_block):
    return print("For " + str(num_level) + " levels, you will need " + str(num_block) + " blocks")

# A recursive function that receives the number of the level, calculates
# the number of blocks required, and returns the result to the calling
# statement.
block = 0
def calc_block(levels):
    global block
    block += levels**2
    if (levels > 0):
        calc_block(levels - 1)
    return block
    
    
    
        
################################ MAIN ################################
# using the function(s) defined above, ask the user for the number of
# pyramid levels
x = get_number_levels()

# using the function(s) defined above, calculate and display the final results
y = calc_block(x)
final_output(x,y)
