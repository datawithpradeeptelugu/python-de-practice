                            #1.Action Functions


'''Design to perform an operation in the system instead of returning a value'''

#Task:Stores application log messages in a file whenever an event occurs 
def write_log(message):
    with open(r"C:\Users\kasi3695\OneDrive - Rackspace Inc\Microsoft Teams Chat Files\Desktop\app.logr","a") as file:   #with open function:open the file safely and closes it automatically when done
        file.write(message + "\n")

# write_log("App Started")
# write_log("user logged in ")
write_log("App Stopped")




                                #2.Trasformation Functions
'''Raw data goes in gets trasformed and returns processed data'''
#Task :Cleans Email Address and splits them into structured data (User Name and Domain)
def clean_and_split_email(email):
    cl_email = email.strip().lower()
    #sara@gmail.com
    username,domain=cl_email.split("@")
    return {"username":username,
            "domain":domain}

print(clean_and_split_email("sara@gmail.com"))

                        #3.Validation Functions
'''Validates a Condition and returns a boolean value'''
#Task:Checks whether the password meets the minimum requirement of 8 characters

def is_valid_password(password):
    return len(password) >= 8
print(is_valid_password("123456"))
print(is_valid_password("123456789"))

#Task:Checks Wheter an email has basic valid formats
def is_valid_email(email):
    return "@" in email and "." in email
print(is_valid_email("sara.com"))
print(is_valid_email("sara@gmail.com"))

                    #4.Orchestrator Function
'''Controls program flow by calling other functions in the correct order'''

 
