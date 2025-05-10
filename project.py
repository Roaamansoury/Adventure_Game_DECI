import time
def print_pause(text,pause=2):
    print(text)
    time.sleep(pause)

monsters= ["goblin","zombie","vampire","werewolf","troll",
          "giant spider","mummy","ghost","Evil fairy","Demon"]
import random
def random_monster():
    return random.choice(monsters)   
monster= random_monster()

weapons=["sword","axe","spear","hammer","wrench","baseball ball",
         "crowbar","shovel","metal pipe","plank of wood"]
import random
def random_weapon():
    return random.choice(weapons)
weapon= random_weapon()

def purple_door():
    print_pause("You enter through the purple door")
    print("you look around and you find a",weapon,"that you can use to defend yourself with against the",monster)
    print_pause("you take it and return back to the hallway you were in")

def silver_door():
    print_pause("you enter through the silver door")
    print_pause("you search the room until you find a big old-fashioned key that you thought could be useful")
    print_pause("you take it and return to thr hallway")  

def return_to_hallway():
    choose_door()

def choose_door():
    print_pause("what would you like to do")
    while True:
      try:
            first_choice= (int(input("[Enter 1,2 or 3]")))
            if first_choice==1:
                print("you open the purple door and go in")
                purple_door()
                return_to_hallway()
                break
            elif first_choice==2:
                print("You open the silver door and go in")
                silver_door()
                return_to_hallway()
                break   
            elif first_choice==3:
                print("you enter through the green door")     
                break
            else: print(int(input("Enter 1,2 or 3")))
      except ValueError: 
               print("Invalid.")


print("You find yourself standing in the hallway of an old house and you hear the sound of a" ,monster, "coming from somewhere in the house")
print_pause("you look around and you find a purple door, a silver door and a green door")
print_pause("Enter 1 to open the purple door")
print_pause("Enter 2 to open the silver door")
print_pause("Enter 3 to open the green door")
choose_door()


