# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Andrew DiBella
# Created: 2017-09-29

def main():

    # get user's first and last names
    
    def getName():
         
        first = input("Enter your first name: ").lower()
        last = input("Enter your last name: ").lower()
        name = [first, last]

        return name
    
    nameList = getName()
    
# TODO modify this to generate a Marist-style username
    def getUserName():
        uname = nameList[0]+"."+ nameList[1] + "@marist.edu"

        return uname

    userName = getUserName()
    
    
    def checkStrength(password):
        tmpPass = password.lower()

        if len(password) < 8 or password == tmpPass:
            return False

        return True
    
    def setPassword():
        while True:
            passwd = input("Create a new password: ")
            print("Fool of a Took! That password is feeble!")
            
            strength = checkStrength(passwd)

            if strength:
                print("The force is strong in this one…")
                break

        return passwd
            
    password = setPassword()

   

    print("\nAccount configured. Your new email address is",
                userName + "@marist.edu")

    
main()
