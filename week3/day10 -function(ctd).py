#Golden Rule
'''Before writng new code 
always check if it is already exists

Just don't reinvent the wheel

#1.Check the Built-in Function

#2.Check the libraries

If you don't find the solution in the library then you must be written from scratch

But even before you start writing from scratch and go and ask your team.So check your project 

Ask your colleague this is the nature of the project



#3.Check with your Team->User Defined Function

#4.Write your User-Defined Functions f(x)
'''


'''Python only defining function doesn't execute it,We have to call it'''

def daily_ritual ():
   
    print("Make My Bed")
    print("Do Brush")
    print("Drink Hot Water")
    print("Natural Call")
    print("Do Stregth/Cardio+Meditation")
    print("Listen Stragest Secrect of the World")
    print("Read Goal Card with Emotion")
    print("Write top 20 Goals on Each 2 Pages")
    print("Listern Affrmations with Feel")

print("wake up")
daily_ritual()
print("start your day with ")
daily_ritual()


'''Note:
Functions Organize & Structure our code and make our life easier'''


#1.built-in function
print(len("Python"))


#Function from libraries (import then call)
import math
number =4.2
print(math.ceil(number))

#User defined function (Define then call)
def greet():
    print("Hello")
greet()



'''How data flow through the Functions'''
#Parameters & Arguements

'''Function Shapes

Noinput/Output

Only Input

Input&Output
Arguement
Parameter
Return

Multi-Input/Output

'''

#Parameter

'''Names used in function defintion that describe what data the function expects '''

#Arguments
'''Actual Values passed in a function call that are assigned to parameters'''


def clean_name():
    name =" Pradeep "  #Hardcoded value issue
    print(name.strip().lower())

clean_name()
clean_name()
clean_name()

'''Hard coded value issue,It is not resuable because it is always clean the same value.

#Pass Data in
Pass the value as a parameter  to handle any input
'''

def clean_name(name):
    print(name.strip().lower())

clean_name(" Brain in the Fridge/Freezer, Action ")
clean_name("Every Day Take Action then What next Without thinking about Perfection")

'''Works With any Value
Values change,But logic stays the same
'''

#3 Kind of Variable in Python

'''
1.Parameters
2.Local Variables
3.Global Variables 


It asks 
How long Does it Live?

Where is it Accessable?

For ex:
'''

def multiple_two(x): #x=>Parameter ,Function Defintion
    print(x*2)

multiple_two(3) # Function Call




#Ex:2 Gloabl Variable

'''Gloable Variable Created outside the function can be accessed Anywhere'''

f=2 # f=> Gloable Variable

def multiple_factor(x): #x=>Parameter ,Function Defintion
    print(x*f)

multiple_factor(3) # Function Call

#Ex:3 Local Variable

f=2 # f=> Gloable Variable

def multiple_factor(x): #x=>Parameter ,Function Defintion
    y=x*f 
    print(y)

multiple_factor(3) # Function Call





