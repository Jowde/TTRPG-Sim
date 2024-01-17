import pygame
import world

DEFAULT_SCREEN_SIZE = (720, 720)
MOVE_SPEED = 4
WORLD_SIZE = 100
SEED = 12345

class Game:
    def __init__(self) -> None:
        # Initialize the game
        self.world = world.generate(WORLD_SIZE, SEED)
        
        pygame.init()
        self.screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE)
        # Uncomment the line below if you want to enable fullscreen mode
        # self.screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE, pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.pixel_size = 12
        pygame.display.set_caption("TTRPG-Sim")
        
        self.running = True
        self.current_position = [0, 0]
        self.pause = False
        
    def play(self):
        while self.running:
            # Main game loop
            screen_size = self.screen.get_size()
            
            self.gameloop()    

            for event in pygame.event.get():
                self.user_input(event, screen_size)
                
            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Render the game
            self.draw_world(screen_size)
            
            # Update the display
            pygame.display.flip()
            self.clock.tick(60)  # Limit FPS to 60

        pygame.quit()

# ============================================== Important Functions ==============================================
    def user_input(self, event, screen_size):
        # Handle user input events
        if event.type == pygame.QUIT:
            self.running = False
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.pause = not self.pause
        
        if self.pause:
            self.running = False
        else:
            # Handle Camera Movement
            self.handle_camera_movement(keys, screen_size)
            
            # Handles Zoom in and out
            self.handle_zoom(keys, screen_size)
            
    def handle_camera_movement(self, keys, screen_size):
        # Handle camera movement based on arrow keys
        if keys[pygame.K_LEFT] and self.current_position[0]  > 0:
            self.current_position[0] -= MOVE_SPEED
                
        if keys[pygame.K_RIGHT] and self.current_position[0] + MOVE_SPEED + screen_size[0] // self.pixel_size < len(self.world):
            self.current_position[0] += MOVE_SPEED
                
        if keys[pygame.K_UP] and self.current_position[1] > 0:
            self.current_position[1] -= MOVE_SPEED
                
        if keys[pygame.K_DOWN] and self.current_position[1] + MOVE_SPEED + screen_size[1] // self.pixel_size < len(self.world):
            self.current_position[1] += MOVE_SPEED
            
    def handle_zoom(self, keys, screen_size):
        # Handle zoom in and out based on '+' and '-' keys
        if keys[pygame.K_MINUS] and self.pixel_size > 4 and screen_size[0] // (self.pixel_size - 4) < len(self.world):
            self.pixel_size -= 4
            self.fix_current_pos(screen_size)
                
        if keys[pygame.K_EQUALS] and self.pixel_size < 32:
            self.pixel_size += 4
            
    def draw_world(self, screen_size):
        # Draw the world based on the current camera position and pixel size
        for y in range(self.current_position[1], screen_size[1] // self.pixel_size + self.current_position[1]):
            for x in range(self.current_position[0], screen_size[0] // self.pixel_size + self.current_position[0]):
                if self.world[y][x].name == "grass":
                    tile_color = (0, int(255 * self.world[y][x].color_percent), 0)
                else:
                    tile_color = (0, 0, int(255 * self.world[y][x].color_percent))
                    
                tile = pygame.Rect(((x - self.current_position[0]) * self.pixel_size, 
                                    (y - self.current_position[1]) * self.pixel_size),
                                   (self.pixel_size, self.pixel_size))
                pygame.draw.rect(self.screen, tile_color, rect=tile)
                    
    def fix_current_pos(self, screen_size):
        # Fix current position to ensure it is within valid bounds
        while screen_size[1] // self.pixel_size + self.current_position[1] > len(self.world):
            self.current_position[1] -= 1
        while screen_size[0] // self.pixel_size + self.current_position[0] > len(self.world):
            self.current_position[0] -= 1

    def gameloop(self):
        # Placeholder for the main game logic
        pass
