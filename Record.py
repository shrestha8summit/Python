#forming an empty ist for input
name=[] 
roll=[] 
age=[] 
address=[]
phone=[] 
gpa=[] 


#forming empty list for storing removed items 
r_name=[]
r_roll=[]
r_age=[]
r_address=[]
r_phone=[]
r_gpa=[]

#taking input from user 
print("\t\t Entery for new records of latest academic year")
n = 1 

while n ==1:
    namee=input("Enter your name:\t")
    rolll=int(input("Enter your roll number:\t"))
    agee = int(input("Enter your age :\t"))
    addresss=input("Enter yur home address:\t")
    
    while True:                                          #updated from Ma'am's idea
        phonee=int(input("Enter your phone number:\t"))
        pho=str(phonee)
        if(len(pho)!=10):
            print("Please enter the correct number ")
        else:
            break
    
    m1    = float(input("Enter the marks obtained in physics\t"))
    m2    = float(input("Enter the marks obtained in maths\t")) 
    m3    = float(input("Enter the marks obtained in N.C\t\t"))
    m4    = float(input("Enter the marks obtained in PTTL\t") )
    m5    = float(input("Enter the marks obtained in c prog.\t"))
    per   = (m1+m2+m3+m4+m5)/500
    perc  = per*100
    gpaa  = perc /9.5
    name.append(namee) 
    roll.append(rolll) 
    age.append(agee)
    address.append(addresss)
    phone.append(phonee) 
    gpa.append(gpaa)
    n = int(input("\n Is there any data remaining for entry 1 or 0: \t "))
    print("\n")
    
#making list from  past year academic record
o_name=["Rajan","Sujal","Abin","Ayush","Sagar"]
o_roll=[1,2,3,4,5]
o_age=[18,19,19,17,20]
o_address=["Kathmandu","Lalitpur","Kirtipur","Kalikot","Nepalgunj"]
o_phone=[9847362467,9847362468,9847362469,9846354983,9856084329]
o_gpa=[8.9,9,8.7,5,7.5]

#list operations
o_name.extend(name)
o_roll.extend(roll)
o_age.extend(age)
o_address.extend(address)
o_phone.extend(phone) 
o_gpa.extend(gpa)


print("The number of records are ",len(o_name))
print("---------------------------------------------------------------------------------")
print("S.N\t NAME\t ROLL\t AGE \t ADDRESS\t PHONE\t\tGPA")
for i in range(len(o_name)):
    print("---------------------------------------------------------------------------------")
    print(i+1,"\t",o_name[i],"\t",o_roll[i],"\t",o_age[i],"\t",o_address[i],"\t",o_phone[i],"\t",o_gpa[i])
print("---------------------------------------------------------------------------------")


drop = int(input("\n\nDid any of the past year student left our college 1 or 0 :\t"))
if drop == 1:
    while drop == 1:
        for i in range(0,len(o_name)):
            which=int(input("Enter the S.N from the last list who have left college:\t"))-1
            re_name=o_name.pop(which)
            re_roll=o_roll.pop(which)
            re_age = o_age.pop(which)
            re_address=o_address.pop(which)
            re_phone=o_phone.pop(which)
            re_gpa=o_gpa.pop(which)
            r_name.append(re_name)
            r_roll.append(re_roll)
            r_age.append(re_age)
            r_address.append(re_address)
            r_phone.append(re_phone)
            r_gpa.append(re_gpa)
            again = int(input("Any other student who left college:\t"))
            if again == 1:
                drop = 1
            else:
                break
        break
    
    print("\nThe number of update records are ",len(o_name),"\n")
    print("---------------------------------------------------------------------------------")
    print("S.N\t NAME\t ROLL\t AGE \t ADDRESS\t PHONE\t\tGPA")
    for i in range(len(o_name)):
        print("---------------------------------------------------------------------------------")
        print(i+1,"\t",o_name[i],"\t",o_roll[i],"\t",o_age[i],"\t",o_address[i],"\t",o_phone[i],"\t",o_gpa[i])
        print("---------------------------------------------------------------------------------")
    
    print("\n\nThe list of student who have left our college:\n")
    print("---------------------------------------------------------------------------------")
    print("S.N\t NAME\t ROLL\t AGE \t ADDRESS\t PHONE\t\tGPA")
    for i in range(len(r_name)):
        print("---------------------------------------------------------------------------------")
        print(i+1,"\t",r_name[i],"\t",r_roll[i],"\t",r_age[i],"\t",r_address[i],"\t",r_phone[i],"\t",r_gpa[i])
        print("---------------------------------------------------------------------------------")    

else:
    print("WOW, non of our student have left the college")
    print("The list record remains the same.")
    
#calculation in the managemnet file for the opertaion involved in list, tuple and dictionary
t_o_name=tuple(o_name)
t_o_roll=tuple(o_roll)
t_o_age=tuple(o_age)
t_o_address=tuple(o_address)
t_o_phone=tuple(o_phone)
t_o_gpa=tuple(o_gpa)

top=int(input("\n\nDo you want to know who achieved the highest among all the students ? 1 or 0 :\t"))
if(top==1):
    print("The highest GPA is :",max(t_o_gpa))
    dherai= o_gpa.index(max(o_gpa))
    print("\nThe detail of the person is given below :")
    print("---------------------------------------------------------------------------------")
    print( o_name[dherai],"\t",o_roll[dherai],"\t",o_age[dherai],"\t",o_address[dherai],"\t",o_phone[dherai],"\t",o_gpa[dherai]) 
    print("---------------------------------------------------------------------------------")
    breakpoint

low=int(input("\nDo you also want to know who achieved the least among all the students ? 1 or 0 :\t"))
if(low==1):
    print("The lowest GPA is :",min(t_o_gpa))
    thorai = o_gpa.index(min(o_gpa))
    print("\nThe detail of the person is given below :")
    print("---------------------------------------------------------------------------------")
    print( o_name[thorai],"\t",o_roll[thorai],"\t",o_age[thorai],"\t",o_address[thorai],"\t",o_phone[thorai],"\t",o_gpa[thorai]) 
    print("---------------------------------------------------------------------------------")
    print("Hope the students will get even more better eductaion.")
    breakpoint    

#printing the result of the class :
print("\n\n\t\t\tHere is the list fo result of student from the class :")
print("\n\t---------------------------------------------------------------------------------")
record=[]
record=o_gpa.copy()
record.sort(reverse=True)
print("\tRank\t NAME\t ROLL\t AGE \t ADDRESS\t PHONE\t\tGPA")
print("\t---------------------------------------------------------------------------------")
for i in range(0,len(o_name)):
        recordd  = record[i]      #nonetype error
        position = o_gpa.index(recordd)
        print("\t",i+1,"\t",o_name[position],"\t",o_roll[position],"\t",o_age[position],"\t",o_address[position],"\t",o_phone[position],"\t",o_gpa[position])
        print("\t---------------------------------------------------------------------------------") 