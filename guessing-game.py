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
        
        if guess == animal:
            answer = False
            print("Wow, you got it.")
            
        elif guess == "quit":
            answer = False
            print("Thanks for playing.")

        else:
            print("Incorrect.. Try Again\n")
main()
    
