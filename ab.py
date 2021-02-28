#Count Positives - Given a list of numbers, create a function to replace 
# the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# list of numbers 




def countPositives(myList):
    pos_count = 0
    for num in range(len(myList)):
        if num >= 0: 
            pos_count += 1
            newList = myList.append(pos_count)
    return newList
   
 
print(countPositives([-1,1,1,1]))  
   

#list1 = [10, -21, 4, -45, 66, -93, 1] 
#pos_count = 0
#for num in list1:
#    if num >= 0: 
#        pos_count += 1
#newList = list1.append(pos_count)
#print(newList)
























