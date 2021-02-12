for x in range(0, 10, 1):  

#Notice that range takes 3 arguments. The first value is where the loop should begin, the second value is where the loop should end (exclusive), and the third value is how to increment the iterator

# The range function actually comes with a few shortcuts. If we know the increment is going to be plus one, we can actually just ignore the third argument. Furthermore, if we know the increment is going to be positive one and the loop starts at 0, we can also leave off the first argument. In other words, each of the following will result in exactly the same loop:
for x in range(0, 10, 1):
for x in range(0, 10):	# increment of +1 is implied
for x in range(10):	# increment of +1 and start at 0 is implied

# Note that if you need to specify an increment other than +1, all three arguments are required.
for x in range(0, 10, 2):
print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# For Loops through Lists
#If we want to iterate through a list, we could use the range function and send in the length of the list as the stopping value, but if we are not interested in the index values and want to just see the values of each item in the list in order, we can actually loop to get the values of the list directly!
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

#For Loops through Dictionaries
#Dictionaries are also iterable. When we iterate through a dictionary, the iterator is each of the keys of the dictionary.
for k in my_dict:
    print(k)
# output: name, language

#That means if we want the values of our dictionary, we might do something like this:
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

#Dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. Test these out to get a better understanding:
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)

#While Loops
#While loops are another way of looping while a certain condition is true.
#Remember this for loop?
for count in range(0,5):
    print("looping - ", count)

#We can rewrite it as a while loop:
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

#The basic syntax for a while loop looks like this:
while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

#Else
#There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something if that happens? We can then use an else statement with our while loop. Yes, that is right, else in a loop.
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

#Loop Control
#We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well. Control flow is the cornerstone of most programming languages.

#When you want finer control over your loops, use the following statements to do so.

#Break
#The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.

#The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop.

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

#Notice that when the loop got to the letter "i", we stopped looping.


#Continue
#The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.

#The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.#

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1