import time
import random

whiteDoorEntry = False
woodenChestEntry = False
score = 0 

def print_pause(text,pause=2):
    print(text)
    time.sleep(pause)

monsters= ["goblin","zombie","vampire","werewolf","troll",
          "giant spider","mummy","ghost","Evil fairy","Demon"]

def random_monster():
    return random.choice(monsters)   

monster= random_monster()

weapons=["sword","axe","spear","hammer","wrench","baseball ball",
         "crowbar","shovel","metal pipe","plank of wood"]

def random_weapon():
    return random.choice(weapons)

weapon= random_weapon()

def white_door():
    global whiteDoorEntry
    print_pause("You enter through the white door")
    print("you look around and you find a",weapon,"that you can use to defend yourself with against the",monster)
    print_pause("you take it and return back to the hallway you were in")
    global score
    score+=25
    print("[you gained 25 points!]")
    whiteDoorEntry= True

def wooden_chest():
    global woodenChestEntry
    print_pause("You search it until you find a big old-fashioned key that you thought could be useful")
    print_pause("you take it and return to the hallway")
    global score
    score+=25
    print("[you gained 25 points!]")
    woodenChestEntry= True 

def return_to_hallway():
    choose_door()

def basement_fight():
    global score
    print_pause("would you like to fight or run back up to the hallway?")
    print("Enter 1 to fight the",monster,)
    print_pause("Enter 2 to run away")
    fight_choice =(int(input("(Enter 1 or 2):")))
    if fight_choice==1: 
        if not whiteDoorEntry and not woodenChestEntry:
            print("you fight it but with no weapon or key to the door")
            print("you can't escape and the",monster,"kills you")
            score-=30
            print("[you lost 30 points!]")
            print_pause("game ends")
        elif not whiteDoorEntry:
            print("You have the key to escape")
            score+=25
            print("[you gained 25 points for having the key!]")
            print("but you don't have a weapon and the",monster,"kills you")
            score-=15
            print("[you lost 15 points for not having a weapon]")
            print_pause("game ends")
        elif not woodenChestEntry:
            print("you use your",weapon,"to kill the monster")
            score+=25
            print("[you gained 25 points for killing the monster!]")
            print_pause("but don't have a key to open the door and escape!")
            score-=15
            print("[you lost 15 points for not having the key]")
            print_pause("you go back to the hallway")
            return_to_hallway()
        else:
            print("with your",weapon,"you hit the monster and kill it")
            print_pause("you use the key you got to escape through the door and out of the house")
            score+=40
            print("you gained 40 points!")
            print("you have a total score of",score,"points!")      
            print("game ends")
    elif fight_choice==2:
        return_to_hallway()
    else:
        print(int(input("(Enter 1,2):")))     

def choose_door():
    print_pause("what would you like to do")
    while True:
      try:
            first_choice= (int(input("Enter (1,2 or 3): ")))
            if first_choice==1:
                if not whiteDoorEntry:
                    print("you open the white door and go in")
                    white_door()
                else:
                    print("you already entered the room, nothing is here")
                return_to_hallway()
                break
            elif first_choice==2:
                if not woodenChestEntry:
                    print("You open the wooden chest and check what is inside")
                    wooden_chest()
                else:
                    print("there is nothing else here")
                return_to_hallway()
                break
            elif first_choice==3:
                print("you enter the basement and go down stairs")
                print("you come face to face with the",monster,"and behind it a door to escape")
                basement_fight()
                break
            else:
                global score 
                score-=10
                print("you lost 10 points for entering a wrong number")
                print(int(input("Enter 1,2 or 3")))
      except ValueError: 
               print("Invalid.")

print("You find yourself standing in the hallway of an old house and you hear" \
" the sound of a" ,monster, "coming from somewhere in the house")
print_pause("you look around and you find a plain white door, a wooden chest and a door leading to the basement")
print_pause("Enter 1 to open the white door")
print_pause("Enter 2 to check the wooden chest")
print_pause("Enter 3 to open do down the basement")
choose_door()

