import random
class Creature:
    def __init__(self, x: int, y: int, name: str, seed: int):
        self.x, self.y = x, y
        self.name = name
        self.health = 100  # Initial health
        
    
    def wander(self):
            new_x = self.x + random.choice([-1, 0, 1])
            new_y = self.y + random.choice([-1, 0, 1])
            return new_x, new_y
        
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
                  