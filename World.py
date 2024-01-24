import numpy as np
from tile import Tile
from scipy.ndimage.interpolation import zoom

class World:
    def __init__(self, size: int, seed: int):
        self.size = size
        self.rng = np.random.default_rng(seed)
        self.info = self.generate()

    def generate(self) -> list:
        world_template = self.world_template_generate()
        world = self.tile_placer(world_template)
        return world

    def get_valid_spawn(self):
        while True:
            x, y = int(self.rng.random() * len(self.info)), int(self.rng.random() * len(self.info))
            if self.info[y][x].name == "grass" and not self.info[y][x].isOccupied():
                return x, y

    def move_creature(self, x, y, creature):
        if self.info[y][x].name == "grass" and not self.info[y][x].isOccupied():
            self.info[y][x].add_creature(creature)
            self.info[creature.y][creature.x].remove_creature()
            return True
        return False

    def world_template_generate(self) -> list:
        world_template = self.rng.uniform(low=0, high=1.0, size=(self.size // 8, self.size // 8))
        #idx = self.rng.choice(np.arange(self.size), size=int(self.size/8), replace=False)
        #world_template.ravel()[idx]=0
        world_template = np.pad(world_template, pad_width=1, mode='constant', constant_values=[0])
        
        world_template = zoom(world_template, 8)
        return world_template

    def tile_placer(self, world_template: list):
        world = []
        for y in range(len(world_template)):
            world.append([])
            for x in range(len(world_template[y])):
                if world_template[y][x] > 0.4:
                    world[y].append(Tile("grass", (x, y), 2 * abs(world_template[y][x]) - 0.3))
                else:
                    world[y].append(Tile("water", (x, y), abs(world_template[y][x]) + 0.6))
        return world
