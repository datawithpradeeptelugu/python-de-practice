'''
Loop=>
Control the flow of code
Repeat a block of code over and over
Until a condition met
'''

'''
For Loops 
Basics
'''

'''
Go through a Group of Items
one by one 
to do something for each item
'''

print("Round :1 ")
print("Round :2 ")
print("Round :3 ")
print("Round :4 ")
print("Round :5 ")
print("Round :6 ")

for i in [1,2,3,4,5]:
    print("Round :",i)


'''
Naming Conventions for Readablity 
loop variable and sequence


Use the same word:
Variable->Singular
Sequence->Plural
'''

#Ex for Naming Convention
items=[1,2,3,4,5]
for item in items:
    print("Round:",item)

'''The Sequence can be 

# Tuple=>user = ("Alice", 30, "Engineer")

#List=>mylist = ["apple", "banana", "cherry"]

#String =>"Python"

#range()=range([start],stop,[step])

#dictionary=> 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#files
'''

items="Python"
for item in items:
    print(item) 
#P
# y
# t
# h
# o
# n

#Range
items=range(1,6)
for item in items:
    print(item)

# 1
# 2
# 3
# 4
# 5


#Python Challenge

#Print 7 Table 
items=range(1,11)
for item in items:
    print(f" 7*{item}={7*item}")

'''

print(f"7 * {item} = {7 * item}")
7 *= Plain Text
{item} gets replaced with current number
= plain text
{7* item}= get replaced with the multiplication result

'''

#Challenge 2:
'''Print Left algined pyramid of stars with 6 rows using a for loop'''
items=range(1,7)
for item in items:
    print("*" * item)

    