#Data Structures
'''Efficient way to store and organize data in a computer so that it can be used effectively.'''
#List
my_list=[454,"Pradeep Data Engineer",True,["SQL","Python","Pyspark","Databricks","Azure"]]

#Inedexing operations on top list 

print(my_list[0])
print(my_list[3])
print(my_list[3] [4]) #indexing with in list

#slicing
print(my_list[0:2])

#slicing with -ve index number
'''Length = total count of elements
Last index = length - 1 (because indexing starts at 0, not 1)'''

'''Value	10	20	30	40	50
Positive index	0	1	2	3	4
Negative index	-5	-4	-3	-2	-1'''

print(my_list[(len(my_list)-2):len(my_list)])

#step/stride slicing 
# the third value in [start:stop:step] controls how many elements to skip.
print(my_list[::2])

#lists are mutable, meaning you can change their content without changing their identity.
my_list.append("PradeepTop 1 % of Data Engineers")
print(my_list)

#list -we can insert number of elements at a specific index using insert() method
my_list.insert(1,1)
print(my_list)

#Drop last index element use pop function
##my_list.pop()
print(my_list)

#Reverse list of element 
'''Permanent .reverse()
 Temporary Method reversed method during runtime'''

#Permanent
my_list=[1,2,3,4,5]
my_list.reverse()
print(my_list)

#During run time reverse
for i in reversed(my_list):
    print(i)


my_list=[1,2,3,4,5]
new_list=[]

for i in my_list:
    new_list.append(i*i)

print(new_list)



#Dictionary
my_dictionary={"x":1,"y":2,"z":3}
print(my_dictionary)

#Dictionary also mutable
'''Key value can update'''
my_dictionary["x"]=10
print(my_dictionary)

#my_dictionary.pop("z")
print(my_dictionary)

#Print only Key
print(my_dictionary.keys())

#print only value
print(my_dictionary.values())


#See Both Keys and Value at once
print(my_dictionary.items())

my_dictionary={"x":1,"y":2,"z":3,"demo":{"x":1,"y":2,"z":3}}

print(my_dictionary)
print(my_dictionary['x'])
print(my_dictionary['demo']['z'])


#sets
a={1,2,3,4,5,6,6,7,8,9,10}
b={11,12,4,5,6,8}

#union
print(a.union(b))

#intersection
print(a.intersection(b))


#remove
a.remove(6)
print(a)

#add
a.add(20)
print(a)



#tuple
'''we can convert tuple to list and perform operations so we can't remember the tuple methods'''
my_tuple=(1,2,3,4,5,6,7,8,9,10)
print(my_tuple)

my_tuplist=list(my_tuple)
my_tuplist.append(11)
print(my_tuplist)

my_tup=tuple(my_tuplist)
print(my_tup)

