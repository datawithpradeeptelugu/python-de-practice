#While Loop
'''Repeats a block of code over and over  as long as a condition is True'''

i=1  #Step1:intilization

while i <4: #Step 2: define condition
    print(i)
    i+=1 #step 3:update the loop variable


#Task
'''Build a Counter from 1 to 5'''
i=1  #initilzation
while i<=5: #condition
    print(i)
    i+=1 #update



#While True

# while True:
#     print("i'm unstoppable!")

# answer=""
# while answer !="yes":
#     answer =input("Do you agree? (yes/no):")
# print("Thank you")


while True:
    answer =input ("Do you agree ? (yes/no)")
    if answer == "yes":
         break
print("Thank you")