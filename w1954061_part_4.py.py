# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.
    #https://stackoverflow.com/questions/62099060/what-is-the-scope-of-global-variables-between-two-functions

# Student ID: w1954061
#Date: 27/11/2022

#Variables
user_input = 0
student_id =''
pass_credit = 0
defer_credit = 0
fail_credit = 0
total_credit = 0
num_progress = 0
num_trailer = 0
num_exclude = 0
num_retriever = 0
total_outcomes = 0
student_data ={}
progression_outcome=''

#Part_1
#Student version
def student_input_validation(student_credit_message):
    while True:
        try:
            student_credit = int(input(student_credit_message))
            if student_credit not in range(0,121,20):
                print("Out of range\n")
                continue

        except ValueError:
            print("Integer required\n")
            continue

        break
    return student_credit


def student_progression():
    while True:
        pass_credit = student_input_validation("Please enter your credit at pass: ")
        defer_credit = student_input_validation("Please enter your credit at defer: ")
        fail_credit = student_input_validation("Please enter your credit at fail: ")
        total_credit = pass_credit + defer_credit + fail_credit

        if total_credit != 120:
            print("Total incorrect\n")
            

        elif pass_credit == 120: #Only one progression outcome if pass_credit = 120
            print("progress\n")

        elif pass_credit == 100: #Only one progression outcome if pass_credit = 100
            print("Progress ( module trailer )\n") 

        elif fail_credit == 120 or fail_credit == 100 or fail_credit == 80:
            print("Exclude\n")

        else: #after all the conditions passed the only outcome that could be is module retriever
            print("Do not progress - module retriever\n") 
     
        break


#Part_1
#staff version
#Function for staff input validation
def staff_input_validation(staff_credit_message):
    while True:
        try:
            staff_credit = int(input(staff_credit_message))
            if staff_credit not in range(0,121,20):
                print("Out of range\n")
                continue

        except ValueError:
            print("Integer required\n")
            continue

        break
    return staff_credit#For further calculations in the program, the value of staff_credit is needed. If the return statement is not used, a TypeError will occur.


#Part_4
#Function for staff progression outcomes 
def staff_progression():
    
    global num_progress , num_trailer , num_exclude , num_retriever #Global variables are declared and defined outside any function in the program. 
    
    while True:
        student_id = input("please enter student id: ")
        if student_id in student_data:
            print("The student id already exists")
            continue
        pass_credit = staff_input_validation("Enter your total PASS credits: ")
        defer_credit = staff_input_validation("Enter your total DEFER credits: ")
        fail_credit = staff_input_validation("Enter your total FAIL credits: ")
        total_credit = pass_credit + defer_credit + fail_credit

        if total_credit != 120:
            print("Total incorrect\n")
            continue  

        
        elif pass_credit == 120: #Only one progression outcome if pass_credit = 120
            print("progress\n")
            num_progress += 1
            progression_outcome = 'Progress'

        elif pass_credit == 100: #Only one progression outcome if pass_credit = 100
            print("Progress ( module trailer )\n")
            num_trailer += 1
            progression_outcome = 'Progress ( module trailer )'

        elif fail_credit == 120 or fail_credit == 100 or fail_credit == 80:
            print("Exclude\n")
            num_exclude += 1
            progression_outcome = 'Exclude'

        else:
            print("Do not progress - module retriever\n")
            num_retriever += 1
            progression_outcome = 'Module retriver'

         #Part_4 #Appending dictionary with progression outcomes and credit values
        student_data[student_id] = progression_outcome,pass_credit,defer_credit,fail_credit

        break


#Function for staff histogram
def histogram(category,num_student):
    print(f"{category:<10}{num_student} : ", num_student * "*")


#Function for staff users for multiple outcomes
def staff_start():
    while True:

        staff_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        print()
        staff_input = staff_input.lower()

        if staff_input == 'y':
            staff_progression()
            

        elif staff_input=='q':
            print("-"*65)
            print("Histogram")
            histogram("Progress",num_progress)
            histogram("Trailer",num_trailer)
            histogram("Retriever",num_retriever)
            histogram("Excluded",num_exclude)
            total_outcomes = num_progress+num_trailer+num_exclude+num_retriever
            print(f"\n\n{total_outcomes} outcomes in total.")
            print("-"*65)
            print()
            print("Part 4:")
            for key in student_data.keys():
                value = student_data[key]
                
                print(key,':',value[0],'-',value[1],',',value[2],',',value[3])#part_4contd- print the keys and values in the dictionary.
                print()
            
            break

        else:
            print("Invalid input")
            

#Staff version will be looped with this code            
def staff_version():
    while True:
            staff_progression()
            staff_start()
            break # After user input 'q' staff_progression should not be executed again. For that purpose breaking outof this loop is needed.


#Menu option for user to choose the preffered version as there're two types of users.(staff and student)
while True:
    print(" Enter '1' to open the Student Version\n Enter '2' to open the Staff Version\n Enter '3' to exit the program")
    print()
    user_input = input(">>>")

    if user_input == '1':
        print("Student Version")
        print()
        student_progression()

    elif user_input == '2':
        print("Staff Version")
        print()
        staff_version()

    elif user_input == '3':
        break

    else:
        print("Invalid input\n")
        #continue is not needed because it's an infinite loop and as this is the last line loop will keep executing
        

