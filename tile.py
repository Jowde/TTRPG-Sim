class Tile:
    def __init__(self,name:str, coords:tuple, color_percent:float):
        self.name=name
        self.coords = coords
        self.color_percent = color_percent
        self.creature = None
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
        
    @property
    def coords(self):
        return self._coords
    @coords.setter
    def coords(self,value):
        self._coords=value
        
    @property
    def color_percent(self):
        return self._color_percent
    @color_percent.setter
    def color_percent(self,value):
        self._color_percent=value
    
    def add_creature(self, value):
        self.creature = value
        
    def remove_creature(self):
        self.creature = None
    
    def isOccupied(self):
        if self.creature == None:
            return False
        return True
        