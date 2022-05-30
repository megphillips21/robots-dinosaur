from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Laser', 20)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} has attacked {dinosaur.name} with {self.active_weapon}')
        print(f'{dinosaur.name} health is now {dinosaur.health}')
        print(f'{self.name} health is still at {self.health}')
        pass



