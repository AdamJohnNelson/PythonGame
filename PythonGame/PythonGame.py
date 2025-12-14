# Example file showing a basic pygame "game loop"
import pygame
import random

class Circles:
    def __init__(self, Surface, Amount):
        self.Surface = Surface
        self.Amount = Amount
        self.Centers = []

    def DrawCircles(self):
        for i in range(0, self.Amount):
            pygame.draw.circle(self.Surface,
                               "red",
                               (self.Centers[i].x, self.Centers[i].y),
                              self.Centers[i].z,
                             0)

    def GenerateCirclePositions(self):
        for i in range(0, self.Amount):
            self.Centers.append(pygame.Vector3(random.randint(0, 1280), random.randint(0,720), random.randint(20,60)))
            print(f"This for loop has been run {i} times.")

    
#if you see this then it worked
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

CirclesInstance = Circles(screen, 10)
CirclesInstance.GenerateCirclePositions()
print(CirclesInstance.Centers)
#pygame.mouse.set_visible(False)
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    CursorPositionX, CursorPositionY = pygame.mouse.get_pos()
    pygame.draw.rect(screen, "white", (CursorPositionX - 10, CursorPositionY - 10, 20, 20))

    CirclesInstance.DrawCircles()
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()