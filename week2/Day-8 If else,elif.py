#if statement

'''Define the first condition if this is the true,do this
-Otherwise,do nothing '''


#stand alone if
score=50
if score>=90:
    print("A")



#else statement
'''Runs only if all previous conditions are false'''

"if nothing was true ,do this insted"


#two-way decision:else

score=95
if score>=90:
    print("A")
else:
    print("F")

#Multiple conditions
#if-elif-else

#elif statement

'''Asks a follow-up question only runs if previous conditions
were false'''


'''if the first wasn't true,try this one '''

'''if condtion1:
     do A
    elif conditon2:
        do c 
    else:
        do B'''

score=72
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")

#nested if

'''if statement inside another if'''

'''if the first is true
then check the second
'''

score=95
submitted_project=True

if score >=90:
    if submitted_project:
        print("A+")
    else:
        print("A")

elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")

