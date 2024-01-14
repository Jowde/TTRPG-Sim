import pygame
import World


SCREENSIZE = (720, 720)
MOVESPEED = 1
class Game:
    def __init__(self) -> None:
        
        self.world = World.generate(200, 12345)
        
        pygame.init()
        
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.clock = pygame.time.Clock()
        self.pixel_size = 12
        pygame.display.set_caption("TTRPG-Sim")
        
        self.running = True
        self.current_position = [0,0]
        
        
        
    
    def play(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_LEFT] and self.current_position[0]>0:
                    self.current_position[0] -= MOVESPEED
                    
                if keys[pygame.K_RIGHT] and self.current_position[0]+ SCREENSIZE[0]//self.pixel_size<len(self.world):
                    self.current_position[0] += MOVESPEED
                    
                if keys[pygame.K_UP] and self.current_position[1]>0:
                    self.current_position[1] -= MOVESPEED
                    
                if keys[pygame.K_DOWN] and self.current_position[1]+SCREENSIZE[1]//self.pixel_size<len(self.world):
                    self.current_position[1] += MOVESPEED
                    
                if keys[pygame.K_MINUS] and self.pixel_size>12:
                    self.pixel_size -=4
                    self.fix_current_pos()
                    
                if keys[pygame.K_EQUALS] and self.pixel_size<32:
                    self.pixel_size +=4
                    
                    
                

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")

            # RENDER YOUR GAME HERE
            self.draw_world()
            # flip() the display to put your work on screen
            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()
            
    def draw_world(self):
        for y in range(self.current_position[1], SCREENSIZE[1]//self.pixel_size + self.current_position[1]):
            for x in range(self.current_position[0], SCREENSIZE[0]//self.pixel_size + self.current_position[0]):
                if self.world[y][x].name == "grass":
                    tile = pygame.Rect(( (x-self.current_position[0])*self.pixel_size, (y-self.current_position[1])*self.pixel_size),(self.pixel_size, self.pixel_size))
                    pygame.draw.rect(self.screen, (0, 255, 0), rect=tile)
                else:
                    tile = pygame.Rect(( (x-self.current_position[0])*self.pixel_size, (y-self.current_position[1])*self.pixel_size),(self.pixel_size, self.pixel_size))
                    pygame.draw.rect(self.screen, (0, 0, 255), rect=tile)
                    
    def fix_current_pos(self):
        isFixed=False
        while isFixed:
            if SCREENSIZE[1]//self.pixel_size + self.current_position[1]>len(self.world):
                self.current_position[1]-=1
            if SCREENSIZE[0]//self.pixel_size + self.current_position[0]>len(self.world):
                self.current_position[0]-=1
                
            if not(SCREENSIZE[0]//self.pixel_size + self.current_position[0]>len(self.world) and SCREENSIZE[1]//self.pixel_size + self.current_position[1]>len(self.world)):
                isFixed=True