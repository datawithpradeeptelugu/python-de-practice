my_var="Pradeep" #my name -Single Line Comment
last_name="Kumar"

x=10
y=5

'''This is a multi-line comment
This is the second line of the comment'''


#Multi Line Code


print(x+y)
print(my_var+last_name)
#print(x+my_var)

#Mutliple assignments
x,y,z=10,20,30
print(z)

x=y=z=100
print(z)

#Multi Line Code-Black slash(\) is used to break the line of code into multiple lines
total=10+20+30 \
      +40+50+60+70+80+90+100
print(total)


'''-Indentation
Indentation refers to the spaces at the beginning of a code line.
Python uses indentation to indicate a block of code.'''

x=1
if x==1:
    print("x is 1")
print(x)


'''Type Casting
-Implict type casting
-Explicit type casting'''

#implicit type casting
a=10
b=20.5
print(type(a+b ))


#explicit type casting
x=454
y="pradeep"
x_new=str(x)
print(type(x_new))
print(y+x_new)