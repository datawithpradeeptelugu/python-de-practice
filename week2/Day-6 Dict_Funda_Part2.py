user ={"id":1,"age":25,"city":"berlin"}

#Add,Remove & Update

'''Assign Key: 
Updates the value if the key exists, or inserts a new key value pair if doesn't'''


#Add -Insert new key value pair
user["name"]="john"
print(user) #{'id': 1, 'age': 25, 'city': 'berlin', 'name': 'john'}

#Update the value of key
user["age"]=35
print(user)  #{'id': 1, 'age': 35, 'city': 'berlin', 'name': 'john'}

'''if we to Update lot of values in the dictionary ,use update()'''

user.update({"age":40,"city":"paris"})
print(user) #{'id': 1, 'age': 40, 'city': 'paris', 'name': 'john'}


 #remove

'''To remove the key from the dictionary use pop() mehtod
pop()=>removes a key from the dictionary and returns its value

'''

user= {'id': 1, 'age': 40, 'city': 'paris', 'name': 'john'}
user.pop("age")
print(user) #{'id': 1, 'city': 'paris', 'name': 'john'}

'''Key error:if the key is not found,python throws a key error'''
# user={'id': 1, 'city': 'paris', 'name': 'john'}
# user.pop("salary")
# print(user) # KeyError: 'salary'

'''To fix this KeyError'''
user={'id': 1, 'city': 'paris', 'name': 'john'}


age=user.pop("salary","Not Found")

print(user) #{'id': 1, 'city': 'paris', 'name': 'john'}

print("Removed Item:",age) #removed item: Not Found

'''Returns and deletes the most recent keys value pair from the dictionary'''
user={'id': 1, 'city': 'paris', 'name': 'john'}
#user.popitem()
print(user) #{'id': 1, 'city': 'paris'}


# Creation
user={'id': None, 
      'city': None, 
      'name': None
      }
'''Defining Dictionary doesn't value so if you want keep repeating same value 
use fromkeys() method

fromkeys()=>builds new dictionary where all keys get the same default value
'''
user=dict.fromkeys(["id","name","age","city"],0)
print(user)


#Challenge:Keep Only String Values & Convert Them to UPPERCASE
user={'id': 1,'name': 'john',"age":30, 'city': 'berlin' }

'''For this case we are using 
Dict comprehensions =>3 Components
1)Key Value Expression
2)a Loop
3)Optional Condition
'''

user_str={
    k:v.upper() #Expression
    for k, v in user.items() #Loop
    if isinstance (v,str) #Filter
}

print(user_str)  #{'name': 'JOHN', 'city': 'BERLIN'}
















