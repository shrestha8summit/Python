name = input("Enter the full name of the employee: ")
design = input("Enter the designation of the employee: ")
salary = int(input("Enter the current net salary: $"))
cdone = input("Has the employee applied for the training program (Y/N)?: ")

compulsory = []
optional = []

def performanceBonus():
    if cdone.upper() == "Y":
        for i in range(1,11):
            percent = float(input(f"Grades of Modules {i} (Compulsory) in % : "))
            compulsory.append(percent)
        fail = 0
        for i in compulsory:
            if i < 70:
                fail += 1
        
        if fail != 0:
            print(f"This employee failed {fail} module and is not eligible for any bonus. They must enroll into this program again next year")
            return False

        elif fail == 0:
            print("This employee passed all the compulsory modules and got $5000 as a performance bonus.")
            odone = input(" Has this employee completed any optional module(Y/N): ")    
            if odone.upper() == "N":
                return 5000

            elif odone.upper() == "Y":
                oComp = int(input("How many optional modules are passed and completed?: "))
                optional.append(oComp)
                print(f"This employee passed {oComp} optional modules and got ${oComp * 500} as an performance bonus.")
                return oComp * 500 + 5000

    elif cdone.upper() == "N":
        print("This employee is not eligible for any performance bonus and they must enroll into this program next year.")
        return False

check = performanceBonus()
if check != False:
    print(f"The total bonus of this employee is: ${check}")
    print(f"The updated salary is: ${salary + check}")