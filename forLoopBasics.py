#Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1005,5):
    print(i)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for num in range(100):
    if num % 5 == 0:
        print("Coding")
    elif num % 10 == 0:
        print("Coding Dojo")
    else:
        print(num)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
total = 0
for num in range (0, 500000, 1):
    if num % 2 != 0:
        total += num
        print(total)


#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num in range(2018, 0, -4):
    print(num)


# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines):
lowNum=2
highNum=9
mult=3
 
num = 0 
for num in range(lowNum, highNum, mult):
    if num % 2 == 0:
        print(num)