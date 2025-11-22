# Example file showing a basic pygame "game loop"
import pygame
import random

def DrawCircles(surface):
        xpos = random.randint(0, 1280)
        ypos = random.randint(0, 720)
        pygame.draw.circle(surface, "red", (xpos, ypos), 10, 0)

def GenerateCirclePositions(amount):
    PositionList = []
    for i in range(0, amount):
        print(f"It is printing {i} times")
    
    

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
GenerateCirclePositions(10)
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


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()