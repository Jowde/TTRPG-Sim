class Tile:
    def __init__(self,name:str, coords:tuple):
        self.name=name
        self.coords = coords
        
        
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
        
        
        