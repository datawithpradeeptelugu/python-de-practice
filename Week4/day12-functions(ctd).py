'''When to use *args and **kwargs in Python functions'''
#*args 
'''when you pass simmilar values 
    Ex: (1,2,3,,4,5)
        (Alex,Kumar,Nora,Omar,Leo)    
'''
#**kwargs
'''When you pass different types of values 
(Alex,25,alex@gmail.com,10.11.2024)
'''


#Create the User Profile
def create_user (**kwargs):
    print(type(kwargs))
    print(kwargs)
    

create_user(first_name="Mo",
            last_name="Salah",
            age="33",
            country="Egypt")

#Now We can pass differnet augment to that user define fucntion
create_user(name="Ronaldo",country="Portugal")

'''Note: Only Work with Keyword Aurgments
Ex: create_user("Ronoldo","Portugal") ##TypeError: create_user() takes 0 positional arguments but 2 were given
'''

#Return Function
def clean_name(name):
    cleaned = name.strip().lower()
   
    return cleaned

#Assigne return value
'''Assign the fucntion call to a variable to store the result'''
cln_name=clean_name(" Maria ")
print(cln_name)

'''Note:
If a function has no return statment ,python retuns none'''


'''A function can have multiple return statements '''
#if the value is empty ,covert it to none .Otherwise ,clean it
def clean_name(name):
    if not name:
        return None
    else:
        cleaned=name.strip().lower()
        return cleaned
cln_name=clean_name(" Maria ")
print(cln_name)

'''Note:
You can return multiple values seperated by commas'''
def clean_name(name):
    lo_cleaned=name.strip().lower()
    up_cleaned=name.strip().upper()
    return lo_cleaned,up_cleaned

lo_name,up_name=clean_name(" maria ")
print(lo_name)
print(up_name)