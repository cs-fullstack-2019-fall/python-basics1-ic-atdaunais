# function to ask for two student names and say they're in class
def studentName():
    student1 = input("Enter Student name: ")
    student2 = input("Enter another Student name: ")
    print(student1 + " and " + student2 + " went to class.")

# function to ask for grade and apply input extra credit
def studentGrade():
    origGrade = int(input("What is your original grade? "))
    extraCredit = int(input("Enter your extra credit: "))
    print("Your total grade is " + str(origGrade + extraCredit))

# function to add 3 input numbers together
def totalSum():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter a final number: "))
    sum = num1 + num2 + num3
    # the two options below output the same thing
    # print(str(num1) + " + " + str(num2) + " + " + str(num3) + " = " + str(sum))
    print(num1,"+",num2,"+",num3,"=", sum)

# function to check if an input number is positive, negative, or 0
def posOrNeg():
    userNum = int(input("Enter a number: "))
    if userNum < 0:
        print("Negative!")
    elif userNum > 0:
        print("Positive!")
    elif userNum == 0:
        print("You entered 0")
        
studentName()
studentGrade()
totalSum()
posOrNeg()