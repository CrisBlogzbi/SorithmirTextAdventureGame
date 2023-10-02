import time

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_adventure():
    while True:
        score = 0 # Initialize score
        delay_print("Welcome to the Sorithmir Text Adventure Game!")
        delay_print("You find yourself standing at a crossroads in a dense forest. You can see a the entrance to a cave on your left. On the right you can see a lake. And in the distance, away from the two roads, you can see a giant tree.")
        delay_print("You can see a the entrance to a cave on your left.")
        delay_print("On the right you can see a lake.")
        delay_print("And in the distance, away from the two roads, you can see a giant tree.")

        cave_visited = False # Flag to track if the cave has been visited
        lake_visited = False  # Flag to track if the lake has been visited

        while True:
            delay_print("Your current score: {}".format(score))
            score, cave_visited, lake_visited, restart = crossroads(score, cave_visited, lake_visited)
            if restart:
                break

#main adventure
def crossroads(score, cave_visited, lake_visited):
    restart = False
    delay_print("What do you want to do?")

    # Determine the available choices based on cave_visited flag
    if not cave_visited:
        delay_print("1. Go left into the dark cave. Creepy, but you might find something good!")
    if not lake_visited:
        delay_print("2. Go right towards the shining lake. Always good to meditate.")
    
    delay_print("3. Go straight ahead. You need to know what's with that tree!")
    delay_print("4. Give up the adventure and go home.")
        
    choice = input("Enter your choice (1/2/3/4):\n ")
        
    if choice == '1' and not cave_visited:
        score, added_score = cave_adventure(score)
        score += added_score
        cave_visited = True
    elif choice == '2' and not lake_visited:
        score, added_score = lake_adventure(score)
        score += added_score
        lake_visited = True
    elif choice == '3':
        score, added_score, restart = giant_tree(score)
        score += added_score
    elif choice == '4':
        delay_print("Thanks for playing! Your final score is: {}".format(score))
        restart = input("Do you want to play again? (yes):\n ").lower() == 'yes'
        return score, cave_visited, lake_visited, restart
    else:
        delay_print("Invalid choice. Please enter 1, 2, 3 or 4.")
    return score, cave_visited, lake_visited, restart

#main adventure .1
def cave_adventure(score):
    added_score = 0
    delay_print("You enter the dark cave.")
    delay_print("It's eerie and you feel unconfortable. It's very dark inside, but you brought a torch with you.")
    delay_print("What do you want to do?")
    delay_print("1. Continue deeper into the cave.")
    delay_print("2. Leave the cave.")
    
    choice = input("Enter your choice (1/2):\n ")
    
    if choice == '1':
        added_score = deeper_cave()
    elif choice == '2':
        pass
    else:
        delay_print("Invalid choice. Please enter 1 or 2")
    return score, added_score
        

    
#cave adventure 
def deeper_cave():
    added_score = 0 
    delay_print("As you enter deeper into the cave, you notice a crack in the wall on your left from where a ray of light is shining out.")
    delay_print("What do you do?")
    delay_print("1. Continue exploring the cave")
    delay_print("2. Check the light.")

    choice = input("Enter your choice (1/2):\n ")

    if choice == '1':
        added_score = dead_end_cave()
    elif choice == '2':
        added_score = light_cave()
    else:
        delay_print("Invalid choice. Please enter 1 or 2.")
    return added_score


#cave adventure .1
def dead_end_cave():
    added_score = 0 
    delay_print("You find a dead end. There's nothing in here. So you walk back.")
    delay_print("As you aproach the crack in the wall, you notice the light is gone.")
    return added_score

#cave adventure .2   
def light_cave():
    added_score = 0 
    delay_print("You push yourself against the crack and the stone crumbles, revealing something that looks like a treasure room.")
    delay_print("Inside, amongst other dusty old treasure, you see a Golden Coin, sparking bright as the sun, looking as if the passing of time never got to it.")
    delay_print("What do you do?")
    delay_print("1. Take the coin with you.")
    delay_print("2. Leave the coin there. And return to the crossroads")

    choice = input("Enter your choice (1/2):\n ")

    if choice == '1':
        delay_print("Congratulations you found the Hidden treasure!")
        added_score = 10 #+10 score
    elif choice == '2':
        pass
    else:
        delay_print("Invalid choice. Please enter 1 or 2.")
    return added_score

#main adventure .2
def lake_adventure(score):
    added_score = 0 
    delay_print("As you aproach the lake you notice a swimming swan. So peaceful.")
    delay_print("What do you want to do?")
    delay_print("1. Sit on the grass and relax for a while.")
    delay_print("2. Go for a swin with the swan.")

    choice = input("Enter your choice (1/2):\n ")

    if choice == '1':
        delay_print("You feel calm. It's always nice to meditate for a while.")
        delay_print("After some time, you decide to return to the crossroads.")
        added_score = 5 #+5 score
    elif choice == '2':
        delay_print("You go for a swim. After some time, the swan aproaches you, carrying a sparkling Golden Coin in its beak.")
        delay_print("You take the Coin, amazed by it's glow and beauty and return to the crossroads.")
        added_score = 10 #+10 score
    else:
        delay_print("Invalid choice. Please enter 1 or 2.")
    return score, added_score
#main adventure .3
def giant_tree(score):
    restart = False
    added_score = 0 
    delay_print("You aproach the mighty tree and notice... it's alive! It has a face on it's trunk and you can see it's roots pulsating through the ground.")
    delay_print("As you get close to it, it lets out a grunt.")
    delay_print("Tree: Beneath me lies a portal to a magical land. Go through it at your own risk.")
    delay_print("You stare in awe, not knowing what to say.")
    delay_print("What do you do?")
    delay_print("1. Go through the portal.")
    delay_print("2. Return to the crossroads.")
    delay_print("3. You've seen enough of the forest. You decide it's time to go home.")

    choice = input("Enter your choice (1/2/3):\n ")

    if choice == '1':
        delay_print("As you go through the portal, you see a lenghty land of magical creatures.")
        delay_print("You turn around and the portal seems to be gone.")
        delay_print("Not knowing what to do, you go on to explore the land.")
        delay_print("To be continued...")
        added_score = 20 #+20 score
        score += added_score
        delay_print("Thanks for playing! Your final score is: {}".format(score))
        restart = input("Do you want to play again? (yes):\n ").lower() == 'yes'
        return score, added_score, restart
    elif choice == '2':
        delay_print("You don't trust the tree... or better said, you're afraid of it! You decide to turn back.")
    elif choice == '3':
        delay_print("After a day like that, the first thing you do after getting home, is taking a nap!")
        added_score = 5 #+5 score
        score += added_score
        delay_print("Thanks for playing! Your final score is: {}".format(score))
        restart = input("Do you want to play again? (yes):\n ").lower() == 'yes'
        return score, added_score, restart
    else:
        delay_print("Invalid choice. Please enter 1,2 or 3.")
    return score, added_score, restart
        
start_adventure()