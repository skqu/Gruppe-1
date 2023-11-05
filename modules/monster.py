import random
#from loot import Loot





class Monster:

    def __init__(self, Name, Health, Defence, Strength, Loot):
        self.Name = Name
        self.Health = Health
        self.Defence = Defence
        self.Strength = Strength
        self.Loot =  Loot

    def take_dmg(self, dmg):
        BR = random.choice ([True, False])
        if BR == True:
                print(f"{self.Name} used defence, and blocked {self.Defence} of your damage!")
                self.Health -= (dmg - self.Defence)
                if self.Health < 0:
                    self.Health = 0
        else:  
            if dmg < self.Health:
                self.Health -= dmg
            else:
                self.Health = 0
                

    def Attack(self):
        return self.Strength

#Monster1 = Monster("Goblin", 30, 10, 8)
#Monster2 = Monster("Skeleton", 25, 3, 10)
#Monster3 = Monster("Troll", 50, 8, 15)
#Monster4 = Monster("Vampyre", 45, 5, 12)
#Monster5 = Monster("Giant", 80, 10, 20)
#Monster6 = Monster("Dragon",100,30,50) 

 

 

#monstre_liste = [Monster1, Monster2, Monster3, Monster4, Monster5, Monster6] 

 