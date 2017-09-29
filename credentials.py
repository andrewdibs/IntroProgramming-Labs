# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Andrew DiBella
# Created: 2017-09-29

def main():

    # get user's first and last names
    
    def getName():
         
        first = input("Enter your first name: ")
        last = input("Enter your last name: ")
        name = [first, last]

        return name
    
    nameList = getName()
    
# TODO modify this to generate a Marist-style username
    def getUserName():
        uname = nameList[0]+"."+ nameList[1] + "@marist.edu"

        return uname

    userName = getUserName()

    
    def setPassword():
        while True:
            passwd = input("Create a new password: ")
            print("Fool of a Took! That password is feeble!")
        
            if len(passwd) >= 8:
                print("The force is strong in this one…")
                break

        return passwd
            
    password = setPassword()

    print("Account configured. Your new email address is",
                userName + "@marist.edu")

    
main()
