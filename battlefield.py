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

    def display_welcome(self):
        print("\nWelcome to the fight! Find out who is stronger, a robot or a dinosaur!\n Time to place your bets!!\n")

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
