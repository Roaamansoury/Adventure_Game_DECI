import time
import random

whiteDoorEntry = False
woodenChestEntry = False
score = 0

def print_pause(text,pause=2):
    print(text)
    time.sleep(pause)

monsters= ["goblin","zombie","vampire","werewolf","troll",
          "giant spider","mummy","ghost","wicked fairy","Demon"]

def random_monster():
    return random.choice(monsters)

monster= random_monster()

weapons=["sword","axe","spear","hammer","wrench","baseball ball",
         "crowbar","shovel","metal pipe","plank of wood"]

def random_weapon():
    return random.choice(weapons)

weapon= random_weapon()

def check_score():
    if score < 0 :
        print_pause("you lost too many points, you need to restart the game!")
        restart_game()
    elif score < 90:
        print_pause("you don't have enough points to win the game")
        print_pause("you need to play again!")
        restart_game()
    elif score >= 90:
        print_pause("Congrats! you defeated the game and won!!")
        restart_game()
    else:
        pass  #do nothing

def white_door():
    global whiteDoorEntry
    print_pause("you look around and you find a "+ weapon +" that you can "
    "use to defend yourself with against the "+ monster)
    print_pause("you take it and return back to the hallway you were in")
    global score
    score+=25
    print_pause("[you gained 25 points!]")
    whiteDoorEntry= True

def wooden_chest():
    global woodenChestEntry
    print_pause("You search it until you find a big old-fashioned " \
    "key that you thought could be useful")
    print_pause("you take it and return to the hallway")
    global score
    score+=25
    print_pause("[you gained 25 points!]")
    woodenChestEntry= True

def choice_options():
    print_pause("Enter 1 to open the white door")
    print_pause("Enter 2 to check the wooden chest")
    print_pause("Enter 3 to open do down the basement")

def return_to_hallway():
    choose_way()

def game_start():
    global score, whiteDoorEntry, woodenChestEntry, weapon, monster
    whiteDoorEntry = False
    woodenChestEntry = False
    score = 0
    monster= random_monster()
    weapon= random_weapon()
    print_pause("You find yourself standing in the hallway of an old house"
    " and you hear the sound of a " + monster + " coming"
    " from somewhere in the house")
    print_pause("you look around and you find a plain white door, " \
    "a wooden chest and a door leading to the basement")
    choice_options()
    choose_way()

def restart_game():
    print_pause("Would you like to play again?")
    choice= input("Enter yes or no ")
    if choice== "yes":
        game_start()
    elif choice== "no":
        print_pause("Goodbye! thank you for playing the game!")
    else:
        print_pause("invaled.")

def basement_fight():
    global score
    while True:
          try:
            print_pause("would you like to fight or run back to the hallway?")
            print_pause("Enter 1 to fight the "+ monster)
            print_pause("Enter 2 to run away")
            fight_choice =(int(input("(Enter 1 or 2):")))
            if fight_choice==1:
                if not whiteDoorEntry and not woodenChestEntry:
                    print_pause("you fight it but with no weapon or door " \
                    "key you can't escape and the "+ monster+ " kills you")
                    score-=30
                    print_pause("[you lost 30 points!]")
                    print_pause("your total score is "+ str(score) +" points!")
                    check_score()
                elif not whiteDoorEntry:
                    print_pause("You have the key to escape")
                    score+=25
                    print_pause("[you gained 25 points for having the key!]")
                    print_pause("but you don't have a weapon")
                    score-=15
                    print_pause("[you lost 15 points for not having a weapon]")
                    print_pause(" the "+ monster +" kills you")
                    print_pause("your total score is "+ str(score) +" points!")
                    check_score()
                elif not woodenChestEntry:
                    print_pause("you use the "+ weapon +" to kill the monster")
                    score+=25
                    print_pause("[you gained 25 points for killing " \
                                "the monster!]")
                    print_pause("but don't have a key to open" \
                                "the door and escape!")
                    score-=15
                    print_pause("[you lost 15 points for not having the key]")
                    check_score()
                    print_pause("you go back to the hallway")
                    choice_options()
                    return_to_hallway()
                else:
                    print_pause("with your "+ weapon +" you hit the "
                   "monster and kill it")
                    print_pause("you use the key you got to escape" \
                    " through the door and out of the house")
                    score+=40
                    print_pause("you gained 40 points!")
                    print_pause("your total score is "+ str(score) +" points!")
                    check_score()
                break
            elif fight_choice==2:
                choice_options()
                return_to_hallway()
                break
            else:
                print_pause("invalid input")
          except ValueError:
              print_pause("invalid input")

def choose_way():
    print_pause("what would you like to do?")
    while True:
      try:
            first_choice= (int(input("Enter (1,2 or 3): ")))
            if first_choice==1:
                if not whiteDoorEntry:
                    print_pause("you open the white door and go in")
                    white_door()
                else:
                    print_pause("you already entered before, nothing is here")
                return_to_hallway()
                break
            elif first_choice==2:
                if not woodenChestEntry:
                    print_pause("You open the wooden chest "
                    "and check what is inside")
                    wooden_chest()
                else:
                    print_pause("there is nothing else here")
                return_to_hallway()
                break
            elif first_choice==3:
                print_pause("you enter the basement and go downstairs")
                print_pause("you come face to face with the "+ monster +" and "
                "behind it a door to escape")
                basement_fight()
                break
            else:
                global score
                score-=10
                print_pause("you lost 10 points for entering a wrong number")
      except ValueError:
               print_pause("Invalid.")

game_start()