class Player:

    def __init__(self, classe, name, surname):
        self.classe = classe
        self.name = name
        self.surname = surname
        self.strenght = 10
        self.stamina = 10
        self.life = 10


    def spellWarrior():
     print("i'm a Warrior")

    def Mage():
     print("i'm a Mage")

player1 = Player('Mage', 'Mathieu', 'Borges')

print(player1.name)
print(player1.classe)