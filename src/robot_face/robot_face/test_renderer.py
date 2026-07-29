import pygame
import sys

from renderer import Renderer


renderer = Renderer()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    renderer.draw()


pygame.quit()
sys.exit()
