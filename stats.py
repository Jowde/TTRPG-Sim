from dataclasses import dataclass

@dataclass
class Stats:
    str: int
    dex: int
    con: int
    
    def increase_str(self, value:int=1) -> None:
        self.str += value
        
    def decrease_str(self, value:int=1) -> None:
        self.str -= value
        
    def increase_dex(self, value:int=1) -> None:
        self.str += value
        
    def decrease_dex(self, value:int=1) -> None:
        self.str -= value
        
    def increase_con(self, value:int=1) -> None:
        self.str += value
        
    def decrease_con(self, value:int=1) -> None:
        self.str -= value
        
    
        