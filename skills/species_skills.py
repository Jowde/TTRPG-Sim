from skills import skill_class

class humanoid(skill_class.Skill):
    def __init__(self, level):
        super().__init__("humanoid", "species")
        self.level = level
            
    
    def grab_item(self):
        return "grab item","collect", True