import random

def roll():
    min_val=1
    max_val=6

    val=random.randint(min_val,max_val)
    return val


val=roll()
print(val)

while True:
    players=input("Enter the number of players (2 - 4): ")

    if players.isdigit():
        players=int(players)
        if players in [2,3,4]:
              break
        else:
            print("Must be between 2 - 4 players")
            
    else:
        print("Invalid, Try Again")



max_score=50
player_scores=[0 for _ in range(players)]
    
while max(player_scores) < max_score:
        currentscore=0
        should_roll=input("Would you like to roll (y)?")
        if should_roll.lower() != "y":
            break
            
        value=roll() 
        if value == 1:
             print("You rolled a 1! Turn done")
        else:
             print("You rolled a:",value)
                     
#continue at 1:50:20