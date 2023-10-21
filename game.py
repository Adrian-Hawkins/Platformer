import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))