from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
   
    def __init__(self): 
        self.robot = Robot('Beep-Boop')
        self.dinosaur = Dinosaur('Toothy',18)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass
    
    def display_welcome(self):
        print("\nWelcome to the fight! Find out who is stronger, a robot or a dinosaur!\n Time to place your bets!!\n")
        pass
    
    def display_winner(self):
        if self.robot.health > 0:
            print(f"{self.robot.name} is the winner! {self.dinosaur.name} has been defeated by the robot's {self.robot.active_weapon.name}!")
        elif self.dinosaur.health > 0:
            print(f'{self.dinosaur.name} is the winner! {self.robot.name} has been defeated! RIP {self.robot.name}')
        pass
    
    def battle_phase(self):
        still_alive = True
        while (still_alive == True):
            self.robot.attack(self.dinosaur)
            
            if self.robot.health > 0:
                still_alive == True
            if self.dinosaur.health > 0:
                still_alive == True
            if self.robot.health <=0:
                print(f'{self.dinosaur.name} has defeated {self.robot.name}')
            elif self.dinosaur.health <=0:
                print(f'{self.robot.name} has defeated {self.dinosaur.name}')
            if self.robot.health <= 0 or self.dinosaur.health <=0:
                still_alive = not still_alive
                break
            self.dinosaur.attack(self.robot)
            pass

        

  