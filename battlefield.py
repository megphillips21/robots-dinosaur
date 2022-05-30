from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
   
   def __init__(self): 
    self.robot = Robot('Beep-Boop')
    self.dinosaur = Dinosaur('Toothy',20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass
    
    def display_welcome(self):
        print("\nWelcome to the fight! Find out who is stronger, a robot or a dinosaur!\n Time to place your bets!!\n")
        pass
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
            pass

        

    def display_winner(self):
        pass
