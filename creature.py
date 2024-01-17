from stats import Stats
class Creature:
    
    def __init__(self, race_name:str, stats:Stats):
        self.name = race_name
        
        self.stats = stats
        self.calculate_advance_stats()
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
     
    def calculate_advance_stats(self):
        str = self.stats.str
        dex = self.stats.dex
        con = self.stats.con
        self.melee_attack_damage: int
        
        self.melee_attack_damage += str
        self.carrying_capacity = str * 15
        self.equipment_carrying_capacity = str * 10
        
        self.melee_attack_damage += dex
        self.speed = dex
        self.inititive = dex 
        
        self.max_health = con * 5
        self.current_health = self.max_health
        self.armor_points = con
        
        
    
        
 
        
        
        