import pygame
import World
class Game:
    def __init__(self) -> None:
        
        self.map = World.generate(100, 12345)
        
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        
    
    def play(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("blue")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()
            
    