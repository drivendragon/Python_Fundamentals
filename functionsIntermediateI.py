#Objectives:
#Practice using default parameter values
#Practice passing in named arguments
#Become familiar with Python's random module

#If no arguments are provided, the function should return a random integer between 0 and 100.
#If only a max number is provided, the function should return a random integer between 0 and the max number.
#If only a min number is provided, the function should return a random integer between the min number and 100
#If both a min and max number are provided, the function should return a random integer between those 2 values.


#random.random() returns a random floating number between 0.000 and 1.000
#random.random() * 50 returns a random floating number between 0.000 and 50.000
#random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
#round(num) returns the rounded integer value of num


import random
def randInt(min=1   ,max=999   ):
    num = random.random()
    #return num
    print(num)

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500