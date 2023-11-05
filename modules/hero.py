class Hero:
    def __init__(self, Liv, Forsvar, Styrke, våben):
        self.Liv = Liv
        self.Forsvar = Forsvar
        self.Styrke = Styrke
        self.våben = våben
        self.taske = []

    def tag_skade(self, skade):
        if skade < self.Liv:
            self.Liv -= skade
        else:
            self.Liv = 0

    def angrib(self, monster):
        totalskade = self.Styrke + self.våben
        monster.take_dmg(totalskade)

    def samle_op(self, genstand):
        self.taske.append(genstand)
        print(f"{genstand.name} was picked up and put in you backpack")

#Batman = Hero(20, 5, 8, 15)

    
    

    

    

    