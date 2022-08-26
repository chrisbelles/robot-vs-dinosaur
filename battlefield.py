from inspect import _void


from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot("R2")
        self.dinosaur = Dinosaur("Barney", 90)
    def run_game(self): _void

    def display_welcome(self): _void
        if startBattle == "n"
            print("Welcome to the most unlikely battle of your lifetime!")
            print("Tonight we will witness the impossible.")
            print(f"{Robot.name}, A 4th generation defense-bot will fight for survival against the most primal of predators, {Dinosaur.name}")
            startBattle = input("The fighters are ready, are you? y/n: ")

    def battle_phase(self):
        if Dinosaur.health > 0 and Robot.health > 0:
            Dinosaur.attack()
            Robot.attack()
        elif Dinosaur.health =< 0:
            print(f"{Dinosaur.name} has been defeated! Your Champion is {Robot.name}!!")
            break
        elif Robot.health =< 0:
            print(f"{Robot.name} has been defeated! Your Champion is {Dinosaur.name}!!")
            break
        else:
            


    def display_winner(self): _void
        