#guessing-game.py
#Author: Andrew DiBella
#Lab 4
#22 September

def main():

    animal = "fox"
    answer = True
    
    print("I'm thinking of an animal...")

        
    while answer:
        guess = input("Can you guess what animal I'm thinking of?\n"
                      "Enter Animal: ").lower()
        if guess[0] == "q":
            answer = False
            print("Thanks for playing.")

        elif guess == animal:
            answer = False
            print("Wow, you got it.")

            response = input("Do you like this animal? 'y' or 'n': ")

            if response == "y":
                print("Good Answer..Me too.")

            else:
                print("Wrong answer.....")
                

        else:
            print("Incorrect.. Try Again\n")
main()
    
