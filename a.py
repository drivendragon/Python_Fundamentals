#3Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for dic in students:
    for val in dic.values():
        print(val)
#Michael
##John
#Mark
#KB
#And iterateDictionary2('last_name', students) should output:

#Jordan
#Rosales
#Guillen
#Tonel
