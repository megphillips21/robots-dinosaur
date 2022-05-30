from weapon import Weapon

class Robot:

    def __init__(self, name_passed):
        self.name = name_passed
        self.health = 100
        self.active_weapon = Weapon('Laser', 20)

    def attack(self, dinosaur):
        pass



