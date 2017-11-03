#Author Andrew DiBella
#Date: 3 November
#Navigation Matrix


curEmotion = 3
interaction = 0
anger   = 0
disgust = 1
fear    = 2
happy   = 3
sadness = 4
surprsie= 5

def showIntro():
    print("\t\tPersonality Artificial Intelligence\n"
          "\t\t===================================")

    
def getInteraction():
    while True:
        
        interaction = input("Enter interaction \n"
                            "Reward\n"
                            "Punish\n"
                            "Threaten\n"
                            "Joke\n"
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

def lookupEmotion(curEmotion, interaction ):


    matrix = [# reward  punish  threaten  joke
                [1,     4,      5,        0] #anger     0 
         ,      [3,     0,      0,        5] #disgust   1
         ,      [3,     4,      1,        0] #fear      2
         ,      [3,     4,      0,        5] #happiness 3
         ,      [3,     0,      1,        0] #sadness   4
         ,      [3,     4,      1,        3] #surprise  5

        ]
    return matrix[curEmotion][interaction]

def showEmotion(curEmotion):
    if curEmotion == 0:
        print("Screw you.")
    elif curEmotion == 1:
        print("You disgust me.")
    elif curEmotion == 2:
        print("AHHH!")
    elif curEmotion == 3:
        print("Woooohoo!")
    elif curEmotion == 4:
        print(":,( " )
    elif curEmotion == 5:
        print("Wow!")
    
            
showIntro()

while True:
    showEmotion(curEmotion)
    interaction = getInteraction()
    curEmotion = lookupEmotion(curEmotion, interaction)
    
    
    
