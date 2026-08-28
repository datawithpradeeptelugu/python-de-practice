#Loops in Python
''''''
#Staic way to print below
print("order")
print("products")
print("customers")

#Another Way-Loop
#For loop
my_list=["orders","products","customers"]
for  item in my_list:
    print(item)

#range function
for item in range(1,101):
    print(item)

tbl_list=["Orders","products","customers"]
for item in tbl_list:
    if (item.lower()=="orders"):
        print("Table Order")
    else:
        print("No Table Order")
        

