#Numbers>int,Float,Decimal
#Alphabet>String,Char,varchar
#Seq Data type >List,Tuple,Range
#Boolean>True,False

var1 =1
var2 =1.0
var3= True
var4="Anjali"
var5="True"
l=[2023,"Python","Easy","Language"] #List
s=(2023,"Python","Easy","Language") #set
d={"Key1":"Value","Key2":"Value","Key3":"Value"}

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(l))
print(type(s))
print(type(d))

#type casting
var1=10
var2=str(10) #explicit casting
print(type(var1))
print(type(var2))

var3=20.5
result=var1+var3
print(result)  #implicit type casting


#Operators
#Arithmetic ->+,-,*,?,%
#Comparision-> =,<=,>=,!=
#Assignment -> =,+=,-+,,*=
#Logical ->AND,OR,NOT
#Memebership ->In,Not In

a=21
b=10
c=0
c=a+b
# c=a-b
# c=a-b
# c=a*b
# c=a/b


#mebership -in,not in
a=10
b=20
list =[1,2,3,4,5,6,7,8,9]
if(a in list):
    print("a is present in the list")
else:
    print("a is not present in the list")


if(b not in list):
    print("b is not preset in the list")
else:
    print("b is  present in the list")

#identity operator
a=[1,2,3] #memory location 1
b=[1,2,3]
c=a
print(a)
print(a is c)
print(a is b)


#BODMAS - Brackets,Order,Division,Multiplication,Addition,Subtraction
#Arithmetic operators
#ompariosn operators
#Assignment operators
#Identity
#Membership
#Logical


#if else
#input from user
a=int(input("Enter a number:"))
