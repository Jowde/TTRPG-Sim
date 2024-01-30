import random
import actions
class Creature:
    def __init__(self, x: int, y: int, name: str):
        self.x, self.y = x, y
        self.name = name
        self.max_hp = 10  # Initial health
        self.hp = 10
        self.phy_atk = 1
        self.phy_def = 1
        self.speed = 1
        self.energy = 100
        
        
        self.actions = ["wander(self.x,self.y)","heal(self.health)"]
        
    def think(self):
        action_name, action_type, *content = eval("actions." + random.choice(self.actions))
        print(f"{self.name}: {action_name}")
        return action_name, action_type, content
        
    def getCoords(self):
        return self.x, self.y
    
    def changeCoords(self,x,y):
        self.x, self.y = x,y
        
    def __str__(self):
        response = ""
        response += f"\nName: {self.name}\n"
        response += f"Coords: {self.x}, {self.y}\n"
        response += f"Health: {self.health}\n"
        return response
                  