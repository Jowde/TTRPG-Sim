class Tile:
    def __init__(self,name:str, coords:tuple, color_percent:float):
        self.name=name
        self.coords = coords
        self.color_percent = color_percent
        
        
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
        
        
        