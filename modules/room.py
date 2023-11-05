import random
#from monster import Monster


class Room:
    def __init__(self): 
        self.str_description = ""
        self.list_monsters = []
        self.list_doors = []
        self.bool_seached = False
        
    def addMonsters(self, list_monsters):
        for monster in list_monsters:
            self.list_monsters.append(monster)

    def removeMonster(self, monster):
        if monster in self.list_monsters:
            self.list_monsters.remove(monster)

    def resetRoom(self):
        self.str_description = ""
        self.list_monsters = []
        self.list_doors = []
        self.bool_seached = False


    #def seachRoom(self): #Not finished
        #if not self.bool_seached: # Check if room has been seached
         #   rng = random.randint(1,100)
          #  if rng <= 50:                   #Normal Rarety
           #     lootname = "sword"
            #    lootrarety = "normal"
             #   loot = "loot"
            #elif rng > 50 and rng <= 80:    #Common Rarety
             #   lootname = "sword"
              #  lootrarety = "common"
               # loot = "loot"
           # elif rng > 80 and rng <= 95:    #Rare Rarety
             #   lootname = "sword"
            #    lootrarety = "rare"
              #  loot = "loot"
           # elif rng > 95 and rng <=100:    #Epic Rarety
            #    lootname = "sword"
             #   lootrarety = "epic"
              #  loot = "loot"
            
            #str_lootFound = "You seach the room and you find a " + lootname + " of " + lootrarety + " rarety"
            #self.bool_seached = True

            #return [str_lootFound, loot] # 0 = str | 1 = loot obj
            
       # else:
           # return ["You have alredy looted this room."]
            


    def createRoom(self): #Creates room
        for i in range(3): #Randomly choose which directions to create doors
            self.bool_door = random.choice([True, False]) 
            self.list_doors.append(self.bool_door)
            
            if True not in self.list_doors:
                self.list_doors[0] = True #If no doors create one heading north 



        #Create discription
        list_roomDes1 = ["You stand in a darkly lit room,", "You stand in a dark and cold room,", "The room is iluminated by two tourches on either side of the room,"]
        list_roomDes2 = ["you feel the water up to you ankles.", "water drippinng from the roof above you forming into a small puddle.", "you see the cockroaches scurrying away into the crevices."]

        self.str_description = f"\n{random.choice(list_roomDes1)} {random.choice(list_roomDes2)}" #Randomly combine the 2 substrings to for the description of the room


    def getDescription(self):

    #Describe Hostiles
        list_monstersNameInRoom = []
        list_monstersInRoom = []


        list_monsterLoc = ["standing in the middle of the room.", "standing in a corner.", "sitting up against the wall"] #List of descriptors for the hostiles location

        for monster in self.list_monsters:
            
            str_monsterDetails = f"{monster.Name} has {monster.Health} health and {monster.Strength} damage\n"
            list_monstersInRoom.append(str_monsterDetails)
            list_monstersNameInRoom.append(monster.Name)
    	    
        
    

        str_monsterDes = f"You see, {len(self.list_monsters)} monsters {random.choice(list_monsterLoc)}\n {' '.join(map(str, list_monstersInRoom))}"

    #Describe doors
        list_direction = []   
        directions = ["North", "South", "East", "West"]

        for i in range(len(self.list_doors)):
            if self.list_doors[i] == True:
                #print(self.directions[i])
                #print(self.directions)
                list_direction.append(directions[i])


        str_direction = ", ".join(str(x) for x in list_direction)
     
        str_door = "doors"

        if self.list_doors.count(True) == 1:
            str_door = "door"


        str_doorsAmount = self.list_doors.count(True)

        str_doorsDes = f"The room contains {str(str_doorsAmount)} {str_door} heading {str_direction}"
   

        return f"{self.str_description}\n{str_doorsDes}\n{str_monsterDes}" ## Returns description of Room, Hostiles amd doors




if __name__ == "__main__":
 

   # Monster1 = Monster("Goblin", 30, 10, 8) 

    #Monster2 = Monster("Skeleton", 25, 3, 10) 

    #Monster3 = Monster("Troll", 50, 8, 15) 

    #Monster4 = Monster("Vampyre", 45, 5, 12) 

    #Monster5 = Monster("Giant", 80, 10, 20) 

    #Monster6 = Monster("Dragon",100,30,50) 

    
    
    

    #monstre_liste = [Monster1, Monster2, Monster3, Monster4, Monster5, Monster6] 

    

    room = Room()
    room.createRoom()



    #room.addMonsters([[Monster1, 2], [Monster2, 1], [Monster3, 5]])
    #room.addMonsters([Monster1, Monster2, Monster3])
    print(room.getDescription())
    #print(room.seachRoom()[0])