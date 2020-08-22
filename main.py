import pygame
from rect import Rect

win = pygame.display.set_mode((500, 500))


def draw_background(win):
    win.fill((64, 64, 64))


rect = Rect(255, 255, 100, 100)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_background(win)

    rect.update(win, pygame.mouse.get_pos())
    pygame.display.update()


pygame.quit()
