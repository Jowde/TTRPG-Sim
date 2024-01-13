import numpy as np
from tile import Tile

def generate(size: int,seed)->list:
    world_template = world_template_generate(size,seed)
    world = tile_placer(world_template, size)
    print(world_template)
    return world


def world_template_generate(size: int, seed: int)->list:
    
    world_template = np.zeros(size**2)
    world_template.shape = (size,size)
    
    rng = np.random.default_rng(seed)
    
    start_y = rng.integers(0,size)
    start_x = rng.integers(0,size)
    world_template[start_y][start_x]=1
    
    
    count=0
    while count<size:
        count+=1
        for y in range(len(world_template)):
            for x in range(len(world_template)):
                if x+1 < size and y+1 < size and y>0 and x>0:
                    if world_template[y][x-1]==1:
                        world_template[y][x]=1
                        
                    elif world_template[y][x+1]==1:
                        world_template[y][x]=1
                        
                    elif world_template[y-1][x]==1:
                        world_template[y][x]=1
                        
                    elif world_template[y+1][x]==1:
                        world_template[y][x]=1
                
                    
    
    
    return world_template
    
    
def tile_placer(world_template: list, size:int):
    
    world = []
    
    
    for y in range(size):
        world.append([])
        for x in range(size):
            if world_template[y][x]==1:
                world[y].append(Tile("grass", (x,y)))
            else:
                world[y].append(Tile("water", (x,y)))
                
    return world
            