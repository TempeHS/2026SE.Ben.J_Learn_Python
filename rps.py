import random
### Start routine bash python rps.py

#enter and store name as a variable
player_name = input("Enter player name")

#subroutine for a player to enter Choice
def player_choice():
    player_choice = input("1 = rock, 2 = paper, 3 = scissors")

#subroutine Generate a random choice
def generate_random_choice():
    return "1" #random.randint(1, 3)

#run subroutine
player_choice()

print ("Player choice is", player_choice())
print("Computer choice is", generate_random_choice())


i=0
#subroutine to compare choices
while i < 3:
    
    #subroutine of equality check or game mechanic
    
    
    i += 1
    #subroutine UI return to player
    print(i)




### End routine