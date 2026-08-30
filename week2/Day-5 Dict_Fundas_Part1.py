#dictionaries
my_dict={'a':1,
         'b':2,
         'c':3}
print(my_dict) #ordered
#o/p:{'a': 1, 'b': 2, 'c': 3}


my_dict={'a':1,
         'b':2,
         'c':3,
         'a':4}
print(my_dict) #keys must be unique
#o/p:{'a': 4, 'b': 2, 'c': 3}


my_dict={'a':1,
         'b':3,
         'c':3,
         'a':4}
print(my_dict) #values allowed duplicates
#o/p:{'a': 4, 'b': 3, 'c': 3}

#Not indexed(keyed)
##print(my_dict[1])
'''Access values by using their keys,not Index'''
print(my_dict['b'])

#O/p:3

#Dictioanries  are mutable
my_dict={'a':1,
         'b':3,
         'c':3}
my_dict['c']=5
print(my_dict)
#o/p: {'a': 1, 'b': 3, 'c': 5}

###Access###

#Access key but it is not part of dictionary

user={"name":"John","age":30,"city":"New York"}
print(user["city"])

'''If the key is not found ,Python throws a key error
get() Missing key returns None or your default value
'''

#print(user["country"]) #KeyError: 'country'
print(user.get("Country"))  #None
print(user.get("Country","Not Found")) #Not Found



###Checks in Dictionary###
'''Ex:test if the key is exist in the dictionary'''
user={"name":"John","age":30,"city":"New York"}
print("age" in user) #True
print("Country" not in user)  #True


#View objects
'''Give you live view of the dictionaries keys,values, or Key value pairs'''

##Print All the keys of Dictionaries

#keys()=> Returns all the KEYS in the dictionary

user={"name":"John","age":30,"city":"New York"}

print(user.keys())  #dict_keys(['name', 'age', 'city'])

#values()=>Returns all the VALUES in the Dictionary

print(user.values()) #dict_values(['John', 30, 'New York'])

#items() =>Returns all (key,value) paris in the dictionary

print(user.items()) #dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

#differece between items() vs print dictionary

print(user) #{'name': 'John', 'age': 30, 'city': 'New York'}

print(user.items()) #dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

'''items()==> Perfect when you need key and value together for looping,tranforming data ,
building new dictionary comparing and more'''

#Looping

#Print Only Keys
for u in user:
    print(u) 
    # name
    # age
    # city


#Print both key and Pair

    #Method1:
    for u in user:
        print(u,user[u])

    # name John
    # age 30
    # city New York

    #Method2
    for key,value in user.items():
        print(key,value)

    # name John
    # age 30
    # city New York

'''Note: Mehtod 2 is more efficient than Method1 because it doesn't have to look up the value for each key'''












