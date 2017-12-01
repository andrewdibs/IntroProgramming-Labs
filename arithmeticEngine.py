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

from graphics import *

def showIntro():
    print("\t\t\tArithmetic Engine\n"
          "\t\t\t================\n\n"
          "Arithmetic engine allows user to perform basic operations on two numbers.")

def getOperation():
    while True:
            
        userInput = input("Please Choose operation:\n\n"
                          "Add\n"
                          "Multiply\n"
                          "Subtract\n"
                          "Divide\n"
                          "Enter quit to exit\n"
                          ">>: ").lower()

        if userInput != "add" or userInput != "multiply" or userInput != "subtract" or userInput != "divide":
            Text(Point(5,2), "Invalid operation").draw(win)            
        else:
            
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


def main():

    showIntro()

    

    win = GraphWin("Arithmetic Engine", 400 , 300)
    win.setCoords(0,0,10,10)

    Text(Point(5,8), "Arithmetic Engine!!!").draw(win)
    operationDisplay = Text(Point(5,5),"Add\nMulitply\nDivide\nSubtract").draw(win)
    inputBox = Entry(Point(5,3),6)
    inputBox.draw(win)


    while True:

        while win.getKey() != "Return" : pass
        
            
        operation = inputBox.getText()
        
        operationDisplay.setText("Enter First Number:")

        while win.getKey() != "Return" : pass 
        
        num1 = float(inputBox.getText())

        operationDisplay.setText("Enter Second Number: ")

        while win.getKey() != "Return": pass

        num2 = float(inputBox.getText())
        

        if operation == "add":
            result = num1 + num2
            operationDisplay.setText(str(num1) + " + " +str(num2)+ " = "+ str(result))

        elif operation == "subtract":
            result = num1 - num2
            operationDisplay.setText(str(num1) + " - " +str(num2)+ " = "+ str(result))

        elif operation == "multiply":
            result = num1 * num2
            operationDisplay.setText(str(num1) + " X " +str(num2)+ " = "+ str(result))

        elif operation == "divide":
            result = num1 / num2
            operationDisplay.setText(str(num1) + " / " +str(num2)+ " = "+ str(result))

        elif operation == "quit":
            print("Thanks for using the Arithmetic Engine")
            quit()

        else:
            print("Invalid Command")
            quit()
        

main()


        
              









