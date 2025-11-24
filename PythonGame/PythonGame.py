# Example file showing a basic pygame "game loop"
import pygame
import random

def DrawCircles(Surface, CircleCenters):
    for item in CircleCenters:
        pygame.draw.circle(Surface, "red", (CircleCenters.x, CircleCenters.y), 10, 0)

def GenerateCirclePositions(Amount):
    PositionList = []
    for i in range(0, Amount):
        PositionList.append(pygame.Vector2(random.randint(0, 1280), random.randint(0,720)))

    return PositionList
    
#if you see this then it worked
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
Centers = GenerateCirclePositions(10)
for i in range(0, len(Centers)):
    print(f"X: {Centers[i].x} Y: {Centers[i].y}")

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