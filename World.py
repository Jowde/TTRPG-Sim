import numpy as np
from tile import Tile
from scipy.ndimage.interpolation import zoom

def generate(size: int,seed)->list:
    world_template = world_template_generate(size,seed)
    world = tile_placer(world_template)
    return world


def world_template_generate(size: int, seed: int)->list:
    
    
    rng = np.random.default_rng(seed)
    
    world_template = rng.uniform(size=(size//8,size//8))
    
    world_template = np.pad(world_template, pad_width=1,mode='constant')
    
    world_template = zoom(world_template, 8)
    
    return world_template


            
            
def tile_placer(world_template: list):
    
    world = []
    
    
    for y in range(len(world_template)):
        world.append([])
        for x in range(len(world_template)):
            print(world_template[y][x])
            if world_template[y][x]>.4:
                world[y].append(Tile("grass", (x,y), world_template[y][x] if world_template[y][x]<1 else 1))
            else:
                world[y].append(Tile("water", (x,y), world_template[y][x] if world_template[y][x]<1 else 1))
                
    return world
            