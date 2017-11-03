#Author Andrew DiBella
#Date: 3 November
#Navigation Matrix


currentEmotion = -1
anger   = 0
disgust = 1
fear    = 2
happy   = 3
sadness = 4
surprsie= 5


def getInteraction():
    while True:
        
        interaction = input("Enter interaction \n"
                            "Reward\n "
                            "Punish\n "
                            "Threaten \n"
                            "Joke \n"
                            ">>: ").lower()

        if interaction == "reward":
            return 0
        elif interaction == "punish":
            return 1
        elif interaction == "threaten":
            return 2
        elif interaction == "joke":
            return 3

        else:
            print("\nInvalid Command..\n")
    
