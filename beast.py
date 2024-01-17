
from creature import Creature
from stats import Stats
class Beast(Creature):
    def __init__(self, race_name:str ,stats:Stats, name=None):
        super().__init__(race_name,stats)
        
        self.name = name
            
        def wander(self):
            pass
        