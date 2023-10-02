import time

def delay_print(text, delay=0.005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_adventure():
    delay_print("Welcome to the Sorithmir Text Adventure Game!")
    delay_print("You find yourself standing at a crossroads in a dense forest. You can see a the entrance to a cave on your left. On the right you can see a lake. And in the distance, away from the two roads, you can see a giant tree.")
    delay_print("You can see a the entrance to a cave on your left.")
    delay_print("On the right you can see a lake.")
    delay_print("And in the distance, away from the two roads, you can see a giant tree.")

    # Initialize score
    global score
    score = 0

    while True:
        delay_print("Your current score: {}".format(score))
        crossroads(score)


#main adventure
def crossroads(score):
    delay_print("What do you want to do?")
    delay_print("1. Go left into the dark cave. Creepy, but you might find something good!")
    delay_print("2. Go right towards the shining lake. Always good to meditate.")
    delay_print("3. Go straight ahead. You need to know what's with that tree!")
    delay_print("4. Quit the game.")
        
    choice = input("Enter your choice (1/2/3/4): ")
        
    if choice == '1':
        score += cave_adventure()
    elif choice == '2':
        score += lake_adventure()
    elif choice == '3':
        score += giant_tree()
    elif choice == '4':
        delay_print("Thanks for playing! Your final score is: {}".format(score))
        return score
    else:
        delay_print("Invalid choice. Please enter 1, 2, 3 or 4.")
    return score

#main adventure .1
def cave_adventure():
    delay_print("You enter the dark cave.")
    delay_print("It's eerie and you feel unconfortable. It's very dark inside, but you brought a torch with you.")
    delay_print("What do you want to do?")
    delay_print("1. Continue deeper into the cave.")
    delay_print("2. Leave the cave.")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        return deeper_cave()
    elif choice == '2':
        return crossroads(score)
    else:
        delay_print("Invalid choice. Please enter 1 or 2")
        

    
#cave adventure 
def deeper_cave():
    delay_print("As you enter deeper into the cave, you notice a crack in the wall on your left from where a ray of light is shining out.")
    delay_print("What do you do?")
    delay_print("1. Continue exploring the cave")
    delay_print("2. Check the light.")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        return dead_end_cave()
    elif choice == '2':
        return light_cave()
    else:
        delay_print("Invalid choice. Please enter 1 or 2.")


#cave adventure .1
def dead_end_cave():
    delay_print("You find a dead end. There's nothing in here. So you walk back.")
    delay_print("As you aproach the crack in the wall, you notice the light is gone.")
    return crossroads(score)

#cave adventure .2   
def light_cave():
    delay_print("You push yourself against the crack and the stone crumbles, revealing something that looks like a treasure room.")
    delay_print("Inside, amongst other dusty old treasure, you see a Golden Coin, sparking bright as the sun, looking as if the passing of time never got to it.")
    delay_print("What do you do?")
    delay_print("1. Take the coin with you.")
    delay_print("2. Leave the coin there. And return to the crossroads")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        delay_print("Congratulations you found the Hidden treasure!")
        return 10
        #+10 score
    elif choice == '2':
        return crossroads(score)
    else:
        delay_print("Invalid choice. Please enter 1 or 2.")

#main adventure .2
def lake_adventure():
    delay_print("As you aproach the lake you notice a swimming swan. So peaceful.")
    delay_print("What do you want to do?")
    delay_print("1. Sit on the grass and relax for a while.")
    delay_print("2. Go for a swin with the swan.")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        delay_print("You feel calm. It's always nice to meditate for a while.")
        delay_print("After some time, you decide to return to the crossroads.")
        crossroads(score)
        return 5
        #+5 score
    elif choice == '2':
        delay_print("You go for a swim. After some time, the swan aproaches you, carrying a sparkling Golden Coin in its beak.")
        delay_print("You take the Coin, amazed by it's glow and beauty and return to the crossroads.")
        crossroads(score)
        return 10
        #+10 score
    else:
        delay_print("Invalid choice. Please enter 1 or 2.")
#main adventure .3
def giant_tree():
    delay_print("You aproach the mighty tree and notice... it's alive! It has a face on it's trunk and you can see it's roots pulsating through the ground.")
    delay_print("As you get close to it, it lets out a grunt.")
    delay_print("Tree: Beneath me lies a portal to a magical land. Go through it at your own risk.")
    delay_print("You stare in awe, not knowing what to say.")
    delay_print("What do you do?")
    delay_print("1. Go through the portal.")
    delay_print("2. Return to the crossroads.")
    delay_print("3. You've seen enough of the forest. You decide it's time to go home.")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        delay_print("As you go through the portal, you see a lenghty land of magical creatures.")
        delay_print("You turn around and the portal seems to be gone.")
        delay_print("Not knowing what to do, you go on to explore the land.")
        delay_print("To be continued...")
        delay_print("Thanks for playing! Goodbye.")
        return 20
        #+20 score
    elif choice == '2':
        delay_print("You don't trust the tree... or better said, you're afraid of it! You decide to turn back.")
        crossroads(score)
    elif choice == '3':
        delay_print("After a day like that, the first thing you do after getting home, is taking a nap!")
        delay_print("Thanks for playing! Goodbye.")
        #+5 score
        return 5
    else:
        delay_print("Invalid choice. Please enter 1,2 or 3.")
        
start_adventure()
        