#Building Full Clean Name

def clean_name(First_Name,Last_Name,country):
    First= First_Name.strip().lower()
    Last= Last_Name.strip().lower()
    Full_Name=First + " " +Last
    print(Full_Name,"From",country)

clean_name(" Pradeep" ,"Kasipuri","India")


'''Note:
No of Aurgments must match the No.of Parameters
'''

#Positinal Aurguments Vs Keyword Aurgments
clean_name("Pradeep","Kasipuri","India")

#Keyword Aurgments
clean_name(country="India",First_Name="Pradeep",Last_Name="Kumar")

#