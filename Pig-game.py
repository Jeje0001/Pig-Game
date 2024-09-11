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
    if players not in [2,3,4]:
        print(" Please Enter a number from 2 to 4")
    else:
        break

print(players)
    
    
    
#continue at 1:45:09