import pygame
from world import World
from creature import Creature

DEFAULT_SCREEN_SIZE = (720, 720)
MOVE_SPEED = 4
WORLD_SIZE = 100
SEED = 987654321
NUM_CREATURES = 7
CREATURE_COLOR = (255, 0, 0)

class Game:
    def __init__(self) -> None:
        # Initialize the game
        self.world = World(WORLD_SIZE, SEED)
        self.creatures = [Creature(*self.world.get_valid_spawn(), f"Creature {i}", "human", SEED//i) for i in range(1,NUM_CREATURES+1)]
        for creature in self.creatures:
            self.world.info[creature.y][creature.x].add_creature(creature)

        
        self.current_position = [0, 0]
        self.pause = False

        pygame.init()
        self.screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE)
        # Uncomment the line below if you want to enable fullscreen mode
        # self.screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE, pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()
        self.pixel_size = 12
        pygame.display.set_caption("TTRPG-Sim")

        self.running = True

    def play(self):
        while self.running:
            # Main game loop
            screen_size = self.screen.get_size()
            
            if self.pause:
                self.gameloop()

            for event in pygame.event.get():
                self.user_input(event, screen_size)

            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Render the game
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = (mouse_pos[0]//self.pixel_size + self.current_position[0], mouse_pos[1]//self.pixel_size + self.current_position[1])
            self.draw_world(screen_size, mouse_pos)

            # Update the display
            pygame.display.flip()
            self.clock.tick(60)  # Limit FPS to 60

        pygame.quit()

    # ============================================== Important Functions ==============================================
    def user_input(self, event, screen_size):
        # Handle user input events
        if event.type == pygame.QUIT:
            self.running = False

        
        if event.type == pygame.KEYDOWN:
            self.handle_hotkeys(event)
            
            # Handle Camera Movement
            self.handle_camera_movement(event, screen_size)

            # Handles Zoom in and out
            self.handle_zoom(event, screen_size)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(self.world.info[pos[1]//self.pixel_size +self.current_position[1]][pos[0]//self.pixel_size +self.current_position[0]])
              
            

    def handle_hotkeys(self, event):
        if event.key == pygame.K_p:
            self.pause = not self.pause
            
    def handle_camera_movement(self, event, screen_size):
        # Handle camera movement based on arrow keys
        if event.key == pygame.K_LEFT and self.current_position[0] > 0:
            self.current_position[0] -= MOVE_SPEED

        if event.key == pygame.K_RIGHT and self.current_position[0] + MOVE_SPEED + screen_size[0] // self.pixel_size < len(self.world.info):
            self.current_position[0] += MOVE_SPEED

        if event.key == pygame.K_UP and self.current_position[1] > 0:
            self.current_position[1] -= MOVE_SPEED

        if event.key == pygame.K_DOWN and self.current_position[1] + MOVE_SPEED + screen_size[1] // self.pixel_size < len(self.world.info):
            self.current_position[1] += MOVE_SPEED

    def handle_zoom(self, event, screen_size):
        # Handle zoom in and out based on '+' and '-' keys
        if event.key == pygame.K_MINUS and self.pixel_size > 4 and screen_size[0] // (self.pixel_size - 4) < len(self.world.info):
            self.pixel_size -= 4
            self.fix_current_pos(screen_size)

        if event.key == pygame.K_EQUALS and self.pixel_size < 24:
            self.pixel_size += 4

    def draw_world(self, screen_size, mouse_pos):
        # Draw the world based on the current camera position and pixel size
        for y in range(self.current_position[1], screen_size[1] // self.pixel_size + self.current_position[1]):
            for x in range(self.current_position[0], screen_size[0] // self.pixel_size + self.current_position[0]):
                if self.world.info[y][x].isOccupied():
                    tile_color = CREATURE_COLOR
                else:
                    tile_color = self.get_tile_color(x, y)
                    
                if mouse_pos == (x,y):
                    tile_color = self.highlight_color(tile_color)
                       
                tile = pygame.Rect(((x - self.current_position[0]) * self.pixel_size,
                                    (y - self.current_position[1]) * self.pixel_size),
                                   (self.pixel_size, self.pixel_size))
                pygame.draw.rect(self.screen, tile_color, rect=tile)

    def get_tile_color(self, x, y):
        # Get color for non-occupied tiles
        tile_info = self.world.info[y][x]
        if tile_info.name == "grass":
            return (0, int(255 * tile_info.color_percent), 0) if tile_info.color_percent < 0.75 else (0, int(255 * 0.75), 0)
        else:
            return (0, 0, int(255 * tile_info.color_percent)) if tile_info.color_percent < 0.75 else (0, 0, int(255 * 0.75))
        
    def highlight_color(self, color):
        return (color[0]+50 if color[0]+50 <=255 else 255, color[1]+50 if color[1]+50 <=255 else 255, color[2]+50 if color[2]+50 <=255 else 255)
    
    def fix_current_pos(self, screen_size):
        # Fix current position to ensure it is within valid bounds
        while screen_size[1] // self.pixel_size + self.current_position[1] > len(self.world.info):
            self.current_position[1] -= 1
        while screen_size[0] // self.pixel_size + self.current_position[0] > len(self.world.info):
            self.current_position[0] -= 1

    def gameloop(self):
        #Main game logic
        for creature in self.creatures:
            action_name, action_type, content = creature.think()
            if action_type == "movement" and self.world.move_creature(content[0], content[1], creature):
                creature.changeCoords(content[0], content[1])
            
