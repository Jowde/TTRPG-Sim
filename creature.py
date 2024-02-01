import random
from species import Species
class Creature:
    def __init__(self, x: int, y: int, name: str, species:str, seed: int):
        self.x, self.y = x, y
        self.name = name
        self.species = Species[species]
        
        self.STR = self.species["STR"]
        self.DEX = self.species["DEX"]
        self.CON = self.species["CON"]
        
        self.skills = self.species["skills"]
        self.actions = [skill for skill in self.skills]
        
        
        self.rng = random.Random()
        self.rng.seed(seed)
        
        
    def think(self):
        action_name, action_type, *content = self.wander()
        print(f"{self.name}: {action_name}")
        return action_name, action_type, content
        
        
    def getCoords(self):
        return self.x, self.y
    
    def changeCoords(self,x,y):
        self.x, self.y = x,y
        
    def wander(self):
        self.x = self.x + 1
        self.y = self.y + 0
        return "Aimless Wander", "movement", self.x, self.y
    
    def __str__(self):
        response = ""
        response += f"\nName: {self.name}\n"
        response += f"Coords: {self.x}, {self.y}\n"
        response += f"Health: {self.hp}\n"
        return response
                  