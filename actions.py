import random
def initalize(seed: int):
    random.seed(seed)

def wander(x:int, y:int):
    new_x = x + random.choice([-1, 0, 1])
    new_y = y + random.choice([-1, 0, 1])
    return "Aimless Wander", "movement", new_x, new_y

def heal(hp:int):
    hp*=1.2
    return "Basic Heal", "heal", hp

