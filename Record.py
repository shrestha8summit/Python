#use of nested if else state ment to check whether or not a person is eligible to get citizenship car and if not how  many year shall s/he
#wait
dob = int(input("Enter your year of birth in A.D \t"))
age = 2024-dob

if(dob%4==0) and(dob % 400==0) or (dob%100!=0):
    print("Oh you were born in leap year")
else:
    print("Oh, you were not born in leap year")
        
if(age>=18):
    print("You are now eligible to own the citizenship card! ")
else:
    print("No, you are not eligible to own the citizenship card.")
    i = 0
    a=0
    for i in range(age,18):
        i=age+i
        a=a+1
        #print(a)
    
    if(a==1):
        print("Now wait for only one year to own your citizenship")
    else:
        print("Only after",a," years you will be eligible to get citizenship.")