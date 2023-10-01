import time

def delay_print(text, delay=1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_adventure()
    delay_print("Welcome to the Sorithmir Text Adventure Game!")
    delay_print("You find yourself standing at a crossroads in a dense forest. You can see a the entrance to a cave on your left. On the right you can see a lake. And in the distance, away from the two roads, you can see a giant tree.")
    delay_print("You can see a the entrance to a cave on your left.")
    delay_print("On the right you can see a lake.")
    delay_print("And in the distance, away from the two roads, you can see a giant tree.")
    while True:
def crossroads()
    delay_print("What do you want to do?")
    delay_print("1. Go left into the dark cave. Creepy, but you might find something good!")
    delay_print("2. Go right towards the shining lake. Always good to meditate.")
    delay_print("3. Go straight ahead. You need to know what's with that tree!")
    delay_print("4. Quit the game.")
        
    choice = input("Enter your choice (1/2/3/4): ")
        
    if choice == '1':
        cave_adventure()
    elif choice == '2':
        lake_adventure()
    elif choice == '3':
        giant_tree()
    elif choice == '4':
        delay_print("Thanks for playing! Goodbye.")
        break
    else:
        delay_print("Invalid choice. Please enter 1, 2, 3 or 4.")

def cave_adventure():
    delay_print("You enter the dark cave.")
    delay_print("It's eerie and you feel unconfortable. It's very dark inside, but you brought a torch with you.")
    delay_print("What do you want to do?")
    delay_print("1. Continue deeper into the cave.")
    delay_print("2. Leave the cave.")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        deeper_cave()
    elif choice == '2':
        crossroad()
    else:
        delay_print("Invalid choice. Please enter 1 or 2")
        

    
    
def deeper_cave():
    

start_adventure()
        
def score()