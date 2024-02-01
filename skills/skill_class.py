class Skill:
    def __init__(self, name:str, catergory:str):
        self.name = name
        self.catergory = catergory
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def catergory(self):
        return self._catergory
    @catergory.setter
    def catergory(self, value):
        self._catergory = value