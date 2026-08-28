'''String Formating
String act as Array
Performnig indexing on top of String
'''
x ="Pradeep Kasipuri"
print(x[8])

#Indexing
'''Indexing is a way to access individual characters in a string. In Python, strings are indexed starting from 0. 
This means that the first character of the string has an index of 0, the second character has an index of 1, and so on. 
You can use square brackets [] to access a specific character in the string by its index.'''

#n-1 logic

x= "Data Engineer"
print(x[5:13]) #Slicing


#x[:]->x[0:len(x)]
x="Pradeep Data Engineer"
print(x[:])

#string functions

#uppercase
print(x.upper()) 

#lowercase
print(x.lower()) 

x="pradeep Top 1 Percent any of the field"
print(x.capitalize()) #capitalizes the first character of the string and converts the rest of the characters to lowercase.


#replace
txt="Systems are more powerful than people"
print(txt.replace("people","humans becasue humans have monkey minds"))

#Split all the things within the delimiter
txt="pradeep kasipuri is top 1% data engineer"
print(txt.split(" "))


#endswith
file="raw_data.csv"

if file.endswith("csv"):
    print("CSC File")
#startswith

if file.startswith("raw"):
    print("raw data")

#count
txt="Pradeep Data Enginneer .Pradeep is Top 1% of Data Engineers.Pradeep belives in sytems than willpower & motivation"
print(txt.count("Pradeep"))

#is functions
txt="Pradee Data Engineer"
num="111111"
alnum="Pradeep1"
print(txt.isnumeric())
print(num.isnumeric())
print(alnum.isalnum())

#if conditon
x=10
if (x==10):
    print("x is:",x)

#else
x=120
if (x==10):
    print("x is:",x)

else:
    print("x is not 10")


#elif
x=120
if (x==10):
    print("x is:",x)
elif(x>100):
    print("x is too Big")
else:
    print("x is not 10")

#nested if else
x=201
if (x==10):
    print("x is:",x)
elif(x>100):
     if (x>100 and x<200):
         print("x is in between 100 and 200")
     else:
         print("x is greater than 200")
    
else:
    print("x is not 10")