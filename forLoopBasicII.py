#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
array = [-1,3,5,-5]
def biggieSize(array):
    for i in range(len(array)):
        if array[i]>0:
            array[i]='big'
        return array
        print array
print(biggieSize(array))


#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# list of numbers 
list1 = [10, -21, 4, -45, 66, -93, 1] 
pos_count = 0
for num in list1:
    if num >= 0: 
        pos_count += 1
newList = list1.append(pos_count)
print(newList)
          
#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
myList = [1,2,3,4]
for i in myList:
    countingTotal = i + i
    print countingTotal

#Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
def Average(lst): 
    return sum(lst) / len(lst) 
lst = [15, 9, 55, 41, 35, 20, 62, 49] 
average = Average(lst) 
print("Average of the list =", round(average, 2)) 

#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
len_list = [1, 5, 9, 'x','y','z', 20, 25]
print ("Number of items in the list = ", len(len_list))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
# list of numbers
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest element is:", *list1[:1])

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
def largest(arr, n): 
    return max(arr)  
arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
print(largest(arr, n)) 

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
my_dict = {'x':500, 'y':5874, 'z': 560}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def Reverse(lst): 
    lst.reverse() 
    return lst 
lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst)) 
