import random

from modules.room import Room
from modules.hero import Hero
from modules.monster import Monster
from modules.loot import *

Monster1 = Monster("Goblin", 30, 10, 8, monster_drop())
Monster2 = Monster("Skeleton", 25, 3, 10, monster_drop()) 
Monster3 = Monster("Troll", 50, 8, 15, monster_drop()) 
Monster4 = Monster("Vampyre", 45, 5, 12, monster_drop()) 
Monster5 = Monster("Giant", 80, 10, 20, monster_drop()) 
Monster6 = Monster("Dragon",100,30,50, monster_drop()) 


Batman = Hero(100, 20, 30, 20)


room = Room()
room.createRoom()

all_monster_list = [Monster1, Monster2, Monster3, Monster4, Monster5, Monster6]
monster_list = []


def randomMonster():
    if all_monster_list:
        randomMonster = random.choice(all_monster_list)
        monster_list.append(randomMonster)
        all_monster_list.remove(randomMonster)
    return monster_list


randomMonster()
room.addMonsters(monster_list)


def combat():
    
    for monster in monster_list:
        while Batman.Liv > 0 and monster.Health > 0:
            print(f"{monster.Name} have {monster.Health} health left.")
            print(f"Batman have {Batman.Liv} health left.\n")
            valg = input("Choose to continue?: (a)ttack, (e)scape: \n")

            if valg == "a":
                Batman.angrib(monster)
                if monster.Health == 0:
                    print(f"{monster.Name} is defeated!")
                    
                    
                    for lootItem in monster.Loot:
                        if lootItem.name != None:
                            Batman.samle_op(lootItem)

                    monster_list.remove(monster) #Removes monster from the active monsters list and from the room
                    room.removeMonster(monster)
                else:
                    monster_dmg = monster.Attack()
                    Batman.tag_skade(monster_dmg)
                    print(f"{monster.Name} attacked you and inflict {monster_dmg} damage upon you!.")

            elif valg == "e":
                print("You escaped the battle.")
                move()
                init()

                break

        if Batman.Liv == 0:
            print("You were defeated.\n")
            break  
            
    #print("no monsters")       
    #move()
            

def move(): 
    
    room.resetRoom()
    room.createRoom()
    monstre_liste = randomMonster()

    room.addMonsters(monstre_liste)
    print(room.getDescription())
    

def init():
    
    print(room.getDescription())
    
    while True:
        print("Choose action: (a)ttack, (m)ove")
        str_playerInput = input()
        match str_playerInput:
            case "a" | "attack":
                combat()
            case "m" | "move":
                if room.list_monsters:
                    print("You need to defeat the monsters first")
                else :
                    move()


init()
