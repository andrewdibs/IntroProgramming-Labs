#numberEngine
#Author: Andrew DiBella
#Date: Oct 13 2017

#Intro ---Loop ---End
#Make functions 
#Ask for input
#Ask for two numbers 
#perform operation or quit 
#show result 
#


def showIntro():
    print("\t\t\tArithmetic Engine\n"
          "\t\t\t================\n\n"
          "Arithmetic engine allows user to perform basic operations on two numbers.")

def getOperation():

    userInput = input("Please Choose operation:\n\n"
                      "Add\n"
                      "Multiply\n"
                      "Subtract\n"
                      "Divide\n"
                      "Enter quit to exit\n"
                      ">>: ").lower()

    return userInput
                      
                      


def getInput():
    nums = []
    while True:
        try:
            nums.append(int(input("Please enter first number: ")))
            nums.append(int(input("Please enter second number: ")))
            
            break

        except:
            print("Invalid number...\n")

        

        
            
    
    return nums

def showEnding():
    print("Thanks for using the Arithmetic Engine.")


showIntro()

while True:
    
    operation = getOperation()
    numbers = getInput()

    if operation == "add":
        print("Result = ", numbers[0] + numbers[1], "\n\n")

    elif operation == "subtract":
        print("Result = ",numbers[0] - numbers[1],"\n\n")

    elif operation == "multiply":
        print("Result = " , numbers[0]* numbers[1] , "\n\n")

    elif operation == "divide":
        print("Result = ", numbers[0] / numbers[1] , "\n\n")

    elif operation == "quit":
        print("Thanks for using the Arithmetic Engine")
        quit()

    else:
        print("Invalid Command")
        quit()
        




        
              









